import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


#initialize text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(voice):
    engine.say(voice)
    engine.runAndWait()

def startUp():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        talk("Good Morning .")
    elif time >= 12 and time < 18:
        talk("Good Afternoon .")
    else:
        talk("Good Evening .")

    botName = ("Victor")
    greetingMsg = random.randrange(0, 10, 1)
    if greetingMsg in range(0,3):
        talk("What can I help you with ?")
    elif greetingMsg in range(3,7):
        talk("What do you want ?")
    elif greetingMsg in range(7,11):
        talk("Yes Sir?")

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        talk = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(talk, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    startUp()

    while True:
        query = takeCommand().lower()
        if 'start up my usual' in query:
            talk('Opening your usual .\n')
            webbrowser.open('facebook.com')
            webbrowser.open('youtube.com')
