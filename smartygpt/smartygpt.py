import requests
import argparse
import os 
from nltk import sent_tokenize
from .contexts import ManualContexts, AwesomePrompts, CustomPrompt
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.core.config import Config
import subprocess
import time
import signal


'''
This function wraps user's petition question with the adequate context to better orient the response of the language model
'''

class Wrapper:

    def __init__(self):
        self.login = None

    def wrapper(self, query:str, context:str, model:str="text-davinci-003", key: str=None) -> str:
        ##### Contexts
        
        contexts = AwesomePrompts.dataset['act']
        contexts.extend(["doctor", "lawyer", "programmer", "sick"])
        contexts.extend(CustomPrompt.available_prompts)
        if not any(context==x for x in contexts):
            raise Exception("Sorry, that context is not implemented yet")
        if context=="doctor":
            context = ManualContexts.DoctorAdvice
        elif context=="lawyer":
            context = ManualContexts.Lawyer
        elif context=="programmer":
            context = ManualContexts.Programmer
        elif context=="sick":
            context = ManualContexts.SickAdvice
        elif context.startswith('custom-'):
            custom_name = context[len('custom-'):]
            context = CustomPrompt(custom_name).prompt
        else:
            context = AwesomePrompts.dataset.filter(lambda x: x['act']==context)['prompt'][0]
            context = ' '.join(sent_tokenize(context)[:-1])

        ### Models
        if model=="flant5":
            model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
            tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
            inputs = tokenizer(context + " \"" + query+ "\"", return_tensors="pt")
            outputs = model.generate(**inputs)
            response = tokenizer.batch_decode(outputs, skip_special_tokens=True)
            response = response[0].lower()       
            return response

        elif model=="chatgpt" or model=="gpt4":
            if not self.login: #### Mandatory login from chatgpt-wrapper
                self.login = subprocess.run(["chatgpt", "install"])
            
            print("The response to:", query, "is generating...")
            if model=="chatgpt":
                bot = ChatGPT()
                _, response, _ = bot.ask(context + " \"" + query)
            elif model=="gpt4":
                config = Config()
                config.set('chat.model', 'gpt4')
                bot = ChatGPT(config)
                _, response, _ = bot.ask(context + " \"" + query)

            return response            
            
        else:
            url = 'https://api.openai.com/v1/completions'
            headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+key}
            myobj = {'model': model, 'prompt': context + " \"" + query+ "\"", "max_tokens":256, "temperature":0} # temperature is set to 0 by default since we want the most deterministic as possible responses
                                                                                                                        # max_tokens = 256 because we want a concrete explanation, better if it yes or no

            x = requests.post(url, headers =headers, json = myobj)
            
            return x.json()['choices'][0]['text']   
