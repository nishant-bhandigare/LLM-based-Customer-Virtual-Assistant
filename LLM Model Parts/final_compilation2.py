from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define language models and tokenizers (one for English, one for Hindi)
ENGLISH_MODEL = "facebook/bart-base"
HINDI_MODEL = "Someman/bart-hindi"
english_tokenizer = AutoTokenizer.from_pretrained(ENGLISH_MODEL)
hindi_tokenizer = AutoTokenizer.from_pretrained(HINDI_MODEL)

# Function to detect language based on user input
def detect_language(text):
  if "हिंदी" in text:
    return "hindi"
  else:
    return "english"

# Function to generate response using LLM
def generate_response(model, tokenizer, prompt, max_length=512):
  input_ids = tokenizer.encode(prompt, return_tensors="pt")
  output = model.generate(input_ids, max_length=max_length)
  return tokenizer.decode(output[0], skip_special_tokens=True)

# Function to handle conversation flow
def conversation():
  # Initialize CVA
  print("Hi, this is Sophia, your smart solutions assistant. How are you?")
  user_lang = detect_language(input())
  if user_lang == "hindi":
    model = AutoModelForSeq2SeqLM.from_pretrained(HINDI_MODEL)
  else:
    model = AutoModelForSeq2SeqLM.from_pretrained(ENGLISH_MODEL)
  tokenizer = english_tokenizer if user_lang == "english" else hindi_tokenizer

  # Conversation loop
  while True:
    user_input = input("> ")
    response = generate_response(model, tokenizer, user_input)
    print(response)

    # Data extraction logic
    if "समस्या" in user_input and user_lang == "hindi" or "problem" in user_input:
      # Extract problem description
      problem_desc = input("Please describe the problem in detail: ")

    if "नाम" in user_input and user_lang == "hindi" or "name" in user_input:
      # Extract full name
      full_name = input("Please enter your full name: ")

    if "फोन" in user_input and user_lang == "hindi" or "phone" in user_input:
      # Extract contact number
      contact_number = input("Please enter your contact number: ")

    if ("पता" in user_input or "पिन कोड" in user_input) and user_lang == "hindi" or ("address" in user_input or "pincode" in user_input):
      # Extract address with pincode
      address = input("Please enter your address with pincode: ")

    # Technician visit preference
    if "समय" in user_input and user_lang == "hindi" or "time" in user_input:
      # Extract preferred date and time
      date_time = input("What date and time works best for you for a technician visit? ")

    # Check if all details are collected
    if all([full_name, contact_number, problem_desc, address]):
      # Create ticket in JSON format
      ticket = {
          "name": full_name,
          "contact": contact_number,
          "problem": problem_desc,
          "address": address,
          "preferred_visit": date_time,
          "language": user_lang
      }
      print(f"Thank you! A ticket has been created with details: {ticket}")
      break

if __name__ == "__main__":
  conversation()
