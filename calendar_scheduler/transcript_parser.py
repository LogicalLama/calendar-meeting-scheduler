import openai

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

# Function to parse transcript and extract call time using OpenAI
def openai_parse_transcript(transcript):
    prompt = f"Extract the time of the call from the following conversation:\n\n{transcript}\n\nThe time of the scheduled call is:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.5
    )
    
    result = response.choices[0].text.strip()
    return result
