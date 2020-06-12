PROJECT=ubermag
IPYNBPATH=docs/ipynb/*.ipynb
CODECOVTOKEN=cdfa6461-04c2-4c85-a292-fd1475eccde8
PYTHON?=python3

test:
	$(PYTHON) -m pytest

test-test:
	$(PYTHON) -c "import sys; import $(PROJECT); sys.exit($(PROJECT).test())"

test-coverage:
	$(PYTHON) -m pytest -v --cov=$(PROJECT) --cov-config .coveragerc

test-docs:
	$(PYTHON) -m pytest -v --doctest-modules --ignore=$(PROJECT)/tests $(PROJECT)

test-ipynb:
	$(PYTHON) -m pytest -v --nbval $(IPYNBPATH)

test-pycodestyle:
	$(PYTHON) -m pycodestyle --filename=*.py .

test-all: test-test test-coverage test-docs test-ipynb test-pycodestyle

upload-coverage: SHELL:=/bin/bash
upload-coverage:
	bash <(curl -s https://codecov.io/bash) -t $(CODECOVTOKEN)

travis-build: SHELL:=/bin/bash
travis-build:
	ci_env=`bash <(curl -s https://codecov.io/env)`
	docker build -f docker/Dockerfile -t dockertestimage .
	docker run -e ci_env -ti -d --name testcontainer dockertestimage
	docker exec testcontainer make test-all
	docker exec testcontainer make upload-coverage
	docker stop testcontainer
	docker rm testcontainer

test-docker:
	docker build -f docker/Dockerfile -t dockertestimage .
	docker run -ti -d --name testcontainer dockertestimage
	docker exec testcontainer find . -name '*.pyc' -delete
	docker exec testcontainer make test-all
	docker stop testcontainer
	docker rm testcontainer

build-dists:
	rm -rf dist/
	$(PYTHON) setup.py sdist bdist_wheel

release: build-dists
	twine upload dist/*
