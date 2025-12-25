@echo off
cd /d "%~dp0"
wsl.exe -d Ubuntu-22.04 -- bash -lc "python bot.py"
pause