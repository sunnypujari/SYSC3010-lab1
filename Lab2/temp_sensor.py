"""
SYSC 3010 A Lab 2 step 3 emulator 
Sunjeevani Pujari 
L3-T-2 
101110032
"""

from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
sense.clear()

class TempSensor(object):
  
  def display_temp(t=0):
    temp = randint(96, 104)
    if temp > 100 :
      sense.show_message("Your body temp is higher than normal. Access Denied")
      sleep(5)
    elif temp <= 100 :
      sense.show_message("Your body temp is normal. Access Granted")
      sleep(5)
    else: 
      sense.show_message("Incorrect temp measurement")
  
