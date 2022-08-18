from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pyasn1.type.univ import Null

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_google.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    
    # coleta a data do dia atual
    today = datetime.datetime.today().strftime('%Y-%m-%d')

    # verifica eventos no dia atual, no Brasil (-03:00)
    events_result = service.events().list(calendarId='###@group.calendar.google.com', 
                                        timeMin=today + 'T00:00:00-03:00', timeMax=today + 'T23:59:59-03:00',
                                        maxResults=5, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    summary = ''
    if not events:
        print('Nenhum evento registrado.')
    for event in events:
        # pesquisa pelo evento Trabalho na agenda, caso o título do evento seja registrado diferente, deve ser alterado aqui
        summary =  event['description'] if 'Trabalho' in event['summary'] else ''
    return summary


if __name__ == '__main__':
   main()
