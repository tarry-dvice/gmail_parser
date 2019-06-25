from __future__ import print_function
from message_tools import get_message_body, list_messages_with_labels
from label_tools import get__label_id

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    user_token_path = "user_data/token.pickle"
    creds_path = 'user_data/credentials.json'

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(user_token_path):
        with open(user_token_path, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for the next run
        with open(user_token_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # User input
    user_id = 'me'
    label_name = 'SENT' or input('Enter label name: ')

    # Call the Gmail API
    label_id = get__label_id(service=service, user_id=user_id, label_name=label_name)

    for msg in list_messages_with_labels(service=service, user_id=user_id, label_id=label_id):
        get_message_body(service=service, user_id=user_id, msg_id=msg['id'])


if __name__ == '__main__':
    main()
