# Smarty-GPT: library of prompts/contexts

This is a simple wrapper that introduces any imaginable complex context to each question submitted to Open AI API. The main goal is to enhance the accuracy obtained in its answers **in a transparent way to end users**. 

This idea arose in the context of a health-related experiment lead by CiTIUS.(**more coming soon**).

## Contexts / Prompts

The current prompts give extra context to the GPT model and allow them to answer as a *doctor*, *programmer*, or *lawyer*. The end user only needs to select the desired context and they can directly *ask the question as they will do with a normal search engine*!

Example:

```bash
$ python smarty-gpt.py "Will wearing an ankle brace help heal an ankle fracture?" "doctor" "xxxxxxxxxxxxxxxxx"
Smarty-GPT says:
No. Wearing an ankle brace may help to provide support and stability to the ankle while it is healing, but it will not directly help to heal the fracture.
```

or 

```bash
$ python smarty-gpt.py "When do I need a solicitor?" "lawyer" "xxxxxxxxxxxxxxxxxxxxx"
Smarty-GPT says:
It depends on the situation. Generally, you should consult a solicitor if you are involved in a legal dispute, need advice on a legal matter, or need help drafting a legal document. You may also need a solicitor if you are buying or selling a property, making a will, or dealing with a family law matter.
```

## Installation and execution (**in progress, not definitive**)

```bash
$ git clone git@github.com:citiususc/gpt-3-medical-wrapper.git

$ pip install -r requirements.txt

[for the moment] $ python smarty-gpt.py query [doctor|lawyer|programmer] key
```

## Prompts / Contexts

More prompts are about to come! (Jailbreaks, etc.). Feel free to make a PR or to contact me at marcosfernandez.pichel@usc.es



## Pypi (in progress)
