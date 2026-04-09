.PHONY: help test lint format check clean install

PYTHON := python3
SRC := .
TESTS := test_*.py

help:
	@echo "Available commands:"
	@echo "  make install  -> Install dependencies"
	@echo "  make format   -> Format code (black + isort)"
	@echo "  make lint     -> Run flake8"
	@echo "  make test     -> Run tests with coverage"
	@echo "  make check    -> Run all checks (format + lint + test)"
	@echo "  make clean    -> Remove cache files"
	@echo "  make all      -> Run all commands (format + lint + test)"

install:
	$(PYTHON) -m pip install -r requirements.txt

format:
	$(PYTHON) -m black $(SRC)
	$(PYTHON) -m isort $(SRC)

lint:
	$(PYTHON) -m flake8 $(SRC) ${TESTS}

test:
	$(PYTHON) -m pytest

check:
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) test

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	rm -f .coverage
