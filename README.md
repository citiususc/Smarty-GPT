# Smarty-GPT: wrapper of prompts/contexts (also ChatGPT and GPT4!)

This is a simple wrapper that introduces any imaginable complex context to each question submitted to a GPT or any other supported LM. The main goal is to enhance the accuracy obtained in its answers in a **TRANSPARENT** way to end users. 


## Installation 

```bash
pip install smarty-gpt==1.1.0
```

## Models

- *OpenAI API standard models*: **text-davinci-003**, **code-davinci-002**, **text-davinci-002**, etc.
- *Hugging Face Language Models*:like [**Flan-T5**](https://huggingface.co/google/flan-t5-small) powered by Google.
- *For ChatGPT Plus suscriptors*: **ChatGPT** and **GPT4** integration thanks to previous [projects](https://github.com/mmabrouk/chatgpt-wrapper).

## Contexts / Prompts

We support three type of prompts from the moment:

- **Manual prompts**: these prompts are hard-coded and were the first included in this project.
- [**Awesome Chat GPT prompts**](https://github.com/f/awesome-chatgpt-prompts): our system also supports this huge HF dataset in a transparent manner.
- **Custom prompts**: any user can add custom prompts through a file.

## Coding examples

```python
from smartygpt import Wrapper
wrapper = Wrapper()
wrapper.wrapper("Can ibuprofen worsen COVID-19?", "doctor", "text-davinci-003", "INSERT-YOUR-OPENAI-KEY-HERE") # manual prompt
wrapper.wrapper("Describe the attack of Pearl Harbor.", "custom-perplexity", "flant5") # custom prompt
wrapper.wrapper("Rap about Eminem", "Rapper", "chatgpt") # Awesome Chat GPT prompts 
wrapper.wrapper("Debate about the meaning of life", "Philosopher", "gpt4") # Awesome Chat GPT prompts 
```
**IMPORTANT!!!**: As it is not yet an official api, the first time "chatgpt" or "gpt4" models are called, a browser opens and asks for our *plus subscriber* credentials. Once logged in, we can close the generated prompt and the model will automatically respond and not ask for the credentials in the rest of the session.

## Purpose of the project

The main purpose of this project is **joining** in a single environment all the resources (models, prompts, APIs, etc.) related to LLMs. Moreover, we also think from an **end-user** perspective. It is heavily unlikely that a user would introduce a complex context in a query to a model or searcher. In this project, we try to bias the different model responses to answer in different ways/behaviors, but hidding this to end-users.

## In progress

More features/models are about to come! Feel free to make a PR, open an issue or to contact me at marcosfernandez.pichel@usc.es

## Disclaimer 

The software is provided "as is" and "with all faults" without warranties of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose and non-infringement. No warranty is provided that the software will be free from defects or that operation of the software will be uninterrupted. Your use of the software and any other material or services downloaded or made available to you through the software is at your own discretion and risk, and you are solely responsible for any potential damage resulting from their use.
