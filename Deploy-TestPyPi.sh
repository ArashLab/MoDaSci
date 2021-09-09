REPO='rodasci'

set -x 
rm -rf build dist ${REPO}.egg-info/ ${REPO}.egg-info
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*

sleep 60
python3 -m pip install -U --index-url https://test.pypi.org/simple/ ${REPO}