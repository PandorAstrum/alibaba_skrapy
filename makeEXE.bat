@ECHO OFF
REM Runs both my project scripts

ECHO Running pyinstaller
python -m PyInstaller --workpath localDump\build --distpath dist Alibaba_Scrapper.spec
ECHO Finished
PAUSE