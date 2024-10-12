# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import subprocess

import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCpzYbRf6O7V03LBmNq0pQf0FAONuGLNEw")

model = genai.GenerativeModel('gemini-1.5-flash')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def makeTextFile(text):
    subprocess.Popen(f"echo '{text}' > text.txt", shell=True)
    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'hi' in query:
            speak('Hello Sir')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'write text' in query:
            speak("What should I write to this text file")
            text = takeCommand()
            makeTextFile(text)

        elif 'open terminal' in query:
            subprocess.Popen("start cmd", shell=True)
        
        elif 'play a game' in query:
            speak("You have installed the game or online?")
            online = takeCommand()
            if (online == "online"):
                speak("Which game do you want to play?")
                game = takeCommand()
                webbrowser.open("https://www.google.com/search?q="+game)
            elif (online != "online"):
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\League of Legends.lnk")

        elif 'quit' in query:
            speak("Thank you for using AI Nick's AI assistant. Have a nice day")
            break
        
        elif 'talk with ai' in query:
            speak("What should I ask the assistant?")
            while(query != "quit"):
                query = takeCommand()
                response = model.generate_content(task)
                print(response.text)
                speak(response.text)
        elif 'outside' in query:
            os.startfile("C:/Users/honsl/Downloads/outside.jpg")

        else:
            print("No query matched")
        
