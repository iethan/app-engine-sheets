# Instructions

## Install gcloud

From any folder, insert the following into your terminal:

```curl https://sdk.cloud.google.com | bash```

Follow the instructions to make default zones for your projects.

## Add this app to your local machine

Go to the directory you'd like to add this project and in terminal:

```git clone <name-of-the-git-repo> ```

## Install required libaries to your machine

In terminal: ```pip install google-auth google-auth-httplib2 google-api-python-client```


## Adding to this app

We now need to add the Google libraries to the app. To do so we'll need to find the path of your existing app, then install the Google libraries via pip.

* Navigate to the app home directory
* Create a library folder for App Engine to use in production:```mkdir lib```
* Type ```pwd``` to find the file path
* Execute ```pip install -t <path copied above>/lib google-auth google-auth-httplib2 google-api-python-client --upgrade```

Now the packages should be installed in the lib folder

## Adding credentials

* Log in here: https://console.cloud.google.com
* Follow: IAM & admin > Service Accounts > Create Service Account
* Name your service account
* Select "Furnish a new private key"
* Navigate to the app and create a folder: ```mkdir credentials```
* Insert the credential json into the file you just created and call it "sheets-cred.json"

## Editing your sheets

In reddit_data.py, changed the 'spreadsheetId' and 'rangeName' variables to your represent your sheet


## Starting the dev server

Navigate to the home folder and type: ```dev_appserver.py ./```. You should see instructions to find your dev server at http://localhost:8080

