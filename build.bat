@echo off
REM Simple build script for Windows users
if not exist build mkdir build
cd build
cmake -G "Unix Makefiles" ..
cmake --build .
cd ..
