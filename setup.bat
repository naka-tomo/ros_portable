@echo off
set DIR=%~dp0\commands\
set PYTHONPATH=%~dp0/python_package;;%PYTHONPATH%
set PATH="%DIR%";%PATH%

set ROS_MASTER_URI=http://127.0.0.1:11311
set ROS_HOSTNAME=127.0.0.1