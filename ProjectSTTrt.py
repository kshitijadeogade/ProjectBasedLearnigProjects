#REAL TIME SPEECH TO TEXT CONVERSION

#importing the library
print("SPEECH TO TEXT")

import speech_recognition as sr

r=sr.Recognizer()

r.energy_threshold = 300

#CREATING A CLASS
#DEFINING FUNCTION AND OBJECT

def mp(sr,r):
    with sr.Microphone() as source:
        
        print("Talk")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio_text=r.listen(source)
        print("Time Over, Thanks")

        try:
            t=r.recognize_google(audio_text)
            print("Text: ",t)
        except:
            print("Sorry , I m unable to recognize")
            
#CALLING FUNCTION            
mp(sr,r)   
    
