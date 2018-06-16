#!/usr/local/bin/python
# -*- coding: iso-8859-1 -*-

__author__="Tobias Ecklebe"

import os
import fnmatch
import fileinput
import sys
import getopt

argcount = 0

for arg in sys.argv:
    argcount = argcount + 1

print(argcount)

if argcount < 2 or argcount > 3:
    print("Missing name")
    sys.exit(1)
    
ProjectName = sys.argv[1]

RootDir = os.getcwd()              
print(RootDir)

searchExp = sys.argv[2]
            
for subdir, dirs, files in os.walk(RootDir):
    for filename in files:
        if not filename.endswith('exe') and not filename.startswith('RenameProject') and not '.git' in subdir and not 'build' in subdir and not 'html' in subdir and not 'pycache' in subdir:
            print(subdir + '\\' + filename)
            for line in fileinput.input(subdir + '/' +filename, inplace=1):         
                if searchExp in line:
                    line= line#line.replace(searchexp,projectname)
                sys.stdout.write(line)   