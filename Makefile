.PHONY: test

test:
	python3 -m pytest -xv --flake8 --pylint --mypy tests/grepper_test.py
