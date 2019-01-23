.PHONY: lint
lint:
	pipenv run pylint ./src

.PHONY: test
test:
	pipenv run pytest -s --color=yes --cov-report html --cov-report term --cov-report=xml:coverage.xml --cov=src test --cov-fail-under=100 $(MAKECMDGOALS)

.PHONY: ci
ci: lint test

.PHONY: commit
commit:
	git add .
	git commit -am working

.PHONY: revert
revert:
	# git reset --hard
	# git clean -f
	# The above 2 commands are a bit too harsh as they revert our test cases
	git checkout HEAD — src/main/

.PHONY: stash
stash:
	git stash drop 0 2&>/dev/null; git add -A && git stash push

.PHONY: tcr
tcr:
	make test && make commit || make revert

