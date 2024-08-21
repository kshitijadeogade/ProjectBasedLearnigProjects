#SIMULATION OF SPEECH TO TEXT CONVERSION

#IMPORTING LIBRARY

import speech_recognition as sr

#SPECIFYING FILE NAME

filename = "ML Class2 - (2 hours).wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
    

