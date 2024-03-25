import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import googletrans as translator
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from pydub import AudioSegment
from pydub.playback import play

# Define language codes
languages = {
    "english": "en",
    "hindi": "hi"
}

# Initialize recognizer, translator, and tokenizer
recognizer = sr.Recognizer()
detected_language = ""
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2", )
model = AutoModelForSeq2SeqLM.from_pretrained("Kaludi/Customer-Support-Assistant-V2", from_tf=True, )

def generate_response(user_input):
    """Generates a response using the transformer model"""
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def speak(text, lang_code):
    """Converts text to speech and speaks the audio"""
    tts = gTTS(text=text, lang=lang_code)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)
    return audio_stream

def detect_language():
    """Listens for user input and detects language"""
    global detected_language
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        detected_language = translator.Translator().detect(text).lang
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error detecting language: {e}")
    return text

def ask_user(question, language):
    """Asks the user a question and returns the response"""
    speak(question, language)
    return detect_language()

def main():
    details=[]
    """Main loop for interaction"""
    # Determine language based on user input or default to English
    language = languages.get(detected_language, languages["english"])
    
    # Greet the user and ask for their name
    full_name = ask_user("Hello! May I have your full name, please?", language)

    # Ask for the nature of the issue
    nature_of_issue = ask_user("What is the nature of your issue? (New Issue or Existing Issue)", language)

    # Ask for contact information
    contact = ask_user("Could you please provide your contact number?", language)

    # Ask for address with pincode
    address = ask_user("What is your address along with pincode?", language)

    # Ask for details of the issue
    issue_details = ask_user("Please describe your issue in detail.", language)

    # Ask for preferred date and time for technical assistant's visit
    preferred_time = ask_user("When would you prefer the technical assistant to visit? (Morning, Afternoon, Evening, Night)", language)

    # Confirm receipt of information and inform the user about the technical assistant's visit
    confirmation_message = f"Thank you, {full_name}. Your issue regarding {nature_of_issue} has been recorded. Our technical assistant will reach out to you at your preferred time of {preferred_time}."
    speak(confirmation_message, language)
    details.append(full_name,nature_of_issue, preferred_time, contact, address, issue_details)
if __name__ == "__main__":
    main()
