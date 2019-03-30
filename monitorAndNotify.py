import time

# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
from db_handler import Database

sample_freq = 1 # time in seconds

def main():
    detector = SHDetector()
    database = Database()

    database.create_dbtable()

    for _ in range(0, 3):
        detector.getSenseData()
        database.save_dbdata(detector.time, detector.temp, detector.humid)
        time.sleep(sample_freq)
    
    database.read_dbdata()                

main()