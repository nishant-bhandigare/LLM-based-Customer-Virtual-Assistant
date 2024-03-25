import speech_recognition as sr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the GPT-2 model and tokenizer
# model_name = "gpt2-medium"
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# model = GPT2LMHeadModel.from_pretrained(model_name)

# Initialize the T5 model and tokenizer
# model_name = "t5-small"
# tokenizer = T5Tokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)

model_name = "EleutherAI/gpt-neo-125M"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name)

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results.")
            return None

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

while True:
    user_input = recognize_speech()
    if user_input:
        response_text = generate_response(user_input)
        print("Assistant:", response_text)
        engine.say(response_text)
        engine.runAndWait()
