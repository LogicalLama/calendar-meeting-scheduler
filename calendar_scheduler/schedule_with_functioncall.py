import openai
from calendar_scheduler.transcript_parser import openai_parse_transcript
from calendar_scheduler.time_processor import process_call_time
from datetime import datetime

# Function to handle the scheduling of a calendar meeting (invoked by OpenAI's function-calling)
def schedule_meeting(call_time: str, attendees: list):
    # Normally, you'd integrate this with a Google Calendar API or similar service
    try:
        # Simulate scheduling a meeting (for illustration purposes)
        meeting_time = datetime.strptime(call_time, "%Y-%m-%dT%H:%M:%S")
        print(f"Meeting scheduled at {meeting_time} for attendees: {', '.join(attendees)}")
        return {"status": "success", "time": call_time, "attendees": attendees}
    except Exception as e:
        print(f"Error scheduling the meeting: {e}")
        return {"status": "failed", "error": str(e)}


# Hypothetical OpenAI API function to trigger meeting scheduling via function calling
def openai_schedule_meeting_via_function_call(call_time, attendees):
    try:
        # Make an OpenAI API request with function-calling enabled
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for scheduling meetings."},
                {"role": "user", "content": f"Schedule a meeting at {call_time} with {', '.join(attendees)}"}
            ],
            functions=[
                {
                    "name": "schedule_meeting",
                    "description": "Schedules a meeting on a calendar",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "call_time": {"type": "string", "description": "ISO formatted time for the meeting."},
                            "attendees": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "List of email addresses of attendees."
                            }
                        },
                        "required": ["call_time", "attendees"]
                    }
                }
            ],
            function_call="auto"  # Let the model decide when to call the function
        )

        # Check if a function call was triggered
        if response.choices[0].finish_reason == "function_call":
            function_call_data = response.choices[0].message['function_call']
            # Extract arguments and call the function
            function_name = function_call_data['name']
            function_args = function_call_data['arguments']
            if function_name == "schedule_meeting":
                # Call the scheduling function with the extracted arguments
                schedule_meeting(**eval(function_args))

    except Exception as e:
        print(f"Error with OpenAI API request: {e}")