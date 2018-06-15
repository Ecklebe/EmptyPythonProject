##  Builder for Package
#
# @file		    builder.py
# @author	    Tobias Ecklebe development.ecklebe@outlook.de
# @date		    15.06.2018
# @version	    0.1.0
# @note		    This file calls the builder function from pylibcklb to build the executable.
# 
# @pre          Folder with name "deploy" and main.spec in the same folder as this script. The main.spec is the specification file for pyinstaller
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment. 
#
# @copyright    Copyright (C) 2018  Tobias Ecklebe

from EmptyPythonProject.metadata import General, Variables
from pylibcklb.installer.pyinstaller import build

# While execution of this file with python the imported function will be executed. See for requierments @pre
if __name__ == "__main__":
    build(Variables.name, General.version_number)