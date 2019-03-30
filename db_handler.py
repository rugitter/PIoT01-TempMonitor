import sqlite3 as lite
import os

class Database():
    def __init__(self):
        self.dbname = 'sensedata.db'

    def create_dbtable(self):
        if(not(os.path.isfile('./' + self.dbname))):
            with lite.connect(self.dbname) as conn:
                curs = conn.cursor()
                curs.execute("DROP TABLE IF EXISTS TEMP_HUMID")
                curs.execute("CREATE TABLE TEMP_HUMID(timestamp DATETIME, temp NUMERIC, humid NUMERIC)")
                conn.commit()

    def save_dbdata(self, time, temp, humid):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO TEMP_HUMID (timestamp, temp, humid) values(datetime('now', 'localtime'), (?), (?))", (temp, humid))
            conn.commit()
        
    def read_dbdata(self):
        print("Read all content from Database " + self.dbname)
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            results = curs.execute("SELECT * FROM TEMP_HUMID")
            for row in results:
                print(row)