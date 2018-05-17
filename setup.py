# codeing: utf-8
from setuptools import setup, find_packages


NAME = 'django-ios-storekit'
VERSION = '1.0.2'


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
    name=NAME,
    version=VERSION,
    description='A Django plugin for iOS In-App Purchases.',
    long_description=read('README.rst'),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keyword='django ios in-app-purchases apple',
    author='nnsnodnb',
    author_email='ahr63_gej@me.com',
    url='https://github.com/nnsnodnb/django-ios-storekit',
    download_url='https://github.com/nnsnodnb/django-ios-storekit/tarball/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': [
                'README.rst',
                'requirements.txt',
                'requirements-test.txt'
            ]
    },
    zip_safe=False,
    install_requires=readlist('requirements.txt'),
    test_suite='runtests.run_tests',
    tests_require=readlist('requirements-test.txt')
)
