@ECHO OFF
REM Runs both my project scripts

ECHO Running pyinstaller to generate spec
pyi-makespec Alibaba_Scrapper ui.py
ECHO Finished making spec file
PAUSE