@echo off
rem tobias.ecklebe@outlook.de

echo Create doxygen based documentation this requires DOXYGEN_ROOT as enviormental variable 
echo -----------
echo.

IF "%DOXYGEN_ROOT%" == "" GOTO NOPATH
:YESPATH
@ECHO Create the documentation
cd config
%DOXYGEN_ROOT%\bin\doxygen.exe Doxyfile
cd ..
GOTO END
:NOPATH
@ECHO The DOXYGEN_ROOT environment variable was NOT detected.
GOTO END
:END
