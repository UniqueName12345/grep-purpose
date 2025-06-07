@echo off
REM Simple build script for Windows users

REM Detect a suitable CMake generator when none is provided
if not defined generator (
    set "generator=NMake Makefiles"
    where nmake >nul 2>nul
    if errorlevel 1 (
        where mingw32-make >nul 2>nul
        if not errorlevel 1 set "generator=MinGW Makefiles"
    )
)

if not exist build mkdir build
cd build
cmake -G "%generator%" ..
cmake --build .
cd ..
