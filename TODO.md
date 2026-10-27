# Open items

Last updated: 2026-10-27. State: `main` clean, all feature branches merged.

## Licensing
- [ ] Audit figures: `micro-credentials/images/` (Ward-*.png, subject-specifc-*.png) and
      `Introduction-to-ai/docs/images/*`. Do this before claiming CC BY 4.0 for them.
      First step: `find micro-credentials/images Introduction-to-ai/docs/images -type f | sort`
- [ ] Verify the upstream licence of mpitutorial.com (see THIRD_PARTY_NOTICES.md).
- [ ] Datasets section in THIRD_PARTY_NOTICES.md is still marked "TO DOCUMENT".

## Repository hygiene
- [ ] Decide whether to purge the Kaggle CSVs from git history (needs a force-push,
      which breaks existing clones, so plan it as a separate session).
- [ ] Move the local `git-token` file out of the repo (for example to `~/.secrets/`).
      It is ignored via `.git/info/exclude`, `chmod 600`, and was never committed.
