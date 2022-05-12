.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: mdseo docs

mdseo: $(SRC)
	nbdev_build_lib
	touch mdseo

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

conda_release:
	fastrelease_conda_package

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
    
nbdev-all:
	nbdev_build_lib
	nbdev_clean_nbs
	nbdev_test_nbs
	nbdev_build_docs