# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sensehat import SenseHat           # Use this if run on both Pi and Computer
import datetime
import sqlite3

def main():
    sense = SenseHat()
    for x in range(0, 3):
        sense.getSenseData()
        sense.logData()

main()