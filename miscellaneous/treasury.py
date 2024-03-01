import pandas as pd
import requests

session = requests.Session()
session.headers.update(
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})

url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'
response = session.get(url, verify=False)

data = pd.read_html(response.text)[1]
data = data.melt(id_vars='Date', var_name='maturity')
data['Date'] = pd.to_datetime(data['Date'])

data.to_csv('treasury yield curve rates.csv', index=False)
