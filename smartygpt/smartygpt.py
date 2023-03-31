import requests
import openai
from nltk import sent_tokenize
from .contexts import *
from .models import Models
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import configparser



class SmartyGPT:

    def __init__(self, model=Models.GPT3, prompt=ManualContexts.DoctorAdvice):
        self.model = model
        config = configparser.RawConfigParser()
        config.read('~/config.txt')
        config_details = config.get_config_dict()
        self.api_key = config_details['API_KEY'] 
        if isinstance(prompt, ManualContexts):
            self.prompt = prompt   
        elif isinstance(prompt, AwesomePrompts):
            context = AwesomePrompts.dataset.filter(lambda x: x['act']==prompt)['prompt'][0]
            context = ' '.join(sent_tokenize(context)[:-1])
            self.prompt = context
        else:
            custom_name = prompt[len('custom-'):]
            context = CustomPrompt(custom_name).prompt
            self.prompt = context

    def change_context(prompt):
        self.prompt = prompt
    
    def get_context(prompt):
        return self.prompt

    '''
    This function wraps user's petition question with the adequate context 
    to better orient the response of the language model
    '''
    def wrapper(self, query:str) -> str:

        ### Models
        if self.model==Models.FlanT5:
            model = AutoModelForSeq2SeqLM.from_pretrained(Models.FlanT5)
            tokenizer = AutoTokenizer.from_pretrained(Models.FlanT5)
            inputs = tokenizer(self.prompt + " \"" + query+ "\"", return_tensors="pt")
            outputs = model.generate(**inputs)
            response = tokenizer.batch_decode(outputs, skip_special_tokens=True)
            response = response[0].lower()       
            return response

        elif self.model==Models.GPT3:
            openai.api_key= self.api_key
            response = openai.Completion.create(
                engine=self.model,
                prompt=self.prompt + query,
                temperature=0,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            response = response['choices'][0]['text']+'\n'
            response = response.lower()
            return response            
            
        elif self.model==Models.ChatGPT or self.model==Models.GPT4:
            openai.api_key=self.api_key
            response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": self.prompt+query},
            ]
            )
            response = response['choices'][0]['text']+'\n'
            return response
