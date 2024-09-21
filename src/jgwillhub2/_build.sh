rm -rf build dist
rm -rf jgwillhub/jgwillhub.egg-info
rm -rf *.egg-info
python setup.py sdist bdist_wheel
