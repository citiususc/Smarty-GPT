import requests
import argparse
from .contexts import ManualContexts, AwesomePrompts

'''
This function wraps user's petition question with the adequate context to better orient the response of the language model
'''

class Wrapper:

    def wrapper(self, query:str, key: str, context:str, model:str="text-davinci-003") -> str:
        contexts = AwesomePrompts.dataset['act']
        contexts.extend(["doctor", "lawyer", "programmer"])
        if not any(context==x for x in contexts):
            raise Exception("Sorry, that context is not implemented yet")

        url = 'https://api.openai.com/v1/completions'
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+key}
        if context=="doctor":
            context = ManualContexts.DoctorAdvice
        elif context=="lawyer":
            context = ManualContexts.Lawyer
        elif context=="programmer":
            context = ManualContexts.Programmer
        else:
            context = AwesomePrompts.dataset.filter(lambda x: x['act']==context)['prompt'][0]
        myobj = {'model': model, 'prompt': context + " \"" + query+ "\"", "max_tokens":256, "temperature":0} # temperature is set to 0 by default since we want the most deterministic as possible responses
                                                                                                                    # max_tokens = 256 because we want a concrete explanation, better if it yes or no

        x = requests.post(url, headers =headers, json = myobj)
        
        return x.json()['choices'][0]['text']