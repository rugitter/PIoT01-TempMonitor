from virtual_sense_hat import VirtualSenseHat
import datetime
import sqlite3

class SHDetector():
    # time = None   # Those are same to static variables in Java
    # temp = None
    # humid = None
    # sense = None

    def __init__(self):
        self.sense = VirtualSenseHat.getSenseHat()

    def getSenseData(self):
        self.sense.clear()
        self.time = datetime.datetime.now()

        self.temp = round(self.sense.get_temperature(), 1)
        self.humid = round(self.sense.get_humidity())
        # If not connected Pi device, will print out on console
        self.sense.show_message('Temp: {0:0.1f}c'.format(self.temp) + 
        ' Humid: {0:0.0f}'.format(self.humid), scroll_speed=0.05)

    # Not in use - Use to print data to Console
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