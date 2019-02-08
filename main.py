# [START gmail_quickstart]
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import auth

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'credentials.json'

authInst = auth.auth(SCOPES, CLIENT_SECRET_FILE)
credentials = authInst.get_credentials()
service = build('gmail', 'v1', http=http)

def get_labels():
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = credentials.get('labels', [])    

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

get_labels()