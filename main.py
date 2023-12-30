import datetime
import random
import speech_recognition as sr
import os
import win32com.client
import webbrowser
from openai import OpenAI
import openai
from config import apikey

chatStr = ""
def chat(query):
    global chatStr
    # print(chatStr)

    api_key = ""
    client = OpenAI(api_key=api_key)

    chatStr += f"Prajwal : {query}\nKitkat : "

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    chatStr += f"{response.choices[0].text}\n"
    print(chatStr)
    say(response.choices[0].text)
    return response.choices[0].text


def ai(prompt):

    api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *****************************\n\n"
    client = OpenAI(api_key=api_key)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # text += response["choices"][0]["text"]
    if hasattr(response, "choices") and response.choices:
        text += response.choices[0].text
    else:
        print("Unexpected response structure:", response)

    print("Task Completed")
    say("The task is completed")


    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)

def say(text):
    speaker = win32com.client.Dispatch("Sapi.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language ="en-in")
            # print(f"user said : {query}")
            return query
        except Exception as e:
            return "Some error has occurred"

if __name__ == '__main__':
    print("Hello I am KitKat AI")
    say("Hello I am KitKat the AI")

    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"],["wikipedia","htps://www.wikipedia.com"],["google","https://www.google.com"]]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {strfTime}")
            say(f"Sir the time is {strfTime}")

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt = query)

        elif "stop".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Typing...")
            chat(query)

