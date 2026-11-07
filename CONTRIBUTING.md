# Working on goldreg-R76

goldreg-R76 uses **Git Flow** and **semantic versioning**, as NSDF-Data, goldpan, goldsluice and goldmap do.

## Branches

| Branch | What it is |
|---|---|
| `main` | Released data only. Every commit on it is tagged `vX.Y.Z`. |
| `develop` | The integration branch. All work lands here first. |
| `feature/<name>` | One change, made from `develop`, finished by a pull request into `develop`. |
| `release/X.Y.Z` | Made from `develop` to get a release ready (`CHANGELOG.md`). Finished by a pull request into `main`; the maintainer tags it. |
| `hotfix/X.Y.Z` | An urgent fix made from `main`. Finished by a pull request into `main`, then merged back into `develop`. |

Rules:

- Never commit directly to `main` or `develop`. Make a branch and open a pull request.
- Finish a branch with a **merge commit** (not squash, not rebase). Never force-push.
- Delete a branch only after it is merged, and only one you made.
- Every change gets a line under `[Unreleased]` in `CHANGELOG.md`. A number that results depend on says so.
- Only a `release/*` or `hotfix/*` branch renames `[Unreleased]`.
- `python -m pytest` runs on Linux, Windows and macOS for every pull request; it must pass.
- The maintainer is Anthony Villano (@villaa). An AI agent never merges without the maintainer's explicit go-ahead.

## A record

1. `git switch develop && git pull`, then `git switch -c feature/<name>`.
2. Add or change a table in `run76.toml` (detectors) or `readouts.toml` (readouts). Every record needs `status` and `evidence`; **say where a number comes from and never write a guess as `confirmed`**. A name may be defined only once.
3. `python -m pytest` (needs `pip install goldpan pytest`).
4. A line in `CHANGELOG.md`, a pull request into `develop`.

A record for another analysis (another run, another experiment) belongs in that analysis's own registry, `goldreg-<name>`, not here. To share a detector with another registry, copy its record there and add `copied_from = "goldreg-R76@<commit>"` beside `evidence`.

No raw data, credentials or tokens, ever.
