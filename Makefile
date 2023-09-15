mypy:
	mypy src

pep8:
	flake8 src

pre-commit:
	pre-commit run --all-files
