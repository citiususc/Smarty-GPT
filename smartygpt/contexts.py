#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datasets import load_dataset

def available_contexts():
    print("-> Manually introduced:", list(ManualContexts.__dict__.keys())[1:][:-3])
    print("-> Awesome Prompts library:", AwesomePrompts.dataset['act'])
    print("-> Plus custom prompts introduced by file...")

class ManualContexts:
    DoctorAdvice = "We are a committee of leading scientific experts and medical doctors reviewing the latest and highest quality of research from PubMED."\
                   "For each question, we have chosen an answer, either 'yes' or 'no', based on our best understanding of current medical practice and literature." 
                   #### taken from (Pradeep et al. 2022)
    SickAdvice = "We are a non-expert user searching for medical advice online."
    Lawyer = "You are a lawyer specialised in Spanish criminal code issues. Respond appropriately to the question posed as if you were being asked by a potential client."

    Programmer = "Act as a skillfull senior programmer and report the errors present in this code:" 

class AwesomePrompts: ##### We have included here the collection of prompts from this repository: https://github.com/f/awesome-chatgpt-prompts
   data = load_dataset("fka/awesome-chatgpt-prompts")
   dataset = data["train"]

class CustomPrompt:

    def __init__(self, path, name):
        with open(os.path.join(path+'custom_prompts/', name), 'r') as f:
            prompt_text = f.read().strip()
        
        self.prompt = prompt_text
        
        
