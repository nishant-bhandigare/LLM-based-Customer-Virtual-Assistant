import speech_recognition as sr
from gtts import gTTS
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    # Recognize speech using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

# def speak(text, language=None):

def text_to_speech(text):
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)

    # Use BytesIO to avoid writing to file
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    # Reset the buffer to the beginning
    mp3_fp.seek(0)

    # Load the mp3 buffer
    audio = AudioSegment.from_file(mp3_fp, format="mp3")

    # Play the audio
    play(audio)


if __name__=="__main__":
    text = speech_to_text()
    LLM_Model(text)
    text_to_speech(text=text)

