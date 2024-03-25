from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    # Example text to translate
    text_to_translate = "Hello, how can I assist you today?"

    # Target language (e.g., 'hi' for Hindi, 'es' for Spanish, 'fr' for French, etc.)
    target_language = 'hi'  # Change this to your desired language code

    # Translate the text
    translated_text = translate_text(text_to_translate, target_language)

    # Display the translated text
    print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    main()
