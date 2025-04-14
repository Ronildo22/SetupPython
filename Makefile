install:
	@poetry install

format:
	@poetry run black .
	@poetry run isort .

test:
	@pytest -v

sec:
	@pip-audit