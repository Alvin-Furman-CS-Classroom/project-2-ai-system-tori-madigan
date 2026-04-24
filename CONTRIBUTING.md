# Contributing

This repository follows a short GitHub workflow so checkpoints stay reviewable and history stays readable.

## Branches and pull requests

1. Create a **feature branch** from `main` for substantive work (e.g. `module-5-fallback-metrics`, `fix-m4-validation`).
2. Open a **pull request** into `main` with a clear title and description. Use the PR template so reviewers see what changed and how it was tested.
3. Prefer **small, focused PRs** over one large batch commit.
4. Request review from a teammate when the change touches shared modules or the pipeline.

## Commit messages

Write messages that state **what** changed and **why** when it is not obvious, for example:

- `Module 5: include constraint count and density in fallback difficulty score`
- `Tests: cover Module 5 historical scoring and invalid baseline fallback`

Avoid vague titles such as `updates` or `fix stuff`.

## Collaboration

- Resolve merge conflicts on your branch before requesting review.
- Use GitHub Classroom **feedback** branches or instructor feedback as needed; merge `main` regularly to reduce drift.

## Tests

Run the relevant tests before opening a PR:

```bash
py -3 -m pip install -r requirements.txt
py -3 -m pytest -q unit_tests/test_module5_complexity_analysis.py integration_tests/test_module1_to_module5.py
```

Adjust paths when your change affects other modules.
