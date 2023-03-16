# Smarty-GPT: wrapper of prompts/contexts 

This is a simple wrapper that introduces any imaginable complex context to each question submitted to Open AI API. The main goal is to enhance the accuracy obtained in its answers in a **TRANSPARENT** way to end users. 

This idea arose in the context of a health-related experiment lead by CiTIUS.(**more coming soon**).

## Contexts / Prompts

We support three type of prompts from the moment:

- **Manual prompts**: these prompts are hard-coded and were the first included in this project.
- [**Awesome Chat GPT prompts**](https://github.com/f/awesome-chatgpt-prompts): our system also supports this huge dataset in a transparent manner.
- **Custom prompts**: any user can add custom prompts through a file.

## Installation 

```bash
$ pip install smarty-gpt==1.0.4
```
## Example

```python
from smartygpt import Wrapper
wrapper = Wrapper()
wrapper.wrapper("Can ibuprofen worsen COVID-19?", "INSERT-YOUR-OPENAI-KEY-HERE", "doctor") # manual prompt
wrapper.wrapper("Describe the attack of Pearl Harbor.", "INSERT-YOUR-OPENAI-KEY-HERE", "custom-perplexity") # custom prompt
wrapper.wrapper("Rap about Eminem", "INSERT-YOUR-OPENAI-KEY-HERE", "Rapper") # Awesome Chat GPT prompts 
```

## Prompts / Contexts

More features/models are about to come! Feel free to make a PR, open an issue or to contact me at marcosfernandez.pichel@usc.es
