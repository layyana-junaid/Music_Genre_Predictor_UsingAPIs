import requests
from transcribing_wav import transcript

#transcript = "i was a ghost i was alone you're so okay given the drone not didn't the know to believe i'm to wake up he'll feel like me put these patterns all in the past now and finally live like the girl they all see no more hiding i'll be shining like because we"

#print("Transcript:", transcript)  # optional

headers = {
    "Authorization": "Bearer YOUR GORQ API GOES HERE",  
    "Content-Type": "application/json"
}

#this is where the transcript will be inserted
payload = {
    "model": "llama3-8b-8192",
    "messages": [
        {
            "role": "user",
            "content": f"Given these lyrics, predict the music genre:\n\n{transcript}\n\nRespond with just the genre name."
        }
    ],
    "max_tokens": 50,
    "temperature": 0.5
}

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=payload
)

print("Predicted Genre:", response.json()["choices"][0]["message"]["content"])
