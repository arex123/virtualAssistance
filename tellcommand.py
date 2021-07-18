import speech_recognition as sr
import pyttsx3
# from callbycommand import write
listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            # listener.pause_threshold = 1
            # voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except Exception as e:
        print("I think you are at very noisy place,\nThis is the error in computer languge: ")
        # write()

