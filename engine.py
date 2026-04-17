import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
from ai_brain import ask_ai

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        command = r.recognize_google(audio)
        print("User:", command)
        return command.lower()

    except:
        return ""

def process(command, callback):

    def say(text):
        if callback:
            callback(text)
        speak(text)

    command = command.lower()

    # SYSTEM COMMANDS
    if "youtube" in command:
        say("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        say("Opening Google")
        webbrowser.open("https://google.com")

    elif "time" in command:
        t = datetime.datetime.now().strftime("%H:%M")
        say(f"Current time is {t}")

    elif "open notepad" in command:
        say("Opening Notepad")
        os.system("notepad")

    elif "exit" in command:
        say("Shutting down assistant")
        return False

    # 🔥 AI FALLBACK (SMART MODE)
    else:
        say("Thinking...")
        response = ask_ai(command)
        say(response)

    return True