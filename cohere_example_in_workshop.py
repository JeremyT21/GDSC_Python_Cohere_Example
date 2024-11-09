import cohere
from api_key_file import API_KEY

'''
You could just put your API key in this file as a string,
and set API_KEY = "Chjj21kb..."

Since I am presenting this code I put API_KEY
in a different python file so
not everyone can see my API key.
'''

#Initialize cohere's AI platform as a variable:
co = cohere.Client(API_KEY)

response = co.generate(model='command',prompt="What is the most googled thing?",max_tokens=25) #Common words count as one token, this model will have a limit of 25 words.
print(response.generations[0].text) #Return the response generated from the cohere 'command' model.