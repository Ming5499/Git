import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" :  "+1 132 323 402"
        
},
    "email" : {
    "hide" : "yes"
    }
}'''

info = json.loads(data)
print(info)
print('Name: ', info['name'])
print('Hide: ',info['email']['hide'])

#################################################################
input = '''[
    {"id" : "01",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "02",
    "x" : "7",
    "name" : "Chuck"
}]
'''

info = json.loads(input)
print('User count: ',len(info))
for item in info:
    print('Name: ',item['name'])
    print('ID: ',item['id'])
    print(('Attribute: ',item['x']))