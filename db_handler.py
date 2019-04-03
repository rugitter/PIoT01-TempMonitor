import sqlite3 as lite
import datetime

class Database():
    def __init__(self):
        self.dbname = 'sensedata.db'
        self.today_date = datetime.datetime.today().strftime("%Y-%m-%d")

    def create_dbtable(self):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("CREATE TABLE TEMP_HUMID(timestamp DATETIME, temp NUMERIC, humid NUMERIC)")
            curs.execute("CREATE TABLE DAILY_REPORT(datestamp DATE, status STRING)")
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

    def save_daily_data(self, status):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO DAILY_REPORT(datestamp, status) values(date('now', 'localtime'), (?))", (status,))
            conn.commit()
    
    def update_daily_data(self, status):
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            
            curs.execute("UPDATE DAILY_REPORT SET status = (?) WHERE datestamp = (?)", (status, self.today_date))
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
    
    def clear_daily_data(self):
        print("Delete all records in the table DAILY_REPORT!")
        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("DELETE FROM DAILY_REPORT")
            conn.commit()

    # Check if today's status exists in the daily report database
    def check_status_exist(self):
        

        with lite.connect(self.dbname) as conn:
            curs = conn.cursor()
            curs.execute("SELECT * FROM DAILY_REPORT WHERE datestamp = (?) LIMIT 1", (self.today_date,))
            rs = curs.fetchone()

            if rs == None:
                print("Record not exist!")
                return False
                # results = curs.execute("SELECT * FROM DAILY_REPORT WHERE datestamp = (?) LIMIT 1", (today_date,))
                # for row in rs:
                #     status = row[1]
                #     print(status)
            else:
                print("Record exist!")
                return True