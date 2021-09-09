REPO='rodasci'

set -x
rm -rf build dist ${REPO}.egg-info/ ${REPO}.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*