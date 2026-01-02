# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

### Added

- (placeholder) Notes for the next release.

---

## [0.9.0] - 2026-01-02

### Added

- Initial public release
- Docs site scaffolding (MkDocs Material, i18n)
- Testing: Ruff lint; pre-commit hooks
- Packaging
- Privacy-first design
- CI/CD: GitHub Actions for checks, docs, and automated releases

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking schema/OpenAPI changes
  - **MINOR** – backward-compatible additions
  - **PATCH** – clarifications, docs, tooling
- Versions are driven by git tags via `setuptools_scm`. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

[Unreleased]: https://github.com/denisecase/datafun-toolkit/compare/v0.9.0...HEAD
[0.9.0]: https://github.com/denisecase/datafun-toolkit/releases/tag/v0.9.0
