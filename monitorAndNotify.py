# Use the following line if only need to run on Pi
# from sense_hat import SenseHat    
from virtual_sense_hat import VirtualSenseHat
import datetime

sense = VirtualSenseHat.getSenseHat()

time = datetime.datetime.now()
temp = sense.get_temperature()
humid = sense.get_humidity()

print('DateTime: ' + str(time) + ' | Temp: {0:0.1f}'.format(temp) + ' | Humidity: {0:0.0f}'.format(humid))
sense.clear()
