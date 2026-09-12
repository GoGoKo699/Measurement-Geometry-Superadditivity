# Historical-object follow-up

This bounded follow-up starts from license-adoption commit `857d173c79140b5c2643c1a7d16b4a2321ed8dd4`. It addresses the two incomplete binary transfers recorded in [HISTORY_REVIEW.md](HISTORY_REVIEW.md). The repository remains private, and the earlier no-merge, no-history-rewrite and no-publication boundaries remain in force.

The added [inspection helper](inspect_historical_objects.py) reads only the two recorded Git object IDs. The [dedicated workflow](../.github/workflows/historical-object-review.yml) checks out complete history with read-only repository permission and runs that helper. It neither executes archived code nor runs numerical science. Checkout credentials are not persisted. Its Actions are pinned to the exact revisions observed in successful reader run `34685435836`.

The workflow retains an access-controlled review artifact containing the exact two objects and a structured inspection report for seven days. The word “private” in prose is not an access control; the repository's current private visibility supplies that boundary. No deployment or release action is present.

Before a successful complete transfer and content inspection, both objects remain unverified. A configured workflow, correct object size or successful ZIP CRC check alone is not distribution clearance. Actual run IDs, object identities and inspection conclusions will be recorded after execution. The historical report and licensing adoption records remain unchanged.

To repeat in a complete authenticated checkout, use a new output directory:

```bash
python3 publication/inspect_historical_objects.py --output build/historical-object-review
```

The helper requires only the Python standard library and Git. Root project files, canonical data, certificates, substantive numerical verifiers, figure exports and earlier audit outputs are not replaced. The separate [integration review](INTEGRATION_REVIEW.md) describes how the existing corrections relate to the reader and licensing work; it is not permission to merge those branches.
