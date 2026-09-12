"""Bounded archive diagnostics must fail closed without reading live history."""
import binascii
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import stat
import struct
import zipfile
import zlib

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("historical_objects", ROOT / "publication/inspect_historical_objects.py")
INSPECT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSPECT)


def archive(entries):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as target:
        for name, payload in entries:
            target.writestr(name, payload)
    return stream.getvalue()


def chunk(kind, payload):
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", binascii.crc32(kind + payload) & 0xffffffff)


def png(extra=b""):
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
            + extra + chunk(b"IDAT", zlib.compress(b"\x00\x00\x00\x00")) + chunk(b"IEND", b""))


def test_exact_git_identity_and_size_required():
    data = b"bounded evidence\n"
    oid = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
    INSPECT.validate_git_blob(data, oid, len(data))
    with pytest.raises(INSPECT.InspectionError, match="identity"):
        INSPECT.validate_git_blob(data, "0" * 40, len(data))
    with pytest.raises(INSPECT.InspectionError, match="byte count"):
        INSPECT.validate_git_blob(data, oid, len(data) + 1)
    with pytest.raises(INSPECT.InspectionError, match="Only the two"):
        INSPECT.read_git_blob(ROOT, "unapproved.bin")


@pytest.mark.parametrize("name", ["../escape", "/absolute", "C:/drive", "a/../../escape", "a\\escape", "a/./b"])
def test_zip_paths_fail_closed(tmp_path, name):
    with pytest.raises(INSPECT.InspectionError, match="path"):
        INSPECT.inspect_zip(archive([(name, b"test")]), tmp_path)
    assert list(tmp_path.iterdir()) == []


def test_zip_duplicates_symlinks_and_size_ceilings(tmp_path):
    with pytest.warns(UserWarning, match="Duplicate"):
        duplicate = archive([("same", b"a"), ("same", b"b")])
    with pytest.raises(INSPECT.InspectionError, match="duplicate"):
        INSPECT.inspect_zip(duplicate, tmp_path)
    info = zipfile.ZipInfo("link")
    info.create_system = 3
    info.external_attr = (stat.S_IFLNK | 0o777) << 16
    with pytest.raises(INSPECT.InspectionError, match="symlink"):
        INSPECT.inspect_zip(archive([(info, b"target")]), tmp_path)
    data = archive([("one.txt", b"12345"), ("two.txt", b"67890")])
    for limit in ({"zip_members": 1}, {"zip_member_bytes": 4}, {"zip_total_bytes": 9}):
        with pytest.raises(INSPECT.InspectionError, match="ceiling"):
            INSPECT.inspect_zip(data, tmp_path, limit)
    with pytest.raises(INSPECT.InspectionError, match="ratio"):
        INSPECT.inspect_zip(archive([("repeat", b"a" * 10000)]), tmp_path, {"zip_compression_ratio": 2})


def test_zip_crc_failure_is_not_a_pass(tmp_path):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as target:
        target.writestr("content.txt", b"unique original payload")
    corrupt = stream.getvalue().replace(b"unique original payload", b"unique modified payload")
    with pytest.raises(zipfile.BadZipFile, match="CRC"):
        INSPECT.inspect_zip(corrupt, tmp_path)


def test_zip_inventory_comparison_and_redacted_candidates(tmp_path):
    (tmp_path / "same.txt").write_bytes(b"same")
    (tmp_path / "changed.txt").write_bytes(b"current")
    candidate = "ghp_" + "x" * 36
    data = archive([("package/same.txt", b"same"), ("package/changed.txt", b"old"),
                    ("package/extra.txt", ("line one\n" + candidate).encode())])
    result = INSPECT.inspect_zip(data, tmp_path)
    assert result["comparison_counts"] == {"identical": 1, "changed": 1, "unmatched": 1}
    assert result["members"][2]["credential_candidates"] == [{"type": "github_token", "line": 2, "count": 1}]
    assert candidate not in json.dumps(result)
    assert sorted(p.name for p in tmp_path.iterdir()) == ["changed.txt", "same.txt"]


def test_png_dimensions_crc_and_redacted_metadata():
    candidate = "sk-" + "Q" * 30
    result = INSPECT.inspect_png(png(chunk(b"tEXt", b"Comment\0" + candidate.encode())))
    assert result["image"]["width"] == result["image"]["height"] == 1
    assert result["text_metadata"][0]["credential_candidates"][0]["type"] == "api_key"
    assert candidate not in json.dumps(result)
    corrupt = bytearray(png())
    corrupt[29] ^= 1
    with pytest.raises(INSPECT.InspectionError, match="CRC"):
        INSPECT.inspect_png(bytes(corrupt))
    with pytest.raises(INSPECT.InspectionError, match="trailing"):
        INSPECT.inspect_png(png() + b"extra")


def test_png_compressed_metadata_is_bounded():
    with pytest.raises(INSPECT.InspectionError, match="ceiling"):
        INSPECT.bounded_inflate(zlib.compress(b"a" * 1000), 10)
    with pytest.raises(INSPECT.InspectionError, match="truncated or trailing"):
        INSPECT.bounded_inflate(zlib.compress(b"one") + b"extra", 100)
    result = INSPECT.inspect_png(png(chunk(b"zTXt", b"Comment\0\0" + zlib.compress(b"original note"))))
    assert result["text_metadata"][0]["text_characters"] == 13


def test_failed_read_records_failure_and_existing_output_is_rejected(tmp_path, monkeypatch):
    def unavailable(*_):
        raise INSPECT.InspectionError("Pinned object unavailable")
    monkeypatch.setattr(INSPECT, "read_git_blob", unavailable)
    output = tmp_path / "fresh"
    result = INSPECT.run(tmp_path, output)
    assert result["status"] == "failed"
    assert result["publication_clearance"] is False
    assert json.loads((output / "REPORT.json").read_text())["failure"]["type"] == "InspectionError"
    with pytest.raises(FileExistsError):
        INSPECT.run(tmp_path, output)


def test_zip_encryption_and_other_project_tree_stop_before_content_reads(tmp_path, monkeypatch):
    info = zipfile.ZipInfo("secret.txt")
    info.flag_bits = 1
    with pytest.raises(INSPECT.InspectionError, match="Encrypted"):
        INSPECT.validated_member_name(info)
    data = archive([("package/current.txt", b"allowed"),
                    ("package/Boundary-Entangling-Susceptibility/README.md", b"must not read")])
    def reject_read(*args, **kwargs):
        pytest.fail("No member content may be read after a separate-project tree is found")
    monkeypatch.setattr(zipfile.ZipFile, "open", reject_read)
    with pytest.raises(INSPECT.InspectionError, match="prohibited-project subtree"):
        INSPECT.inspect_zip(data, tmp_path)
