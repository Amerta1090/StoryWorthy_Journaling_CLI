import os
import sys
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1vDFoWgJ7dK0scz8xGdONPK-yg8z9pr5rWG9A6kry4QY'
RANGE_NAME = 'Sheet1!A:B'  # Kolom A = tanggal, B = catatan

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def append_entry(text):
    creds = authenticate()
    service = build('sheets', 'v4', credentials=creds)

    date_str = datetime.date.today().isoformat()
    values = [[date_str, text]]
    body = {'values': values}

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body
    ).execute()
    print(f"✅ Ditambahkan: {date_str} - {text}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("❌ Gunakan: python journal.py 'catatan'")
        sys.exit(1)
    note = " ".join(sys.argv[1:])
    append_entry(note)
