import time
import sqlite3 as lite
# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
import os

dbname = 'sensedata.db'
sample_freq = 1 # time in seconds

def main():
    detector = SHDetector()

    if(not(os.path.isfile('./' + dbname))):
        create_dbtable()

    for _ in range(0, 3):
        detector.getSenseData()
        save_dbdata(detector.time, detector.temp, detector.humid)
        time.sleep(sample_freq)
    
    read_dbdata()

def create_dbtable():
    with lite.connect(dbname) as conn:
        curs = conn.cursor()
        curs.execute("DROP TABLE IF EXISTS TEMP_HUMID")
        curs.execute("CREATE TABLE TEMP_HUMID(timestamp DATETIME, temp NUMERIC, humid NUMERIC)")
        conn.commit()

def save_dbdata(time, temp, humid):
    with lite.connect(dbname) as conn:
        curs = conn.cursor()
        curs.execute("INSERT INTO TEMP_HUMID (timestamp, temp, humid) values(datetime('now', 'localtime'), (?), (?))", (temp, humid))
        conn.commit()
    
def read_dbdata():
    print("Read all content from Database " + dbname)
    with lite.connect(dbname) as conn:
        curs = conn.cursor()
        results = curs.execute("SELECT * FROM TEMP_HUMID")
        for row in results:
            print(row)
                

main()