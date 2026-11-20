# Installation

1. Download/extract the ZIP.
2. Go to `https://github.com/danishirfan21/danishirfan21` (public profile repository).
3. Upload `README.md`, `assets/`, `scripts/update_stats.py` and `.github/workflows/telemetry.yml` while preserving folder paths. Keep existing repository files you still need.
4. On GitHub, go to **Actions → Refresh public GitHub telemetry → Run workflow**.
5. The Action generates `assets/telemetry.svg` using GitHub's API and commits it back to the repository. If pushing fails, enable **Settings → Actions → General → Workflow permissions → Read and write permissions**.
6. View `https://github.com/danishirfan21`.

## What is real, and what isn't
- `assets/signal.gif` is a pre-rendered animation and works in GitHub's README image renderer. Its text and effects are fixed.
- The three wide destination images are ordinary linked SVG images. They are clickable links, not JavaScript buttons.
- `assets/telemetry.svg` is generated from your public GitHub account. The metrics are not invented. A dash means an API fetch was unavailable.
- PR figures use GitHub Search (`author:`) and include public PRs across repositories, as indexed by GitHub.
- Stars earned are summed across your owned, non-fork public repositories; this differs from stars you've given.
- Metrics refresh daily (not continuously) and can lag due to API indexing or Actions scheduling.
- The source `.github` workflow must remain on the repository default branch for scheduled runs.
- The hero animation and cards are self-contained assets and don't rely on third-party stat badge services.

## Customization
- Edit `README.md` for text/link changes.
- Change the words in `scripts/build_art.py`, then rerun it with Pillow installed (`pip install pillow`) to regenerate the GIF and image cards.
- Update `scripts/update_stats.py` for different metric choices.
