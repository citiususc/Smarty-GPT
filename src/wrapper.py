import requests

url = 'https://api.openai.com/v1/completions'
headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer sk-xxxxxxxxxxx"}
myobj = {'model': 'text-davinci-003', 'prompt': "Barack Obama was born in", "max_tokens":7, "temperature":0}

x = requests.post(url, headers =headers, json = myobj)

print(x.json())