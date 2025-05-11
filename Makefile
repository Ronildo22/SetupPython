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

cc:
	@poetry run radon cc -s src

mi:
	@poetry run radon mi -s src

raw:
	@poetry run radon raw -s src

hal:
	@poetry run radon hal src