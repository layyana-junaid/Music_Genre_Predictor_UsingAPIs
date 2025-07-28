import requests

DG_API_KEY = "API KEY GOES HERE"
file_path = "golden.wav"

with open(file_path, 'rb') as f: #read hum binary mai krwa rhy hain jbtw (why cause it is API's requirement!)
    audio_data = f.read()

#passing API key to Deepgram for authorization 
headers = {
    'Authorization': f'Token {DG_API_KEY}',
    'Content-Type': 'audio/wav', #specifying the type of content that we are sending 
    #in our case we are sending audio file which is in .wav format 
}

#sending request to deepgram to authenticate the process
response = requests.post(
    'https://api.deepgram.com/v1/listen',
    headers=headers,
    data=audio_data
)

transcript = response.json()['results']['channels'][0]['alternatives'][0]['transcript'] #converting the json file (from the Deepgram)
                                                                                        #to python -accessing the transcript.
print("Transcript:", transcript)


