##  Metadata for package
#
# @file		    metadata.py
# @author	    Tobias Ecklebe development.ecklebe@outlook.de
# @date		    15.06.2018
# @version	    0.2.0
# @note		    This file includes all used meta data used in the package
# 
# @pre          See description in file: main.py 
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment. 
#
# @copyright    Copyright (C) 2018  Tobias Ecklebe

from EmptyPythonProject.version import __version__


## Documentation for a class that handles values of the git repository where we work on
class GitRepository:
    """
    Class that stores information about the git repository sites used by this project
    """

    repository_name = "EmptyPythonProject"
    """
    The name of the repository
    """

    gitlab_owner = "open-source/python"
    """
    The project's owner's username on Gitlab
    """

    gitlab_site_url = "https://gitlab.ecklebe.de/"
    """
    The address of the Gitlab instance
    """

    gitlab_url = gitlab_site_url + gitlab_owner + "/" + repository_name
    """
    The Gitlab Project URL
    """

## Documentation for a class that handles general information over the efos package
class General:
    """
    Class that stores general information about a project
    """

    project_description = "This project containes the most things to start programming in python with an new project. To do this fork or clone this repo to your local computer and start editing."
    """
    A short description of the project
    """

    version_number = __version__
    """
    The current version of the program.
    """

    author_names = "Tobias Ecklebe"
    """
    The name(s) of the project author(s)
    """

    author_emails = "development.ecklebe@outlook.de"
    """
    The email address(es) of the project author(s)
    """

    license_type = "None"
    """
    The project's license type
    """

    project_name = 'EmptyPythonProject'
    """
    The name of the project
    """

    download_master_zip = GitRepository.gitlab_url + "/repository/archive.zip?ref=master"
    """
    A URL linking to the current source zip file of the master branch.
    """

## Documentation for a class that handles values for pypi if we want to use this in future
class Variables:
    """
    Variables used for distributing with setuptools
    """

    classifiers = [

        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
    ]
    """
    The list trove classifiers applicable to this project
    """

    install_requires = ["pyinstaller", "pylibcklb<=1.4"]
    """
    Python dependencies
    """

    dependency_links =  [] #['https://github.com/Ecklebe/pylibcklb/tarball/master#egg=pylibcklb'] #old way if the package is not on pypi.org

    extras_require = {}
    """
    Optional dependencies
    """

    name = 'EmptyPythonProject'
    """
    The name of the project
    """

    version = General.version_number
    """
    The version of the project
    """

    description = General.project_description
    """
    The short description of the project
    """

    url = GitRepository.gitlab_url
    """
    A URL linking to the home page of the project, in this case a
    self-hosted Gitlab page
    """

    download_url = General.download_master_zip
    """
    A link to the current source zip of the project
    """

    author = General.author_names
    """
    The author(s) of this project
    """

    author_email = General.author_emails
    """
    The email adress(es) of the author(s)
    """

    license = General.license_type
    """
    The License used in this project
    """
