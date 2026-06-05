# How to contribute

## Setup

This project uses [`mise`](https://mise.jdx.dev/) to manage tools (Python,
[`uv`](https://docs.astral.sh/uv/), [`ruff`](https://docs.astral.sh/ruff/),
[`hk`](https://hk.jdx.dev/)) and tasks, `uv` for dependencies, and `ruff` for
linting and formatting.

```bash
mise install        # provision the pinned tools
mise run install    # uv sync -> .venv
mise run setup-hk   # install git hooks (ruff runs via hk)
```

If you'd rather not use `mise`, install `uv` yourself and run `uv sync`.

## Common tasks

```bash
mise run test    # uv run pytest
mise run lint    # ruff check .
mise run fmt     # ruff format .
mise run check   # ruff check + ruff format --check
mise run docs    # mkdocs serve
mise run build   # uv build
```

## Before submitting

1. Add your changes (and tests for new behaviour).
2. Update the docs if you changed something significant.
3. Run `mise run fmt`, then `mise run check`.
4. Run `mise run test`.

The `hk` pre-commit hook runs `ruff` automatically on commit.

## Other help

You can contribute by spreading the word about this library, writing a short
article on how you use it, or sharing your best practices with us.
