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


key = "1M7JWFZ8UKMOEC9C"  # Put your API Key here
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = random.randint(90,150) #int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 Get Raspberry Pi CPU temp
        params = urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (str(temp))
            print (str(response.status), str(response.reason))
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()
