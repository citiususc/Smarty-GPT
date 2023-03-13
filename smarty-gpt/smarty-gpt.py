import requests
import argparse
from contexts import Contexts

'''
This function wraps user's petition question with the adequate context to better orient the response of the language model
'''
def wrapper(query:str, key: str, context:str, model:str) -> str:
    url = 'https://api.openai.com/v1/completions'
    headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+key}
    if context=="doctor":
        context = Contexts.DoctorAdvice
    elif context=="layer":
        context = Contexts.Lawyer
    elif context=="programmer":
        context = Contexts.Programmer

    myobj = {'model': model, 'prompt': context + " \"" + query+ "\"", "max_tokens":256, "temperature":0} # temperature is set to 0 by default since we want the most deterministic as possible responses
                                                                                                                   # max_tokens = 256 because we want a concrete explanation, better if it yes or no

    x = requests.post(url, headers =headers, json = myobj)
    
    return x.json()['choices'][0]['text']

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='simple query we will ask to the model as end-user')
    parser.add_argument('context', choices=["doctor", "lawyer", "programmer"])
    parser.add_argument('api_key')
    parser.add_argument('model', nargs='?', default='text-davinci-003')
    args = parser.parse_args()
    response = wrapper(args.query, args.api_key, args.context, args.model)
    print("Smarty-GPT says: ", response)