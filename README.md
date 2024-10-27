# Calendar Meeting Scheduler

This project extracts meeting times from conversational transcripts using OpenAI GPT and schedules meetings on Google Calendar.

## Setup

### Prerequisites
- Python 3.7+
- Google Calendar API credentials (`credentials.json`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/calendar-meeting-scheduler.git
   cd calendar-meeting-scheduler
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your Google Calendar API credentials in the project root as `credentials.json`.

### Running the Script

1. Run the main script:

   ```bash
   python main.py
   ```

2. You'll be prompted to log in to Google Calendar the first time to generate `token.json`.

## File Structure

- `main.py`: The main script that orchestrates the scheduling process.
- `token.json`: OAuth token (auto-generated after first run).
- `credentials.json`: Google OAuth 2.0 credentials file.
- `calendar_scheduler/`: Contains the core functionality split into modules.
  - `google_calendar.py`: Functions to authenticate and schedule meetings on Google Calendar.
  - `transcript_parser.py`: Functions to parse transcripts and extract call times using OpenAI.
  - `time_processor.py`: Functions to convert extracted times to proper `datetime` objects.
