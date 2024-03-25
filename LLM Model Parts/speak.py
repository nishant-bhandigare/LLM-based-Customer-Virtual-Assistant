import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant: Hello, how can I assist you today?")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service."

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def assistant_response(text, language='en'):
    if language == 'hi':
        # Translate to Hindi
        translated_text = translate_text(text, 'hi')
        print(f"Assistant (Hindi): {translated_text}")
        tts = gTTS(text=translated_text, lang='hi', slow=False)
    else:
        print(f"Assistant: {text}")
        tts = gTTS(text=text, lang='en', slow=False)
    
    tts.save("assistant_response.mp3")
    os.system("mpg321 assistant_response.mp3")  # Use "afplay" on macOS or "aplay" on Linux

def main():
    while True:
        user_input = recognize_speech()
        print("You:", user_input)

        if 'exit' in user_input.lower():
            print("Assistant: Goodbye!")
            break

        # Determine the language of user input (English or Hindi)
        language = 'en' if user_input.isascii() else 'hi'

        assistant_response(user_input, language)

if __name__ == "__main__":
    main()
