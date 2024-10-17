Python Application template

A project in GCP will need to be setup first. Used for storing and running container 

Fill out items in "<>" in app.bat, deploy.bat and metadata.json

Create a new python environment with conda

- conda create --name <app name> python=3.9.7

## GCP Container Regisry and Cloud Run Setup

- Install gcloud CLI

- Run `gcloud auth login` to authenticate user

- Create a project in cloud run or firebase

- Go into service account in IAM & admin dashboard

- Find account for "App Engine default service account"

- Generate new key file and save the file in project directory

- Grab username and api key file path and run this command
    `gcloud auth activate-service-account <ACCOUNT> --key-file=<KEY FILE PATH>`

- Configure docker by running `gcloud auth configure-docker`

- You are ready for `app deploy` command