default:
	pip install -e ../bfmplot --no-binary :all:

install:
	pip install ../bfmplot

pypi:
	rm dist/*
	python setup.py sdist
	twine upload dist/*
