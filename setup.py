from setuptools import setup


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as f:
        return f.read()


def readlist(filename):
    rows = read(filename).split('\n')
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


setup(
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    download_url='https://github.com/nnsnodnb/django-ios-storekit/tarball/master',
    include_package_data=True,
    package_data={
        '': [
                'README.rst',
                'requirements.txt',
                'requirements-test.txt'
            ]
    },
    install_requires=readlist('requirements.txt'),
    test_suite='runtests.run_tests',
    tests_require=readlist('requirements-test.txt')
)
