# ask dev(a automated robot) to play music or video on youtube, etc

import pywhatkit
import datetime
from askinternet.shortsol import quickres
from system.systemapp import appopen
import socket
from tellcommand import talk, take_command
from askinternet.weather import weather
import tkinter as tk
import webbrowser


def run_dev():
    talk("hello sir welcome tell me what you want me to do ")
    command = take_command()
    T.insert(tk.END, 'you-->'+command + '\n')

    print(command)
    if 'hi' in command:
        ask = "hello sir how are you "
        T.insert(tk.END, 'DEV-->' + ask + '\n')
        talk(ask)
        res = take_command()
        if 'fine' in res:
            talk("glad to hear that, what now sir")

    elif 'open' in command:
        appopen(command)
    elif 'search in google' in command:
        command = command.replace('search in google','')
        if len(command)==0:
            talk("what you want to search")
            command = take_command()
        print(command)
        url = 'https://google.com/search?q=' + command
        webbrowser.get().open(url)

    elif 'play' in command:
        song = command .replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        T.insert(tk.END, 'DEV--> current time is' + Time + '\n')
        talk('current time is ' + time)
    elif 'my ip address' in command:
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname) + ' is your ip address '
        print(ipaddress)
        talk(ipaddress)
    elif 'weather' in command:
        weather()

    else:
        command = command .replace('question', '')
        ans = quickres(command)
        T.insert(tk.END, 'DEV-->' + ans + '\n')


def onclick():
    print("button clicked")
    run_dev()


root = tk.Tk()
root.title("GUI for bot")
root.geometry('500x500')
T = tk.Text(root, height=5, width=52)


l = tk.Label(root, text ="Dev_Bot GUI")
l.config(font =("Courier", 14))

Fact = "Hello , I am dev bot"
# lie = "Hello , I am not dev bot"


# Create button for next text.
b1 = tk.Button(root, text="Start", command=onclick)

# Create an Exit button.
b2 = tk.Button(root, text="Exit", command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact+'\n')
# T.insert(tk.END, lie+'\n')


# button1.pack()
root.mainloop()
