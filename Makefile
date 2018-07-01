PROJECT=joommf
IPYNBPATH=docs/ipynb/*.ipynb
CODECOVTOKEN=b0beeda5-9b5d-4418-bad5-09f209fc5e88
PYTHON?=python3

test:
	$(PYTHON) -m pytest

test-test:
	$(PYTHON) -c "import sys; import $(PROJECT); sys.exit($(PROJECT).test())"

test-coverage:
	$(PYTHON) -m pytest --cov=$(PROJECT) --cov-config .coveragerc

test-docs:
	$(PYTHON) -m pytest --doctest-modules --ignore=$(PROJECT)/tests $(PROJECT)

test-ipynb:
	$(PYTHON) -m pytest --nbval $(IPYNBPATH)

test-joommf:
	$(PYTHON) -c "import sys; import joommfutil as ju; sys.exit(ju.test())"
	$(PYTHON) -c "import sys; import discretisedfield as df; sys.exit(df.test())"
	$(PYTHON) -c "import sys; import oommfodt as oo; sys.exit(oo.test())"
	$(PYTHON) -c "import sys; import micromagneticmodel as mm; sys.exit(mm.test())"
	$(PYTHON) -c "import sys; import oommfc as oc; sys.exit(oc.test())"

# In test-all target test-docs is disabled because this package has no docs.
test-all: test-test test-coverage test-ipynb test-joommf

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
