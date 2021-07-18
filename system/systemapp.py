import os
import webbrowser
import cv2
from pyttsx3 import speak
from tellcommand import take_command


def appopen(command):
    if 'notepad' in command:
        path = 'C:\\WINDOWS\\system32\\notepad.exe'
        os.startfile(path)
    elif 'command prompt' in command:
        os.system("start cmd")
    elif 'open camera' in command:
        cap = cv2.VideoCapture(0)
        if not (cap.isOpened()):
            print('Could not open video device')

        while 1:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif 'youtube' in command:
        webbrowser.open("www.youtube.com")
    elif 'google' in command:
        speak("what you want to search ")
        search = take_command().lower()
        webbrowser.open(f"{search}")
