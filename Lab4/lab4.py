import urllib.request
import requests
import threading
import json

import random

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val1 ="L3-T-2"
    val2="sunjeevanipujari@cmail.carleton.ca"
    val3 = "b"
    URl='https://api.thingspeak.com/update?api_key='
    KEY=' AT68QYQ94MQEWXL3'
    HEADER='&field1={}&field2={}&field3{}'.format(val1,val2,val3)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    
if __name__ == '__main__':
    thingspeak_post()
