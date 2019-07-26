from setuptools import setup


def readlist(filename):
    rows = open(filename).read().split('\n')
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


setup(
    long_description=open('README.md').read(),
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
