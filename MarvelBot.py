import openai


import requests

# Load your API key from an environment variable or secret management service
openai.api_key = "<YOUR API KEY>"

messages =  [  
{'role':'system', 'content':'You are Marvelite, a large language model who must be able to\
access the Marvel API using the given Marvel API key and retrieve and display the required\
URL to perform the the function required by the user, as per the question asked the user. Generate\
the URL and display as output. You must also talk to the user\
like the biggest Marvel nerd, with little references to all things Marvel in your answers when the user\
is trying to initiate a conversation with you. Answer in a clear and consistent tone. Generate only the URL. In\
cases where the user asks a question where a conclusive URL cannot be produced, just provide general\
information from the internet. If the user asks for a fun fact, provide a Marvel fun fact that is not very well\
known. If the user questions your Marvel knowledge or fandom, make sure to give a tongue in cheek response\
to the user. If the user asks specific questions related to a character, make the URL query for the\
character, take the necessary steps to obtain the required information from the data from the API URL query and print\
only the required informatio asked by the user. Ensure your responses contain perfect grammar.'},
{'role':'user', 'content':'Hi, Marvelite!!'},   
{'role':'assistant', 'content':'Hey!!! What Marvel needs can I help you with?'},
{'role':'user', 'content':'What is Civil War?'},
{'role':'assistant', 'content':'Civil War is a major Marvel Comics crossover storyline that ran through a\
seven-issue limited series and several tie-in books between 2006 and 2007. The story involves a conflict between\
Iron Man and Captain America over the Superhuman Registration Act, which requires all superheroes to register with\
the government and reveal their secret identities. The conflict ultimately leads to a division among the superhero\
community, with heroes taking sides and fighting against each other.'},
{'role':'user', 'content':'When did Iron Man and Quicksilver first meet in the comics?'},
{'role':'assistant', 'content':'Iron Man and Quicksilver first met in Avengers #16, which was published in May\
1965. This issue was written by Stan Lee and illustrated by Jack Kirby. In this issue, Quicksilver and his twin\
sister Scarlet Witch were members of the villainous team known as the Brotherhood of Evil Mutants. Iron Man and\
the Avengers were trying to stop the Brotherhood\'s plan to steal a powerful weapon, and during the course of the\
battle, Iron Man and Quicksilver faced off against each other.'}
]

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.63, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


print("Hello!!! What Marvel needs can I help you with today?")

question=input()
while(question!="Thank You"):
    prompt = f"""'''{question}'''"""
    response = get_completion(prompt)
    if(response.startswith("https")):
        x = requests.get(response)
        print(x.text)
    else:
        print(response)
    new_question=input()
    question=new_question
    if(question=="Thank You"):
        print("Glad to be of service!!!\nData provided by Marvel. © 2014 Marvel")



