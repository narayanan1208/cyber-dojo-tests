.PHONY: test lint format all

PYTHON=python3

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m flake8 hiker.py test_*.py

format:
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

all:
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) test