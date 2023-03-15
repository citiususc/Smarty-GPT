#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datasets import load_dataset

CURRENT_DIR = os.path.dirname(__file__)

class ManualContexts:
    DoctorAdvice = "We are a committee of leading scientific experts and medical doctors reviewing the latest and highest quality of research from PubMED."\
                   "For each question, we have chosen an answer, either 'yes' or 'no', based on our best understanding of current medical practice and literature." 
                   #### taken from (Pradeep et al. 2022)

    Lawyer = "You are a lawyer specialised in Spanish criminal code issues. Respond appropriately to the question posed as if you were being asked by a potential client."

    Programmer = "Act as a skillfull senior programmer and report the errors present in this code:" 

class AwesomePrompts: ##### We have included here the collection of prompts from this repository: https://github.com/f/awesome-chatgpt-prompts
   data = load_dataset("fka/awesome-chatgpt-prompts")
   dataset = data["train"]

class CustomPrompt:
    base_path = os.path.join(CURRENT_DIR, '..', 'custom_prompts')
    available_prompts = ['custom-{}'.format(p) for p in os.listdir(base_path)]

    def __init__(self, name):
        with open(os.path.join(self.base_path, name), 'r') as f:
            prompt_text = f.read().strip()
        
        self.prompt = prompt_text
        
        
