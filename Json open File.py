import json

with open('dc.json') as f:
    data = json.load(f)

for contato in data['contacts']:
    del contato['address']

with open('novoContatos.json', 'w') as f:
    json.dump(data, f, indent = 2)

##with open('dc.json') as f:
##    data = json.load(f)

for contato in data['contacts']:
    print('id:', contato['id'], 'nome:', contato['name'])

