import speech_recognition as sr
import pyttsx3
import requests
from googletrans import Translator
import os
import google.generativeai as genai

# API key for Google Gemini
GOOGLE_API_KEY=''
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Target language
target_language = 'en'

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the speech
    engine.setProperty('rate', 180)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

def generate_response_gemini(user_input):
    # url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    # headers = {"Authorization": f"Bearer {API_KEY}"}
    # data = {"contents": [{"parts": [{"text": user_input}]}]}
    # response = requests.post(url, headers=headers, json=data)
    # response.raise_for_status()  # Raise an exception for error responses
    # response_json = response.json()
    # generated_text = response_json["generatedContent"]["parts"][0]["text"]
    # return generated_text

    response = model.generate_content(user_input)
    return response


    

def main():
    intro = "Hey, this is Ethan. How may I help you?"
    text_to_speech(intro)
    print("CVA:", intro)

    user_input = ""

    while (user_input != "goodbye"):
        user_input = speech_to_text()
        print("User:", user_input)

        CVA_response = generate_response_gemini(user_input)

        print(CVA_response)
        text_to_speech(CVA_response)

if __name__ == "__main__":
    main()
