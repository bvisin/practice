.PHONY: lint
lint:
	pipenv run pylint ./src

.PHONY: test
test:
	pipenv run pytest -s --color=yes --cov-report html --cov-report term --cov=src test --cov-fail-under=100

.PHONY: ci
ci: lint test