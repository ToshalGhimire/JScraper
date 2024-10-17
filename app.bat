@ECHO OFF
set cmd=%1


set appName=<app_name>
:: ex sitemanager

set project=<project_name>
:: ex fsbattleleague

set containerName=%project%-%appName%
::pip install requirements.txt

IF %cmd%==build (
    ::Running pyinstaller to create the execuatable
    ECHO Building %appName%
    docker build -t gcr.io/%project%/%appName% .
    ECHO Build Succesful
    )

IF %cmd%==run (
    ::Installing app in services
    ECHO running %appName%...
    docker run --restart=always -d -p 5000:5000 --name %containerName% gcr.io/%project%/%appName%:latest
    )

IF %cmd%==stop (
    ::starting app 
    ECHO Stoping sitemanager-container...
    docker container stop %containerName%
    ECHO Stopped sitemanager-container
    )


IF %cmd%==deploy (
    ::starting app 
    ECHO deploying %appName% to Google's container registry...
    deploy.bat
    ECHO Finished deploying %appName%  
    )


