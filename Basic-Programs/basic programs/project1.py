#robo speaker
import pyttsx3
if __name__ =='__main__' : #yaha se program suru 
    print("Welcome to Robospeaker .. Created by Srijan")
    
    while True:
        x=input("Enter what you want me to pronounce  : ")
        if x=="q":
            engine=pyttsx3.init()
            
            print("Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        engine=pyttsx3.init()
        engine.say(x)
        engine.runAndWait()#process speech before asking again

    #import winsound 
    #winsound.Beep(1000,500) #frequency , duration
    #this only makes beep sounds , not speech
    