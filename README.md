# Journal CLI with Google Sheets API

A simple command-line tool to quickly journal your day using a one-sentence summary inspired by the book *Storyworthy*. Entries are stored in a Google Sheets spreadsheet.

## Features

* Write a journal entry directly from the terminal
* Automatically logs the date and time
* Saves entries to your Google Sheets

---

## Setup Instructions (Step by Step)

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Go to **APIs & Services > Library**.
4. Enable the **Google Sheets API** and **Google Drive API** for your project.

### 2. Create OAuth Credentials

1. Go to **APIs & Services > Credentials**.
2. Click **+ CREATE CREDENTIALS > OAuth client ID**.
3. Select **Desktop App**.
4. Name it anything (e.g., `JournalCLI`).
5. Click **Download JSON** — rename it to `credentials.json` and put it in the same folder as your script.

### 3. Install Required Python Packages

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 4. Authenticate

Run the Python script for the first time to trigger authentication:

```bash
python journal.py "Your first journal entry"
```

This will open a browser asking for permission to access your Google account. After you allow access, a `token.json` file will be generated.

### 5. Prepare Your Google Sheet

1. Go to [Google Sheets](https://sheets.google.com/).
2. Create a new spreadsheet and name it something like `Journal Entries`.
3. In `journal.py`, make sure you paste the spreadsheet ID from the URL:

```
https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit#gid=0
```

4. Also ensure your service account/email has access to edit the sheet (Share > add email).

---

## How to Use

Make sure your shell script (`j.sh`) and Python script (`journal.py`) are in the same folder.

Example command:

```bash
./j.sh "Had a breakthrough with my ML model deployment!"
```

It will automatically write the date and entry to your spreadsheet.

---

## Folder Structure Example

```
📂 Journal CLI
├── credentials.json
├── token.json
├── journal.py
├── j.sh
└── venv/
```

---

## License

MIT

---

## Inspired by

* [Storyworthy by Matthew Dicks]([https://www.goodreads.com/book/show/38723597-storyworthy](https://www.goodreads.com/book/show/37786022-storyworthy))
* The power of micro-journaling for personal growth.
