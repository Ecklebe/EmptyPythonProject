@echo off
rem tobias.ecklebe@outlook.de

echo Create executable with documentation this require DOXYGEN_ROOT as enviormental variable 
echo -----------
echo.

cd ../documentation/
call run_doxygen.bat
cd ../deploy
pyinstaller.exe Installer.spec