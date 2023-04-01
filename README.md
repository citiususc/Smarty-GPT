# Smarty-GPT
## A wrapper of LLMs (chatgpt, gpt4, etc.) that biases its behaviour using prompts

<p align="center">
    <a href="https://pepy.tech/project/smarty-gpt/"><img alt="Downloads" src="https://img.shields.io/badge/dynamic/json?style=flat-square&maxAge=3600&label=downloads&query=$.total_downloads&url=https://api.pepy.tech/api/projects/smarty-gpt"></a>
    <a href="https://pypi.python.org/pypi/smarty-gpt/"><img alt="PyPi" src="https://img.shields.io/pypi/v/smarty-gpt.svg?style=flat-square"></a>
</p>

A wrapper of LLMs that biases its behaviour using prompts and contexts in a **transparent** manner to the end-users.

## Installation 

```bash
sh install.sh
```

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/citiususc/Smarty-GPT/HEAD?labpath=Demo.ipynb) [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/citiususc/Smarty-GPT/blob/master/Demo.ipynb) [![GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=citiususc/Smarty-GPT&machine=basicLinux32gb&location=WestEurope)


## Models

- **text-davinci-003**
- [**Flan-T5**](https://huggingface.co/google/flan-t5-small) powered by Google.
- **ChatGPT** and **GPT4** through paid API.

## Contexts / Prompts

We support three type of prompts from the moment:

- **Manual prompts**: these prompts are hard-coded and were the first included in this project.
- [**Awesome Chat GPT prompts**](https://github.com/f/awesome-chatgpt-prompts): our system also supports this huge HF dataset in a transparent manner.
- **Custom prompts**: any user can add custom prompts through a file.
- (In progress) Support for [**awesome-gpt4**](https://github.com/radi-cho/awesome-gpt4) prompts.


## Authentication

Users should create a *config.txt* file like the following to read Open AI bearer:

```txt
[auth]
api_key = xxxxxxxxxxxxxxxxxx
```

## Coding examples

```python
from smartygpt import SmartyGPT, Models
if __name__=="__main__":
    s = SmartyGPT(prompt="DoctorAdvice", config_file="/home/user/config.txt") 
    result = s.wrapper("Can Vitamin D cure COVID-19?")
    print(result)
```


Check the [**Colab**](https://colab.research.google.com/github/citiususc/Smarty-GPT/blob/master/Demo.ipynb) or test folder for more examples and functionalities

## Philosophy

The main purpose of this project is **joining** in a single environment all the resources (models, prompts, APIs, etc.) related to LLMs. 

Moreover, we also think from an **end-user** perspective. It is heavily unlikely that a user would introduce a complex context in a query to bias a model response. This library tries to solve this hidding the implementation details to end-users.

## In progress

More features/models are about to come! Feel free to make a PR, open an issue or to contact me at marcosfernandez.pichel@usc.es

## Disclaimer 

The software is provided "as is" and "with all faults" without warranties of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose and non-infringement. No warranty is provided that the software will be free from defects or that operation of the software will be uninterrupted. Your use of the software and any other material or services downloaded or made available to you through the software is at your own discretion and risk, and you are solely responsible for any potential damage resulting from their use.
