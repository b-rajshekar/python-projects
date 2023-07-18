import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to speakingRobot 1.0 Created by rajshekar")
    print("Enter 'q' to quit.")

    while True:
        user_input = input("Enter something I'll speak: ")

        if user_input.lower() == 'q':
            speak("say 'Bye have a nice day and see you later'")
            print("speakingRobot 1.0 program Ended")
            break

        speak(user_input)