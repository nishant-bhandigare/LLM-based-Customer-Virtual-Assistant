from transformers import  AutoTokenizer, AutoModelForCausalLM

# Load fine-tuned model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2")
model = AutoModelForCausalLM.from_pretrained("Kaludi/Customer-Support-Assistant-V2", from_tf=True)

# Define your prompt
prompt = "You are an excellent Customer Service Assistant with excellent hold in technical services and you are tasked to get the details of the customer who is interacting with you by asking them in a conversational way. Dont ask all the fields at once be conversational and ask 1 thing at a time."

# Start conversation
conversation = []

while True:
    # Add prompt to ongoing conversation
    conversation.append(prompt)
    
    # Tokenize the conversation
    inputs = tokenizer.encode(" ".join(conversation), return_tensors="pt")
    
    # Generate response
    output = model.generate(inputs, max_length=1000, num_return_sequences=1)
    
    # Decode and print the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Assistant:", response)
    
    # Exit loop if all information is gathered
    if "technical assistant will be reaching at their preferred time at their place" in response:
        break
    
    # Ask for user input
    user_input = input("Your response: ")
    conversation.append(user_input)

print("Conversation ended.")
