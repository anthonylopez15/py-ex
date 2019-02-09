import json
contact_string = '''
{
    "contacts": [
        {
                "id": "c200",
                "name": "Ravi Tamada",
                "email": "ravi@gmail.com",
                "address": "xx-xx-xxxx,x - street, x - country",
                "gender" : "male",
                "phone": {
                    "mobile": "+91 0000000000",
                    "home": "00 000000",
                    "office": "00 000000"
                }
        },
        {
                "id": "c209",
                "name": "Clint Eastwood",
                "email": "clint_eastwood@gmail.com",
                "address": "xx-xx-xxxx,x - street, x - country",
                "gender" : "male",
                "phone": {
                    "mobile": "+91 0000000000",
                    "home": "00 000000",
                    "office": "00 000000"
                }
        }
    ]
}'''

#data = json.loads(contact_string)

#for contacts in data['contacts']:
#    print('email:', contacts['email'], 'Genero:', contacts['gender'])
    #print(contacts['id'])
    #del contacts['address']

#novoString = json.dumps(data, indent = 2, sort_keys = True)
#print(novoString)

    
