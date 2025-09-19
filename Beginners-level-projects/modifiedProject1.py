import pyttsx3

def main():
    print("Welcome to Robospeaker .. Created by Srijan")

    # Initialize the engine only once
    engine = pyttsx3.init('sapi5')  # 'sapi5' is specific to Windows

    # Optional: Customize voice settings
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 = Male, 1 = Female (usually)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Max volume (0.0 to 1.0)

    while True:
        x = input("Enter what you want me to pronounce (or type 'q' to quit): ")

        if x.strip().lower() == "q":
            print("Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()

if __name__ == '__main__':
    main()
