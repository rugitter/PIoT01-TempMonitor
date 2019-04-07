from virtual_sense_hat import VirtualSenseHat
import datetime
import sqlite3

class SHDetector:
    def __init__(self):
        self.sense = VirtualSenseHat.getSenseHat()
    
    # Accessor
    # Get time in the format of 2019-03-30 14:04:05 - Melbouren local time
    def getTime(self):
        return self.time.strftime("%Y-%m-%d %H:%M:%S")
    
    def getTemp(self):
        return self.temp
    
    def getHumid(self):
        return self.humid

    def getSenseData(self):
        self.sense.clear()
        self.time = datetime.datetime.now()

        self.temp = round(self.sense.get_temperature(), 1)
        self.humid = round(self.sense.get_humidity())
        # If not connected Pi device, will print out on console
        self.sense.show_message('T:{0:0.1f} '.format(self.temp) + 
            'H:{0:0.0f}'.format(self.humid), scroll_speed=0.05)

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