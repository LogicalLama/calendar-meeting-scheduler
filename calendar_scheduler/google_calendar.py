import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Authenticate Google Calendar API
def authenticate_google_calendar():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    
    if os.path.exists('../token.json'):
        creds = Credentials.from_authorized_user_file('../token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file('../credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('../token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('calendar', 'v3', credentials=creds)
    return service

# Function to schedule a meeting on Google Calendar
def schedule_meeting(service, call_time, attendees=None):
    event = {
        'summary': 'Scheduled Meeting',
        'location': '',
        'description': 'Automatically scheduled from parsed conversation.',
        'start': {'dateTime': call_time.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': (call_time + datetime.timedelta(hours=1)).isoformat(), 'timeZone': 'UTC'},
        'attendees': [{'email': attendee} for attendee in attendees] if attendees else [],
        'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 24 * 60}, {'method': 'popup', 'minutes': 10}]},
    }
    
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")
