from virustotal_python import Virustotal
from base64 import urlsafe_b64encode
from pprint import pprint
import json
import requests

key="79b779e9144d245d8749425a7bc1bf098c53d57a0405b56ad5fcd005f2faab2c"
vtotal = Virustotal(API_KEY=key, API_VERSION="v3")

#Retrieve information about a file
# The ID (either SHA-256, SHA-1 or MD5) identifying the file
FILE_ID = "A761FFF1A260750946A5E87C0AEE4EF3"

# v3 example
resph = vtotal.request(f"files/{FILE_ID}")
data = json.loads(json.dumps(resph.data))
print("Original name: ", data['attributes']['signature_info']['original name'])
print("Size (in Byte): ",data['attributes']['size'])
if data['attributes']['total_votes']['malicious'] > 0 :
    print('File is MALICIOUS')
else:
    print('File is HARMLESS')

print("\n###########################################################\n")

#URLScan Report
url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': '79b779e9144d245d8749425a7bc1bf098c53d57a0405b56ad5fcd005f2faab2c', 'resource':'https://pypi.org/project/virustotal-python/'}
response = requests.get(url, params=params)
report = json.loads(json.dumps(response.json()))
if report['positives'] > 3:
    print("URL:"+report['url']+"\nSTATUS: MALICIOUS")
    print("Has"+report['positives']+" out of"+report['total']+"scans positive.")
elif report['positives'] > 0 and report['positives'] <= 3:
    print("URL:"+report['url']+"\nSTATUS: MAYBE MALICIOUS")
else:
    print("URL:"+report['url']+"\nSTATUS: NOT MALICIOUS")




