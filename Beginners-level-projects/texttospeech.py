# Python program to convert
# text to speech
#Robo speaker

# import the required module from text to speech conversion
import win32com.client as wc

# Calling the Dispatch method of the module which 
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = wc.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    if s=="q":
       speaker.Speak("So , this is it ........ Goodbye my dear friend")
       break
    speaker.Speak(s)

# To stop the program press
# CTRL + Z