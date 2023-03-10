import requests
import argparse

MEDICAL_CONTEXT = "We are a committee of leading scientific experts and medical doctors reviewing the latest and highest quality of research from PubMED."\
                  "For each question, we have chosen an answer, either 'yes' or 'no', based on our best understanding of current medical practice and literature." 
## we have seen through experimentation that giving this specific context (Pradeep et al. 2022) enhances the accuracy of GPT-3 models for answering medical questions

'''
This function wraps user's petition/medical question with the adequate context to better orient the response of the language model
'''
def wrapper(query:str, key: str, model:str) -> str:
    url = 'https://api.openai.com/v1/completions'
    headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+key}
    myobj = {'model': model, 'prompt': MEDICAL_CONTEXT + " \"" + query+ "\". The answer must be Yes or No.", "max_tokens":256, "temperature":0} # temperature is set to 0 by default since we want the most deterministic as possible responses
                                                                                                                   # max_tokens = 256 because we want a concrete explanation, better if it yes or no

    x = requests.post(url, headers =headers, json = myobj)
    
    return x.json()['choices'][0]['text']

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='medical query we want to ask to GPT-3 models')
    parser.add_argument('api_key')
    parser.add_argument('model', nargs='?', default='text-davinci-003')
    args = parser.parse_args()
    response = wrapper(args.query, args.api_key, args.model)
    print("GPT-3 says: ", response)