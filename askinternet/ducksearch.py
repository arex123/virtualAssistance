import webbrowser
import pyttsx3
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def searching(text):
     url = 'https://google.com/search?q=' + text
     webbrowser.get().open(url)
