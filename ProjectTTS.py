#TEXT TO SPEECH CONVERSION
print("TEXT TO SPEECH")
#IMPORTING THE REQUIRED FOR TEXT TO SPEECH CONVERSION
import gtts

# This module is imported so that we can play the converted audio
import playsound

#ASKING USER INPUT
#THE TEXT FOR WHICH USER WANTT TO LISTEN SPEECH

text = input("Enter text to convert: ")

#SPECIFYING THE LANGUAGE IN WHICH YOU WANT TO CONVERT AUDIO

sound = gtts.gTTS(text, lang="en", slow = False)

#SAVING THE AUDIO

sound.save("welcome.mp3")

#PLAYING THE AUDIO

playsound.playsound("welcome.mp3")



