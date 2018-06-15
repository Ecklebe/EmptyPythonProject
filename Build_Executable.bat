@echo off
rem Tobias Ecklebe development.ecklebe@outlook.de

echo Create executable with documentation this require DOXYGEN_ROOT as enviormental variable 
echo ----------------------------------------------------------------------------------------
echo.

rem build documentation
call Build_Documentation.bat

rem build the executable
python builder.py

echo.
ECHO Press any key to exit
PAUSE >NUL
EXIT /B