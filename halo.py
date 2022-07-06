import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import random

Halo = pyttsx3.init('sapi5')
voices = Halo.getProperty('voices')

Halo.setProperty('voice', voices[1].id)


def speak(sound):
    Halo.say(sound)
    Halo.runAndWait()


def Wishing():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hey There,Good morning Nithin")
    elif hour >= 12 and hour < 18:
        speak("Hey There,Good afteroon Nithin")
    else:
        speak("Good evening sir")
    speak("I am Olivia,i am here to assist you")


def takeCommand():
    # takes microphone input from the user and returns string output"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        sound = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(sound)
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        hj = ["I am not sure I understood that", "please sir,repeat it again",
              "can you spell it for me once more", "sorry sir i didnt get that"]
        speak(hj[random.randint(0, 3)])
        return "None"
    return query


if __name__ == "__main__":
    speak("Nithin,Good Luck for your Future")
    Wishing()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia"+str(speak(results)))
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("As you wish sir")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("as you said sir")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'who are you' in query:
            speak("I am olivia,a virtual artificial intelligence and I am here to assist you variety of tasks as best I can")
