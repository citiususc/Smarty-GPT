# Smarty-GPT: library of prompts/contexts (**connected with Awesome Prompts Chat GPT**)

This is a simple wrapper that introduces any imaginable complex context to each question submitted to Open AI API. The main goal is to enhance the accuracy obtained in its answers in a **TRANSPARENT** way to end users. 

This idea arose in the context of a health-related experiment lead by CiTIUS.(**more coming soon**).

## Contexts / Prompts

The current prompts give extra context to the GPT model and allow them to answer as a *doctor*, *programmer*, or *lawyer*. The end user only needs to select the desired context and they can directly *ask the question as they will do with a normal search engine*! More manual prompts are welcomed!

We have also connected this tool with the [Awesome ChatGPT Prompts dataset](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts) and [repo](https://github.com/f/awesome-chatgpt-prompts) from Fatih Kadir Akın. 

Our purpose is to connect all this data with the API and make the proccess **fully transparent** to the end user.

## Installation 

```bash
$ pip install smarty-gpt==1.0.3
```
## Example

```python
from smartygpt import Wrapper
wrapper = Wrapper()
wrapper.wrapper("Can ibuprofen worsen COVID-19?", "INSERT-YOUR-OPENAI-KEY-HERE", "doctor")
```

## Prompts / Contexts

More prompts are about to come! (Jailbreaks, etc.). Feel free to make a PR or to contact me at marcosfernandez.pichel@usc.es
