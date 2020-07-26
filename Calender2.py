from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta

'''scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes=scopes)   ---> The credentials.json file can be obtained by 
                                                                                            signing in for the google calendar API and creating 
                                                                                            your client secrets and saving it as a .json file.

credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl","wb"))'''

'''We don't have to execute the above block again because we have 
saved the tokens (aka the credentials) into a pickle (.pkl) file called "token.pkl",
so that now we can directly load the credentials (tokens) from it.'''

'''I have not uploaded the files related to credentials for security purpose. So, create your own credentials.'''

credentials = pickle.load(open("token.pkl","rb"))

service = build("calendar","v3",credentials=credentials)
result = service.events().list(calendarId="<Your calendar id here>").execute()   # Your calendar id is most probably your email id

start_time = datetime(2020, 7, 28, 11,15,00)
end_time = start_time + timedelta(hours=24)
timezone = 'Asia/Kolkata'
event = {
  'summary': 'It is my birthday',
  'location': 'Tirunelveli',
  'description': 'Today is my birthday!',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'recurrence': [
    'RRULE:FREQ=YEARLY;COUNT=57'
  ],
  'attendees': [
    {'email': ''},
    {'email': ''},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId="<Your calendar id here>", body = event).execute()