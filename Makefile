install:
	@poetry install

lint:
	@poetry run black .
	@poetry run isort .

format:
	@poetry run prospector .

test:
	@pytest -v

sec:
	@pip-audit