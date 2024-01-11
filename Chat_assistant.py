import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

name = input("What is your Name?\n")
print(f'Hi {name} I am your Personalized bot!!')

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg}) 
# above line is optional, but it helps the chatbot understand the context of the conversation

print(f'Your {system_msg} assistant is ready!\n')

while input != "quit()": # type quit() to exit the program

    message = input()

    messages.append(
        {
        "role": "user",
        "content": message
        }
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    reply = response["choices"][0]["message"]["content"] 
    # get the reply from the chatbot response


    messages.append( 
    # append the reply to the messages list so that the chatbot can learn from it
        {
        "role": "assistant",
        "content": reply
        }
    )

    print("\n" + reply + "\n")