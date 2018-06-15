## Main file for EmptyPythonProject
#
# @file		    main.py
# @author	    author name
# @date		    08.07.2017
# @version	    0.0.1
# @note		    This file includes the main function code for the application.
# 
# @pre          The programm was developed with python 3.5 and the following modules. An installation is possible over the installtaion batch script or via:
#               - pyinstaller:  python -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip --upgrade
#
# @bug          No bugs at the moment.
#
# @note 		Some ideas comes from https://github.com/namboy94/comunio-manager/
#
# @warning      No warnings at the moment. 
#
# @copyright    Unknown at this stage of implemantation.
#

import sys
import argparse
from typing import Dict
from argparse import Namespace
	
# Parses the command line aruments
def parse_arguments() -> Namespace:

    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action="store_true",
                        help="Starts the program in GUI mode")
    return parser.parse_args()

# Starts the Program by analyzing the given command line parameters and acting accordingly
def main() -> None:
    try:

        args = parse_arguments()

        handle_gui(vars(args)) if args.gui else handle_cli(vars(args))

    except Exception as e:
        raise e

# Handles the GUI initialization of the program
# @param args the arguments passed by argparse
# @return none
def handle_gui(args: Dict[str, object]) -> None:
    sys.exit(print('Hello World for gui'))

# Handles the behavious of the CLI of the program
# @param args  the previously parsed console arguments
def handle_cli(args: Dict[str, object]) -> None:
	sys.exit(print('Hello World for cli'))

if __name__ == "__main__":
    if sys.platform == "win32" and len(sys.argv) == 1:  # Automatically start in GUI mode when using windows,
        sys.argv.append("-g")                           # but only if no arguments were passed
    main()