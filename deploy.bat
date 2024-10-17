@ECHO OFF
set cmd=%1

@ECHO OFF
for /f "tokens=1,2" %%i in (./metadata.json) do (   
    set string=%%i
)

set string=%string:{=%
set string=%string:}=%

for /F "tokens=1,2,3,4,5,6 delims=, " %%a in ("%string%") do (
    set MajorString=%%a
    set MinorString=%%b
    set RevisionString=%%c
    set BuildTagString=%%d
    set AppNameString=%%e
    set DockerImage=%%f
)



for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%MajorString%") do (set MajorNumber=%%b)
for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%MinorString%") do (set MinorNumber=%%b)
for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%RevisionString%") do (set RevisionNumber=%%b)
for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%BuildTagString%") do (set BuildTag=%%b)
for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%AppNameString%") do (set AppName=%%b)
for /F "tokens=1,2,3,4,5 delims=:" %%a in ("%DockerImage%") do (set DockerImage=%%b)


set BuildTag=%BuildTag:"=%
set AppName=%AppName:"=%
set DockerImage=%DockerImage:"=%

set Version=v%MajorNumber%.%MinorNumber%.%RevisionNumber%
set TagName=%AppName%_%Version%

echo %AppName% %Version% %BuildTag% 
:: Use this for when you connect deploy to cloud run: 
:: set SERVICE_ID=svc-site-manager

set GOOGLE_PROJECT_ID=<project_name>
:: ex fsbattleleague
set IMAGE_NAME=gcr.io/%GOOGLE_PROJECT_ID%/%DockerImage%


call docker build -t %IMAGE_NAME% .

echo Saving build to git as tag "%TagName%"  
call git tag "%TagName%" -m "Tag of build %TagName%"
call git push origin "%TagName%"

call docker tag %IMAGE_NAME% %IMAGE_NAME%:%Version%

call docker push %IMAGE_NAME%:%Version%

echo Incrementing build number  
call node generate-buildno.js