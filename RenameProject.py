__author__="Tobias Ecklebe"

import os
import fileinput
import sys

def Rename(RootDir, ProjectName, Name2Replace):
    for subdir, dirs, files in os.walk(RootDir):
        for filename in files:
            if not filename.endswith('exe') and not filename.startswith('RenameProject') and not '.git' in subdir and not 'build' in subdir and not 'html' in subdir and not 'pycache' in subdir:
                print(subdir + '\\' + filename)
                for line in fileinput.input(subdir + '/' +filename, inplace=1):         
                    if Name2Replace in line:
                        line= line.replace(Name2Replace,ProjectName)
                    sys.stdout.write(line)   

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Missing name")
        sys.exit(1)
    
    ProjectName = sys.argv[1]
    Name2Replace = sys.argv[2]
    RootDir = os.getcwd()              

    print(Name2Replace)
    Rename(RootDir, ProjectName, Name2Replace)
            
if __name__ == '__main__':
    main()