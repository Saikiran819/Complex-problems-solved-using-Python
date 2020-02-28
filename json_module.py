import json
import requests


with open('Sample-JSON-file-with-multiple-records-download.json') as f:
    dat = json.load(f)

for key in dat['users']:
    del key['userId']
    del key['lastName']
    
with open('data.json', 'w') as g:
    json.dump(dat, g, indent = 2)
    
users_string = '''
{
  "users": [
    {
      "firstName": "Krish",
      "phoneNumber": "123456",
      "emailAddress": "krish.lee@learningcontainer.com"
    },
    {
      "firstName": "racks",
      "phoneNumber": "123456",
      "emailAddress": "racks.jacson@learningcontainer.com"
    },
    {
      "firstName": "denial",
      "phoneNumber": "33333333",
      "emailAddress": "denial.roast@learningcontainer.com"
    },
    {
      "firstName": "devid",
      "phoneNumber": "222222222",
      "emailAddress": "devid.neo@learningcontainer.com"
    },
    {
      "firstName": "jone",
      "phoneNumber": "111111111",
      "emailAddress": "jone.mac@learningcontainer.com"
    }
  ]
}
'''

dat2 = json.loads(users_string)

for person in dat2['users']:
    del person['emailAddress']
dat2_string = json.dumps(dat2, indent = 2)

print(dat2_string)


src = requests.get('https://api.github.com/users/mralexgray/repos').text

data = json.loads(src)
dat3_str = json.dumps(data, indent = 2)

for item in data:
    if 'id' in item.keys():
        print(item['id'], end = '\t')
    if 'html_url' in item.keys():
        print(item['html_url'], end = '\n')