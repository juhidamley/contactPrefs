@echo off
cd /d "%~dp0"
call "%USERPROFILE%\AppData\Local\anaconda3\Scripts\activate.bat" base
python contactPrefsNaming.py
