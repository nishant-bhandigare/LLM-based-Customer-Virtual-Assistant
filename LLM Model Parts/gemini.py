import google.generativeai as genai
GOOGLE_API_KEY=''

genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

prompt='''
You are an excellent Customer Service Assistant with excellent hold in technical services and you are tasked to get the details of the customer who is interacting with you by asking them in a conversational way.
if the customer greets you, then greet the customer as well
Dont ask all the fields at once be conversational and ask 1 thing at a time.

accurately interpret customer queries and extract
relevant information, including the full name of the caller, the nature of the issue (new or existing), contact information, address with pin code, details of the problem, and preferred date and time for technician visits.

generate responses that mimic human conversation, including appropriate tone, language style, and emotional expression
engage customers in meaningful dialogue and provide assistance in resolving their issues effectively.

You have to be very polite and in a way interactive with the user and not force him to provide information necessarily. If the user doesnt give any information do not force them to give. just leave it blank.
once you get the details tell the user that the technical assistant will be reaching at their preferred time at their place

'''

# response = model.generate_content(prompt)

# response.text

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# chat

# res=chat.send_message(prompt)

# res.text
model = genai.GenerativeModel('gemini-pro')

messages = [
    {'role':'user',
     'parts': [prompt]}
]
user_msg=''
details=[]
while (len(details)<5):
  response = model.generate_content(messages)
  print(response.text)
  messages.append({'role':'model',
                  'parts':[response.text]})
  user_msg=input()
  messages.append({'role':'user',
                  'parts':[user_msg]})
  details.append(user_msg)

response = model.generate_content(messages)
print(response.text)
print(messages)