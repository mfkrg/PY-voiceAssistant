from os import startfile
import subprocess
import os
import time
import speech_recognition
from selenium import webdriver

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Не распознано'



def say_hi():
    return 'Привет, mfkrg'

def open_browser():
    os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
    return

def open_discord():
    os.system('"C:\\Users\\Zahar\\AppData\\Local\\Discord\\app-1.0.9006\\Discord.exe"')
    return

def close_discord():
    os.system("taskkill /im Discord.exe")
    return


def main():
    while True:
        query = listen_command()
        if query == 'привет питон':
            print(say_hi())
        elif query == 'открой браузер':
            print('Открыл бразуер')
            open_browser()
        elif query == 'открой discord' or query == 'открой discord':
            open_discord()
        elif query == 'закрой discord' or query == 'закрой дискорд':
            close_discord()
        else:
            print('Не распознано')
            print(query)

if __name__ == '__main__':
    main()



