
all: build install

build:
	python setup.py build
	python setup.py build_ext --inplace

install: build
	python setup.py install

clean:
	python setup.py clean
	rm -Rf build
	rm -Rf doc/.build

