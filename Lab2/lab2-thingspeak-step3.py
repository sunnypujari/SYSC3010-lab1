import http.client
import urllib
import time
import random 
import urllib.request
from urllib import request
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus
import json 
#import requests
import threading

READ_API_KEY = "1M7JWFZ8UKMOEC9C"
CHANNEL_ID = "1178424"

def main():
    t = urllib.request.urlopen('https://api.thingspeak.com/channels/1178424/feeds.json?api_key=URSD604HKXN9F8SB&results=4')
    response = t.read()
    data=json.loads(response)  
    a = data['field1']
    print (a)
    t.close()

if __name__== '__main__':
    main()