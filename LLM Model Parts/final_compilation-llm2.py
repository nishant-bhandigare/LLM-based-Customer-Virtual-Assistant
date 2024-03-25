import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import json
GOOGLE_API_KEY='AIzaSyBKFI9vTUNZ2b4sQh-IRSrRb0zb98QsL8o'

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

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the speech
    engine.setProperty('rate', 180)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

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

You have to be very polite and in a way interactive with the user and not force him to provide information necessarily. If the user doesnt give any information do not force them to give. just leave it blank. 
once you get the deatils tell the user that the technical assistant will be reaching at their preferred time at their place
after getting all the information you need to give a json representation of the information whenever the user says goodbye.

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
    # if(response )
    messages.append({
        'role':'model',
        'parts':[response.text]
    })

    return response.text

        
type(messages)
        
def main():
    intro = "Hey, this is Ethan. How may I help you?"
    print("CVA:", intro)
    text_to_speech(intro)    
    user_input=""

    while True:
        user_input = speech_to_text()
        print("User:", user_input)
        if "goodbye" in user_input:
            json_save()
            break

        response= generate_response(user_input)

        print("CVA:", response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
    json_save()