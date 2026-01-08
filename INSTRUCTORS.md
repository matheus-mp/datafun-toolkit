# INSTRUCTORS.md

This file documents **teaching intent, operational scope, and maintenance guidance**.

## Purpose

This repository provides **infrastructure** for Data Analytics Python projects:

- Privacy-safe diagnostics
- Path normalization
- Standardized logging
- CI/CD validation
- Versioned documentation
- PyPI distribution

It exists to:

- Reduce debugging time
- Normalize environments
- Make execution visible and auditable
- Model professional Python practices

## Scope

This repository **includes additional features** that many project repos will NOT need.

### INCLUDED HERE

- PyPI packaging and release workflow
- Dynamic versioning (SCM tags)
- Versioned documentation (Mike + MkDocs)
- CI enforcing formatting, linting, typing, and tests
- Pre-commit quality gates
- Typed package marker (`py.typed`)

## Adapting

When adapting this repository, start here:

### 1. pyproject.toml

Defines:

- Python version
- Dependencies
- Tool configuration (ruff, pyright, deptry, bandit)
- Packaging metadata

This is the single source of truth for a Python project.

### 2. .pre-commit-config.yaml

Defines:

- Local quality gates
- What CI enforces
- What checks must pass before submission

We want failures to first fail in pre-commit.
If pre-commit passes, the GitHub actions CD/CD should pass.

### 3. .github/workflows/

GitHub actions workflows:

- `ci-python-mkdocs.yml` - validation only (should check but not mutate code)
- `deploy-mkdocs.yml` - GitHub Pages build (provides the optional project documentation)
- `release.yml` - PyPI and versioned docs (advanced)

## Design Notes

### Logging is introduced early

- Makes execution observable
- Helps illustrate program flow
- Enables verification of execution
- Builds professional habits

### Paths are sanitized

- Prevents leaking home directories
- Makes logs shareable
- Avoids operating system assumptions

### Diagnostics provided

- Shell differences explain many issues
- OS/version visibility helps with debugging
- Uses heuristics only (privacy-safe)

## Signals and Interpretation

Useful indicators.

### Missing log header

Usually means:

- Logger not initialized
- Function not called
- Script not executed
- Solution: Call necessary functions - see example below

```python
# imports at the top of the file
from datafun_toolkit.logger import get_logger, log_header

# just once, early in program execution (e.g. beginning of main())
logger = get_logger("datafun-project", level="INFO")
log_header(logger, "datafun-project")
```

### CI fails but local run works

Often indicates:

- Formatting has not been normalized
- Line endings differ
- Either pre-commit has not been run or pre-commit checks do not all pass.
- Solution: run the following commands and fix issues until all checks pass.

```shell
git add -A
uv run pre-commit run --all-files
git add -A
```

### Paths look absolute

Indicates:

- Paths not sanitized.
- Provided helpers are not being called.
- Hard-coded paths used
- Solution: import the functions, initialize the logger, and use the functions provided.

```python
# imports at the top of the file
from pathlib import Path
from datafun_toolkit.logger import get_logger, log_header
from datafun_toolkit.paths import find_project_root, safe_relpath_str

# just once, early in program execution (e.g. beginning of main())
logger = get_logger("datafun-project", level="INFO")
log_header(logger, "datafun-project")

# as needed to log paths
root: Path = find_project_root()
data_dir: str = safe_relpath_str(root / "data", root)
notebooks_dir: str = safe_relpath_str(root / "notebooks", root)

logger.info(f"Root: {root}")
logger.info(f"Data: {data_dir}")
logger.info(f"Notebooks: {notebooks_dir}")
```

## Maintenance Notes

### Version bumps

- Python version changes affect CI, tooling, and docs
- Update pyproject.toml first

### Tool churn

- Ruff, Pyright, and uv evolve quickly
- Prefer pinning major versions

### Windows considerations

- Line endings
- Shell detection
- Path separators

These are expected and handled by design.
