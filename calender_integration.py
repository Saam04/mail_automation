import schedule
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
import schedule
import time

print(" Task Automation Script Started...")  # Debugging Message

while True:
    schedule.run_pending()
    print(" Waiting for the next scheduled task...")  # Added for Debugging
    time.sleep(60)  # Waits 60 seconds before checking again

# Load credentials
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "credentials.json"  # Update this with your file path

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=creds)
    return service

def create_event(summary, description, start_time, end_time):
    service = get_calendar_service()
    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f" Event created: {event.get('htmlLink')}")

#  Automate event scheduling at fixed times
schedule.every().monday.at("09:00").do(create_event, "Team Meeting", "Weekly Standup", "2025-03-10T09:00:00", "2025-03-10T10:00:00")
schedule.every().wednesday.at("15:00").do(create_event, "Project Review", "Check project progress", "2025-03-12T15:00:00", "2025-03-12T16:00:00")
schedule.every().friday.at("18:30").do(create_event, "Client Call", "Call with client", "2025-03-14T18:30:00", "2025-03-14T19:30:00")

#  Run the scheduler in a loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again
