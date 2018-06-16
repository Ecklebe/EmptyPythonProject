@echo off
rem Author Tobias Ecklebe
echo Script to rename the folders and files to the correct project name

cd /d %~dp0

IF "%1"=="" ( set /p ProjectName="Filtername :" 
) ELSE ( set ProjectName=%1)

call python.exe RenameProject.py "%ProjectName%" "EmptyPythonProject"

MOVE EmptyPythonProject %ProjectName%
REM del /Q RenameProject.py


if "%NO_PAUSE%" NEQ "" goto skip_pause
pause
:skip_pause