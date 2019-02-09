import json
from urllib.request import urlopen

linkUrl = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"

response = urlopen(linkUrl)
content = response.read()
response.close()

data = json.loads(content.decode("utf-8"))
name = ''
price = ''
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']

print(name, " - ", price)
    

'''print(json.dumps(data, indent = 2))

usd_rates = dict()


for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name, price)
    #usd_rates[name] = price
    
#print(50* float(usd_rates['USD/INR']))'''
