# AGENTS.md: working in goldreg-R76

Instructions for AI coding agents and human contributors. `CONTRIBUTING.md` has the rules; this adds what an agent must not forget.

- **This is data, not code.** Keep it to TOML records, the README and the test. Nothing from goldpan or goldsluice is copied in, and neither of them may depend on this repository (their tests take a registry folder from an environment variable).
- **Never write a guess as `confirmed`.** A record without `evidence` is refused by the reader. Say where a number comes from: a file, a document, a measurement with its dump names.
- **Do not change a number that results depend on** (`pretrigger_samples`, `sample_period_s`) without the maintainer: outputs made with the old value differ. It is a minor version and a line in `CHANGELOG.md`. goldpan carries presets of the same numbers (`DCRC_RUN76`, `Z7`) only until they are dropped; never "fix" a preset to match, change the registry.
- Work on a `feature/*` branch from `develop`, open a pull request into `develop`, merge commits only, never force-push. **An agent never merges a pull request without the maintainer's go-ahead**, and never pushes a release tag.
- Run `python -m pytest` before asking for review.
- If an AI assistant helped, add a `Co-Authored-By:` trailer to the commit.
