# Requirements

## System Requirements

- Python >= 3.13
- pip (Python package installer)

## Python Dependencies

The project uses the following Python packages (defined in `pyproject.toml`):

### Build Dependencies
- setuptools >= 61.0
- wheel

### Development Dependencies
- unittest (built-in)
- pytest (optional, for alternative test runner)

## Installation Requirements

To install this package in development mode:

```bash
pip install -e .
```

This will install the package in editable mode, allowing you to make changes to the source code without reinstalling.

## Running the Application

After installation, the package provides a command-line entry point:

```bash
nba-stats
```
