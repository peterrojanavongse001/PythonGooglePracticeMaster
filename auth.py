# [START gmail_quickstart]
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

class auth:
    def __init__ (self, SCOPES, CLIENT_SECRET_FILE):
        self.SCOPES = SCOPES
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
        #self.APPLICATION_NAME = APPLICATION_NAME
    def get_credentials(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
