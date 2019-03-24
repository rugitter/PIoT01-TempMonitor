from virtual_sense_hat import VirtualSenseHat
import datetime
import sqlite3

class SenseHat():
    time = None
    temp = None
    humid = None
    sense = None

    def __init__(self):
        self.sense = VirtualSenseHat.getSenseHat()

    def getSenseData(self):
        self.sense.clear()
        self.time = datetime.datetime.now()
        self.temp = self.sense.get_temperature()
        self.humid = self.sense.get_humidity()
        self.sense.show_message('Temp: {0:0.1f}c'.format(self.temp) + 
        ' Humid: {0:0.0f}'.format(self.humid), scroll_speed=0.05)

    def logData(self):
        if( self.time and self.temp and self.humid):
            print('DateTime: {:%Y-%m-%d %H:%M:%S}'.format(self.time) + 
            ' | Temp: {0:0.1f}'.format(self.temp) + 
            ' | Humidity: {0:0.0f}'.format(self.humid))
        else:
            print('No sense data saved!')

# if temp is not None & humid is not None:
#     temp = round(temp, 1)
# sense.clear()