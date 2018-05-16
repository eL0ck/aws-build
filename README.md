# AWS CODE BUILD DEMO

This package demonstrates how to build a python package and upload it to Pypi for users to install via `pip install yoyo`


## TODO:  The following build steps are required

1. Install dependencies
```
pip install -r requirements.txt
pip install -r requirements_build.txt
```
2. Test: `pytest`
3. Lint: `flake8 --ignore=E501`
4. Package: `python setup.py sdist bdist_wheel`
5. Deploy to PyPi (Test):
```
twine upload --repository-url https://test.pypi.org/legacy/ \
    -u ${USERNAME} \
    -p ${PASSWORD} \
    dist/*
```

The package should then be installable via the command (available now):

`pip install --index-url https://testpypi.python.org/pypi yoyo`

and testable with the CLI app: `yoyo --help`

Manage the project here:

[PyPI Test](https://test.pypi.org/manage/projects/)
