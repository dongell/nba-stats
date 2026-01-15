# NBA Stats

A Python project for ranking NBA teams by their statistics.

## Project Structure

```
nba-stats/
├── src/
│   └── nba_stats/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_hello.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation

Install the package in development mode:

```bash
pip install -e .
```

## Usage

After installation, you can run the application using the command:

```bash
nba-stats
```

Or run directly as a Python module:

```bash
python -m nba_stats.main
```

Or run the module directly:

```bash
python src/nba_stats/main.py
```

## Development

### Running Tests

Run tests using unittest:

```bash
python -m unittest discover -v
```

Or with pytest (if installed):

```bash
pytest
```

### Syntax Check

Compile (syntax-check) the code:

```bash
python -m py_compile src/nba_stats/main.py
```

## Requirements

- Python >= 3.13
