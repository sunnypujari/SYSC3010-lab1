from sense_hat import SenseHat
from time import sleep
from temp_sensor import TempSensor
sense = SenseHat()
temp = TempSensor()
sense.clear()


sense.show_message("Press on action key to take temp measurement")
while True:
  for event in sense.stick.get_events():
    # Check if the actionkey (joystick) was pressed
    if event.action == "pressed":
        temp.display_temp()
        sleep(0.5)
        sense.clear()
        break
   
      
      
