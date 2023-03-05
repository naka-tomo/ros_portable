@echo off
set DIR=%~dp0
set PYTHONPATH=%DIR%;%DIR%..;%PYTHONPATH%
set PATH="%DIR%";%PATH%

set ROS_MASTER_URI=http://127.0.0.1:11311
set ROS_HOSTNAME=127.0.0.1