from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, this is a text-to-speech example."

# Language (en for English)
language = 'en'

# Initialize the gTTS object with text and language
tts = gTTS(text=text, lang=language, slow=False)

# Save the audio file
tts.save("output.mp3")

# Play the audio file
os.system("start output.mp3")  # For Windows
# os.system("afplay output.mp3")  # For MacOS
# os.system("mpg321 output.mp3")  # For Linux
