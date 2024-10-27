from calendar_scheduler.google_calendar import authenticate_google_calendar, schedule_meeting
from calendar_scheduler.transcript_parser import openai_parse_transcript
from calendar_scheduler.time_processor import process_call_time

# Example transcripts and attendees
transcripts = [
    """
    User 1: "Hey team, we need to schedule a quick sync-up. Can everyone do 3 PM tomorrow?"
    User 2: "3 PM works for me."
    User 3: "Same here."
    """
]
attendees = ['alice@example.com', 'bob@example.org']

def main():
    # Authenticate Google Calendar
    service = authenticate_google_calendar()
    
    for idx, transcript in enumerate(transcripts):
        print(f"Processing transcript {idx + 1}:")
        
        # Extract call time from transcript
        call_time_str = openai_parse_transcript(transcript)
        print(f"Extracted call time: {call_time_str}")
        
        # Convert the extracted call time to datetime object
        call_time = process_call_time(call_time_str)
        print(f"Scheduling call at: {call_time}")
        
        # Schedule the meeting on Google Calendar
        schedule_meeting(service, call_time, attendees)
        print(f"Meeting scheduled for Transcript {idx + 1}\n")

if __name__ == '__main__':
    main()
