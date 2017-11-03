PYTHON?=python3

build-docker:

# push-docker: build-docker
# 	docker push joommf/joommf
#
# build-dists:
# 	rm -rf dist/
# 	$(PYTHON) setup.py sdist
# 	$(PYTHON) setup.py bdist_wheel
#
# release: build-dists
# 	twine upload dist/*

test:
	pwd
	ls -l
	oommf +version

	$(PYTHON) -c "import oommfodt as m; m.test()"
	$(PYTHON) -c "import joommfutil as m; m.test()"
	$(PYTHON) -c "import discretisedfield as d; import sys; sys.exit(d.test())"
	$(PYTHON) -c "import micromagneticmodel as m; m.test()"
	$(PYTHON) -c "import oommfc as m; m.test()"
	$(PYTHON) -c "import joommf"


travis-build:
	make build-docker
	docker run -e ci_env -ti -d --name testcontainer joommftestimage
	docker exec testcontainer make test
	docker exec testcontainer pwd
	docker exec testcontainer ls -l
	docker stop testcontainer
	docker rm testcontainer
