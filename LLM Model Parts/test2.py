import speech_recognition as sr
import pyttsx3
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Load pretrained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def speech_to_text():
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def get_user_details():
    details = {}
    text_to_speech("Hi, this is Sophia, your smart solutions assistant. How may I help you today?")
    text_to_speech("Please tell me your full name.")
    user_input = speech_to_text()
    details["Full Name"] = user_input if user_input else ""
    
    text_to_speech("Are you facing a new issue or an existing issue?")
    user_input = speech_to_text()
    details["Nature of Issue"] = user_input if user_input else ""
    
    text_to_speech("Can you please tell me your contact number?")
    user_input = speech_to_text()
    details["Contact"] = user_input if user_input else ""
    
    text_to_speech("Please tell me your address with pincode.")
    user_input = speech_to_text()
    details["Address with Pincode"] = user_input if user_input else ""
    
    text_to_speech("Please provide details of your issue.")
    user_input = speech_to_text()
    details["Details of Issue"] = user_input if user_input else ""
    
    text_to_speech("When would you prefer the technical assistant's visit?")
    user_input = speech_to_text()
    details["Preferred date and time"] = user_input if user_input else ""
    
    return details

def main():
    # user_details = get_user_details()
    response = generate_response("Thank you for providing the details. A technical assistant will reach you at your preferred time at your place.")
    text_to_speech(response)

if __name__ == "__main__":
    main()
