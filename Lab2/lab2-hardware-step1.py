"""
SYSC 3010 A Lab 2 step 1 
Sunjeevani Pujari 
L3-T-2 
101110032
"""
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()


sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the actionkey (joystick) was pressed
    if event.action == "pressed":
        sense.show_letter("S") 
        sleep(2)
        sense.clear()
        sense.show_letter("P") 
        sleep(2)
        sense.clear()
        event.action == "pressed"
      
      
