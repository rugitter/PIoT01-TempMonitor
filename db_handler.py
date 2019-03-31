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
                curs.execute("CREATE TABLE DAILY_REPORT(datestamp DATE, status STRING, msg STRING)")
                conn.commit()

    def save_dbdata(self, time, temp, humid):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO TEMP_HUMID (timestamp, temp, humid) values(datetime('now', 'localtime'), (?), (?))", (temp, humid))
            conn.commit()
        
    def read_dbdata(self):
        print("Read all content from Database " + self.dbname)
        my_list = []      # Create a list to return to outer method
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            results = curs.execute("SELECT * FROM TEMP_HUMID")

            for row in results:
                my_list.append(row)
                print(row)
        return my_list
    
    def clear_dbdata(self):
        print("Delete all records in the table TEMP_HUMID!")
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("DELETE FROM TEMP_HUMID")
            conn.commit()

    def save_daily_data(self, status, msg):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO DAILY_REPORT(datestamp, status, msg) values(date('now', 'localtime'), (?), (?))", (status, msg))
            conn.commit()
    
    def read_daily_data(self):
        print("Read daily report data")
        my_list = []    # Create a list to return to outer method
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            results = curs.execute("SELECT * FROM DAILY_REPORT")
                  
            for row in results:
                my_list.append(row)
        print(my_list)
        
        return my_list