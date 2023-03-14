import requests
import argparse
from .contexts import Contexts

'''
This function wraps user's petition question with the adequate context to better orient the response of the language model
'''

class Wrapper:

    def wrapper(self, query:str, key: str, context:str, model:str="text-davinci-003") -> str:
        if not any(context==x for x in ["doctor", "lawyer", "programmer"]):
            raise Exception("Sorry, that context is not implemented yet")

        url = 'https://api.openai.com/v1/completions'
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+key}
        if context=="doctor":
            context = Contexts.DoctorAdvice
        elif context=="lawyer":
            context = Contexts.Lawyer
        elif context=="programmer":
            context = Contexts.Programmer

        myobj = {'model': model, 'prompt': context + " \"" + query+ "\"", "max_tokens":256, "temperature":0} # temperature is set to 0 by default since we want the most deterministic as possible responses
                                                                                                                    # max_tokens = 256 because we want a concrete explanation, better if it yes or no

        x = requests.post(url, headers =headers, json = myobj)
        
        return x.json()['choices'][0]['text']