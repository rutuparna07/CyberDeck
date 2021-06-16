from virustotal_python import Virustotal
from base64 import urlsafe_b64encode
from pprint import pprint
import json
import requests

key="<VTAPI_KEY>"
vtotal = Virustotal(API_KEY=key, API_VERSION="v3")

def filescan(FILE_ID):
    #Retrieve information about a file
    resph = vtotal.request(f"files/{FILE_ID}")
    data = json.loads(json.dumps(resph.data))
    a = "Original name: ", data['attributes']['signature_info']['original name']
    b = "Size (in Byte): ",data['attributes']['size']
    if data['attributes']['total_votes']['malicious'] > 0 :
        return (print(a,b,str('File is MALICIOUS')))
    else:
        return (print(a,b,str('File is HARMLESS')))

# The ID (either SHA-256, SHA-1 or MD5) identifying the file
filescan("<Enter FILE ID>")

#URLScan Report
def urlscan(url):
    params = {'apikey': '<VTAPI_KEY>', 'resource':'https://pypi.org/project/virustotal-python/'}
    response = requests.get(url, params=params)
    report = json.loads(json.dumps(response.json()))
    if report['positives'] > 3:
        return(print("URL:"+report['url']+"\nSTATUS: MALICIOUS\nHas"+report['positives']+" out of"+report['total']+"scans positive."))
    elif report['positives'] > 0 and report['positives'] <= 3:
        return(print("URL:"+report['url']+"\nSTATUS: MAYBE MALICIOUS"))
    else:
        return(print("URL:"+report['url']+"\nSTATUS: NOT MALICIOUS"))

urlscan("<Enter URL>")

