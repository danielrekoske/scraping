import re
import json
import pandas as pd
import requests

session = requests.Session()
session.headers.update(
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})

url = 'https://www.macrotrends.net/stocks/charts/AAPL/apple/financial-statements'
response = session.get(url)

num = re.findall('(?<=div\>\"\,)[0-9\.\"\:\-\, ]*', response.text)
text = re.findall('(?<=s\: \')\S+(?=\'\, freq)', response.text)
dicts = [json.loads('{' + i + '}') for i in num]

df = pd.DataFrame()
for ind, val in enumerate(text):
    df[val] = dicts[ind].values()
df.index = dicts[ind].keys()

df.to_csv('aapl financial statements.csv')
