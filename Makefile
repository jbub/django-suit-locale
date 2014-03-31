.PHONY: sdist wheel upload

release: sdist wheel upload

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

upload:
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel upload -r pypi

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info