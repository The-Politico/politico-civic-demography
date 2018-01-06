test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd demography/staticapp/

database:
	dropdb demography --if-exists
	createdb demography
