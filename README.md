# Marvelite
Marvelite, powered by Marvel API and OpenAI, is a Marvel chatbot that will be able to answer the user's queries regarding Marvel Comics and the MCU, from characters to events to stories and more.

Marvelite, is an AI chatbot created using OpenAI that can tap into the resources available in Marvel API and get data that the user's question requires from the database.
We use a model trained to read the user's question, understand the question and devise the required API URL required to get the information that answers the user's question, we then use the URL to tap into Marvel API and get the necessary resources, using the requests module and get function in Python. The model is trained via system specifications, as well as few-shot prompting to create a chatbot that can handle different types of queries on all things Marvel

NOTE : The scope of 'Marvelite' goes beyond just MarvelAPI, as it is also able to access information from the internet if required. It can also handle complex questions that go beyond just simple URL generation. This MarvelBot can take in complex queries beyond a rigid format of "Who is?/What is?/When did?" type of questions and can dive deeper into the information available in MarvelAPI, including understanding of context.

