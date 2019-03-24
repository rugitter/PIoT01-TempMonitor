import time
import sqlite3 as lite
# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sensehat import SenseHat           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file

dbname = 'sensedata.db'
sample_freq = 1 # time in seconds

def main():
    sense = SenseHat()
    create_dbtable()

    for i in range(0, 3):
        sense.getSenseData()
        save_dbdata(sense.time, sense.temp, sense.humid)
        time.sleep(sample_freq)
    
    read_dbdata()

def create_dbtable():
    conn = lite.connect(dbname)
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS TEMP_HUMID")
    curs.execute("CREATE TABLE TEMP_HUMID(timestamp DATETIME, temp NUMERIC, humid NUMERIC)")
    conn.commit()
    conn.close()

def save_dbdata(time, temp, humid):
    conn = lite.connect(dbname)
    curs = conn.cursor()
    curs.execute("INSERT INTO TEMP_HUMID values(datetime('now'), (?), (?))", (temp, humid))
    conn.commit()
    conn.close()
    
def read_dbdata():
    print("Read all content from Database " + dbname)
    conn = lite.connect(dbname)
    curs = conn.cursor()
    results = curs.execute("SELECT * FROM TEMP_HUMID")
    for row in results:
        print(row)
    conn.close()
                

main()