from askinternet.ducksearch import searching
import wikipedia as wk

import pyttsx3
engine = pyttsx3.init()


def talk1(text):
        engine.say(text)
        engine.runAndWait()
  

def wikiask(command):  
    try:  
        # if 'star' in command:
        #     command = command.replace("star","")
        Ans = wk.summary(command)
        print(command + " : " + Ans)
        talk1(Ans)
        return Ans


    except Exception as e:
        print("sorry couldn't find the query in wikipedia")
        talk1("sorry couldn't find the query in wikipedia")
        talk1("want to look in google, press 1")
        fur = input("wanna look in google press 1")
        if '1' in fur:
           searching(command)
        else:
            exit()

