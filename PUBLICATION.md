# Publication administration

The scientific repository, reader guides, documentary corrections and licenses are integrated. [Project status](STATUS.md) describes the completed scientific account. This page records distribution decisions for the maintainer; it is not part of the learning route.

## Current decisions

- Original code uses MIT; original prose, figures and data use CC BY 4.0 where rights exist. Ruge Lin is the confirmed rights holder and citation author. [License scope](LICENSE.md) · [Citation](CITATION.cff) · [Third-party notices](THIRD_PARTY_NOTICES.md)
- The owner has approved retaining the contact email so readers can get in touch. It is displayed with the project contact information and remains in the existing history.
- Historical reports and provenance remain available through the [record index](publication/PROJECT_HISTORY.md). The reader-facing pages present the current result and scope without the preparation chronology.
- Repository visibility is still private and Pages is disabled. This editorial update does not change those settings. The final visibility instruction, including disclosure of retained project/history metadata, remains separate from permission to keep the contact email.

[Machine-readable preparation record](publication/READINESS.json) · [Current reader-status report](publication/reader-status/REPORT.md)

## Before changing visibility

Recheck the intended main commit and actual CI outcomes, then apply the owner's visibility instruction. GitHub's [visibility documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) explains that existing Actions history and logs become visible with a public repository. Removing an item from the reader route does not erase it from Git history. No history rewrite is included in this work.

The GitHub reading pages are the intended repository interface. Public repository visibility does not require Pages, another hosted site, a release tag or an archival DOI. Optional HTML builds remain local artifacts. A manuscript and any later article citation are separate from the completed repository account.

## Maintenance checks

Use `python publication/reader-status/check_reader_status.py` for the current editorial preservation check, followed by the applicable reader checks in [WEBSITE.md](WEBSITE.md). It compares this presentation stage against the integrated commit and validates the historical integration checkpoint without changing its checker or recorded hashes. Earlier preparation, adoption and integration reports retain their own commit scopes in the [record index](publication/PROJECT_HISTORY.md).
