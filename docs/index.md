# DataFun Toolkit

The **DataFun Toolkit** provides small, privacy-safe utility helpers for data analytics coursework and professional Python projects.

This package is designed to be:

- Imported, not modified
- Safe to log and share
- Consistent across operating systems

It supports common needs such as:

- Finding the project root reliably
- Sanitizing file paths for logs
- Detecting runtime environment details (OS, shell, Python)
- Emitting standardized log headers

## Who This Is For

- Students learning Python for data analytics
- Instructors grading and debugging student work
- Analytics projects that need lightweight diagnostics
- CI / GitHub Actions environments

This toolkit intentionally avoids:

- Heavy dependencies
- Framework assumptions
- User-specific identifiers

## Design Principles

- CI-friendly: behaves the same locally and in GitHub Actions
- Privacy-safe: avoids usernames, hostnames, and absolute home paths
- Teaching-first: clear structure, readable output, predictable behavior
- Industry-legible: follows standard Python logging and packaging practices

## Installation

pip install datafun-toolkit

Or with uv:

    uv add datafun-toolkit
    uv sync

Once installed, import the functions by module (see api.md).

## Documentation

- API Reference (api.md)
- Examples (examples.md)
- Troubleshooting (troubleshooting.md)
