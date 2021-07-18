from askinternet.ducksearch import searching
from pyexpat import error
from askinternet.wiki import wikiask
import wolframalpha
from tellcommand import take_command, talk
client = wolframalpha.Client("LLKY8E-9XT98YXP3T")
import pyttsx3

engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


# wolframalpha command for asking Q from its server

def quickres(command):
    try:
        res = client.query(command)
        Ans = next(res.results).text
        print(command + " is " + Ans)
        talk(Ans)
        return Ans
        if 'no data' in Ans:
            talk("let me search in google")
            searching(command)
    except Exception as e:
        print("sorry couldn't find the query in walframalpha")
        talk("sorry couldn't find the query in walframalpha")
        talk("want to look in wikipedia or google")

        fur = take_command()
        if 'wikipedia' in fur:
            print('looking in wikipedia')
            wiki_res = wikiask(command)
            return wiki_res
        elif 'google' in fur:
            print('searching in google')
            searching(command)
        else:
            exit()
