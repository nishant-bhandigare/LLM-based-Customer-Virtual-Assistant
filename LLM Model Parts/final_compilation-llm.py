import speech_recognition as sr
import pyttsx3
from google.cloud import translate_v2 as translate
import google.generativeai as genai
from gtts import gTTS
import io
import pygame
import re
from pymongo import MongoClient
import json
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
uri = os.environ.get("URI")

target_lang = "hi"

# App initialization
generation_config = {    
  "temperature": 0.3,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config, safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:HarmBlockThreshold.BLOCK_NONE,
          
        
    })
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

    
def text_to_speech(text, speed =2):
    tts = gTTS(text=text, lang=target_lang)

    # Use a BytesIO object to hold the audio data
    audio_bytes_io = io.BytesIO()

    # Write the audio data to the BytesIO object
    tts.write_to_fp(audio_bytes_io)

    # Reset the pointer of the BytesIO object to the beginning
    audio_bytes_io.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio data from the BytesIO object
    pygame.mixer.music.load(audio_bytes_io)

    # Play the audio
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue
    # Close the BytesIO object
    audio_bytes_io.close()

def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return (result['translatedText'])

prompt='''You are a polite Customer Service Assistant specializing in technical services related only with laptops. Engage the customer in a conversational manner to gather the following details one at a time:

- Contact Number (ask first)
- Full Name (First_Name Middle_Name Last_Name)
- Nature of Issue (New Issue || Existing Issue)
- Address with pincode
- Details of Issue (Long Paragraph)
- Preferred date and time for a technician visit (Date and Morning || Evening || Night)

Do not push for details if the customer is unwilling to provide them. Once all details are collected, confirm the appointment and present the information in the JSON format when the customer says goodbye.
Ask straight forward questions in minimum words
Example JSON:
```json
{
    "name": "first_name middle_name last_name",
    "phoneno": "1234567890",
    "address": "123 Main Street, Florida 401202",
    "problem_detail": "Keyboard not working properly.",
    "nature_of_issue": "Existing",
    "date": "Sunday evening at 8 pm"
}
```
'''


messages=[]
messages.append({
    'role':'user',
    'parts':[prompt]})

messages.append({
    'role':'model',
    'parts':"What's Your name?"           
    })
messages.append({
    'role':'user',
    'parts':"Hi"
  })
messages.append({
    'role':'model',
    'parts':"Hi, there, thank you for contacting us! My name is ethan, and I'm here to assist you today. Could you tell me your full name so I can address you properly?"
  })


def generate_response(user_input):

    message= user_input
    messages.append({
        'role':'user',
        'parts':[message]
        })
    
    response = model.generate_content(messages)

    part = response.text
    if "```json" in part:
        subpart=f"""{part}"""
        json_data = re.search(r'```json\s*(\{.*?\})\s*```', subpart, re.DOTALL).group(1)
        data = json.loads(json_data)
        client = MongoClient(uri)
        database = client["userInformation"]
        collection = database["users"]
        collection.insert_one(data,)
        client.close()
        part = "Thankyou for your time"
    messages.append({
        'role':'model',
        'parts':[part]
    })
    return part



def json_save():    
    desired_json_representation = None

    for item in messages:
        if item['role'] == 'model':
            if ('```\n' or "```" or "```json" or "json") in item['parts'][0]:
                desired_json_representation = item['parts'][0].split('')[1]
                break


    if desired_json_representation:
        # Save to a file
        with open("extracted_data.json", "w") as outFile:
            outFile.write(desired_json_representation)
        
        print("Data saved to extracted_data.json")
    else:
        print("Desired JSON representation not found.")
        
def main(tr):
    intro = "Hello, I'm Rasika. How may I help you?"
    intro = translate_text(text = intro, target=tr )
    print("CVA:", intro)
    text_to_speech(text = intro)    
    user_input=""
    while True:
        user_input = translate_text(text = speech_to_text(), target="en")
        print("User:", user_input)

        if "goodbye" in user_input:
            break

        response= translate_text(text=generate_response(user_input), target=tr)

        print("CVA:", response)
        text_to_speech(response)


if __name__ == "__main__":
    tr = input("language?\n\nHindi -> hi\n Marathi-> mr\n English -> en\n\n").lower()
    main(tr=tr)