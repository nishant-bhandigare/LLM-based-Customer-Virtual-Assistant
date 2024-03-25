import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
GOOGLE_API_KEY='AIzaSyBKFI9vTUNZ2b4sQh-IRSrRb0zb98QsL8o'
from googletrans import Translator
from gtts import gTTS
import io
import pygame
import json

target_lang = "hi"


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

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

# def text_to_speech(text):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()

#     # Set properties for the speech
#     engine.setProperty('rate', 180)  # Speed of speech
#     engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

#     # Speak the text
#     engine.say(text)
#     engine.runAndWait()
    
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


def translate_text(text, target_lang = target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text


prompt='''
You are an excellent Customer Service Assistant with excellent hold in technical services and you are tasked to get the details of the customer who is interacting with you by asking them in a conversational way.

Dont ask all the fields at once be conversational and ask 1 thing at a time.

The details that you need to get are 
Full Name: String Format First_Name Middle_Name Last_Name
Nature of Issue: String Format New_Issue || Exist_Issue
Contact: Number phone_number
Address with pincode: String Format 
Details of Issue: String format (Long Paragraph)
Preffered date and time for technical assistants visit: Date and period of day (Morning || Evening || Night)
In the format of :
{
    "name":"aditya",
    "phoneno":"86868",
    "address":"Vasai 401202",
    "problem_detail":"Keyboard not working",
    "nature_of_issue":"Existing",
    "date":"Sunday evening at 8 pm"
    }
You have to be very polite and in a way interactive with the user and not force him to provide information necessarily. If the user doesnt give any information do not force them to give. just leave it blank. 
once you get the deatils tell the user that the technical assistant will be reaching at their preferred time at their place
after getting all the information you need to give a json representation of the information whenever the user says goodbye.

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

    messages.append({
        'role':'model',
        'parts':[response.text]
    })

    return response.text


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
        
def main():
    intro = "Hey, this is Ethan. How may I help you?"
    intro = translate_text(intro)
    print("CVA:", intro)
    text_to_speech(intro)    
    user_input=""

    while True:
        user_input = translate_text(speech_to_text())
        print("User:", user_input)

        if "goodbye" in user_input:
            break

        response= translate_text(generate_response(user_input))

        print("CVA:", response)
        text_to_speech(response)


if __name__ == "__main__":
    main()
    json_save()