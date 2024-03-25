import speech_recognition as sr
import pyttsx3
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="SantiagoPG/chatbot_customer_service")
# Load the tokenizer and model using TensorFlow weights

tokenizer = AutoTokenizer.from_pretrained("SantiagoPG/chatbot_customer_service")
model = AutoModelForSeq2SeqLM.from_pretrained("SantiagoPG/chatbot_customer_service")
# Rest of your code remains the same


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

def generate_response(user_input):
    # Tokenize the user input
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids

    # Generate a response from the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    
    # Decode and return the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():

    intro = "Hey, this is Ethan. How may I help you?"
    text_to_speech(intro)
    print("CVA:", intro)

    user_input=""

    while (user_input!="goodbye"):
        user_input = speech_to_text()
        print("User:", user_input)

        CVA_response = generate_response(user_input)

        print(CVA_response)
        text_to_speech(CVA_response)

if __name__ == "__main__":
    main()