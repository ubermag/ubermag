PYTHON?=python3

build-docker:
	rm -rf oommfc/
	git clone https://github.com/joommf/oommfc.git
	docker build -t joommf/joommf .

push-docker: build-docker
	docker push joommf/joommf

build-dists:
	rm -rf dist/
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

release: build-dists
	twine upload dist/*
