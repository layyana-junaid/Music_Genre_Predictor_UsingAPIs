from pydub import AudioSegment

#converting the mp3 files to .wav for deepgram
audio = AudioSegment.from_mp3("Golden.mp3")
audio = audio.set_frame_rate(16000).set_channels(1) #it works best with 16kHz sampling rate
audio.export("golden.wav", format="wav")
