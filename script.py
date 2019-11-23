import json
import requests
import urllib
import time 


PWNED_API_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/"

headers = {"hibp-api-key": "58779e4f5a4d427a9cb3175dcc3b3f58"}

values = []

lines = []

infile = [line.rstrip('\n') for line in open('emails-2.txt')]
data = []

for line in infile:
    encoded = urllib.parse.quote(line) 
    lines.append(encoded)

#request = requests.get(PWNED_API_URL + "garytinnin%40gmail.com", headers=headers)

#print(request.json())
#print(PWNED_API_URL + "garytinnin%40gmail.com")

#print(lines)


for email in lines:
    json_data = requests.get(PWNED_API_URL + email , headers=headers) 
    response = json_data
    print(email + ":" + response.text) 
    time.sleep(1.6)
    #results = json_data.json()
    #data.append(results) 



