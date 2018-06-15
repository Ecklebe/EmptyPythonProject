## Setup file for the Package
#
# @file		    setup.py
# @author	    Tobias Ecklebe development.ecklebe@outlook.de
# @date		    16.05.2018
# @version	    0.1.0
# @note		    This file includes all used meta data used in the package
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment. 
#
# @copyright    Copyright (C) 2018  Tobias Ecklebe 


# imports
import os
from setuptools import setup, find_packages
from EmptyPythonProject.metadata import Variables


# @note Found at: https://gitlab.namibsun.net/namboy94/comunio-manager/blob/master/setup.py
def readme():
    """
    Reads the readme file.

    :return: the readme file as a string
    """
    try:
        # noinspection PyPackageRequirements
        import pypandoc
        with open('README.md') as f:
            # Convert markdown file to rst
            markdown = f.read()
            rst = pypandoc.convert(markdown, 'rst', format='md')
            return rst
    except (OSError, ImportError):
        # If pandoc is not installed, just return the raw markdown text
        with open('README.md') as f:
            return f.read()

exec(open('EmptyPythonProject/version.py').read())

setup(name=Variables.name,
      version=__version__,
      description=Variables.description,
      long_description=readme(),
      classifiers=Variables.classifiers,
      url=Variables.url,
      download_url=Variables.download_url,
      author=Variables.author,
      author_email=Variables.author_email,
      license=Variables.license,
      packages=find_packages(),
      install_requires=Variables.install_requires,
      dependency_links=Variables.dependency_links,
      extras_require=Variables.extras_require,
      test_suite='nose.collector',
      tests_require=['nose'],
      package_data={'': ['CHANGELOG.md']},
      data_files=[('.',['CHANGELOG.md'])],
      include_package_data=True,
      entry_points = {
        #'console_scripts': []},
        'gui_scripts': ['EmptyPythonProject=EmptyPythonProject.main:main']},
      zip_safe=False)
