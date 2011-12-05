#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='test-ci',
    url='http://github.com/mmikulicic/test-ci',
    license='GPL',
    version='2.0.1',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
    ],
    scripts=['scripts/testciscript.py']
)

