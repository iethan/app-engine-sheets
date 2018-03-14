import os
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/drive',
		  'https://www.googleapis.com/auth/spreadsheets']

spreadsheetId = '1qbAvTxUP-0I8eiYQVkXiLJo_3bT39JlW2uX2sVECvq8'
rangeName = 'A1:A2'

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
  # Production
	from google.auth import app_engine	

	credentials = app_engine.Credentials(scopes=SCOPES)  
else:
	#Development
	from google.oauth2 import service_account
	
	SERVICE_ACCOUNT_FILE = '/credentials/sheets-cred.json'

	credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, 
																		scopes=SCOPES)

service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
response = service.spreadsheets().values().get(spreadsheetId=apreadsheetId, range=rangeName).execute()




# import praw
# import json

# # create a file called cred.json and put it in the folder with this py file
# data = json.load(open('cred.json'))

# # the following must be keys in the dictionary, obtained from reddit, see https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

# client_secret = data['client_secret']
# client_id = data['client_id']
# user_agent =data['user_agent'] 

# r = praw.Reddit(client_id=client_id,
# 		client_secret=client_secret,
# 		user_agent=user_agent)

# for submission in r.subreddit('learnpython').hot(limit=10):
#     print submission.title
