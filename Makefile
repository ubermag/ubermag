PYTHON?=python3


# install joommf via pip
build-docker-pip:
	docker build -t joommfimage-pip -f Dockerfile .

# install joommf via conda (see https://github.com/joommf/conda-install)

build-docker:
	make build-docker-pip

test:
	pwd
	ls -l
	oommf +version

	$(PYTHON) -c "import sys; import oommfodt as m; sys.exit(m.test())"
	$(PYTHON) -c "import sys; import joommfutil as m; sys.exit(m.test())"
	$(PYTHON) -c "import sys; import discretisedfield as d; import sys; sys.exit(d.test())"
	$(PYTHON) -c "import sys; import micromagneticmodel as m; sys.exit(m.test())"
	$(PYTHON) -c "import sys; import oommfc as m; sys.exit(m.test())"
	$(PYTHON) -c "import sys; import joommf"


travis-build:
	make build-docker
	docker run --rm -e ci_env joommfimage-pip make test
