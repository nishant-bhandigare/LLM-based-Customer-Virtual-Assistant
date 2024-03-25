from transformers import pipeline
import pyttsx3
import speech_recognition as sr

# Initialize speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Initialize LLM pipeline with a different pretrained model (e.g., GPT-3)
cva = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

def listen():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    while True:
        try:
            user_input = listen()
            print("User Input:", user_input)
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            continue
        except sr.RequestError as e:
            speak("There was an error processing your request.")
            print(f"Error: {e}")
            continue

        # Generate response using LLM
        assistant_response = cva(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        print("Assistant Response:", assistant_response)

        # Convert response to speech
        speak(assistant_response)

if __name__ == "__main__":
    main()
