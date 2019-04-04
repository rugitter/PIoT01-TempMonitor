import time
import datetime
import os

# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
from db_handler import Database
from compare import Compare             # A utility class used to compare temp and humid
from notify_bullet import BulletNotice  # A utility class used to send bullet notification

class Monitor:
    def __init__(self):
        # Initiate all the necessary database and utilities
        self.detector = SHDetector()
        self.notice = BulletNotice()
        self.compare = Compare()
        self.database = Database()

        self.dbname = 'sensedata.db'
        self.sample_freq = 1 # time in seconds, change to 60 for pi
        self.num_of_notice = 0       # record of notification sent today

        if(not(os.path.isfile('./' + self.dbname))):
            self.database.create_dbtable()   # create sqlite3 db file if not existing, plus tables

    def main(self):
        # print(database.check_status_exist())
        # Pre-save a "OK" status as today's status record in the DAILY_REPORT table
        self.database.save_daily_data('OK')

        for _ in range(0, 3):
            self.detector.getSenseData()
            monitor_time = self.detector.getTime()
            temp = self.detector.getTemp()
            humid = self.detector.getHumid()

            status = self.compare.compare_data(temp, humid)
            print("status is " + status)

            # Save the monitored temperature and humidity with current time to DB - TEMP_HUMID table
            self.database.save_dbdata(monitor_time, temp, humid)
            
            # If monitored temp or humid exceed the boundary, and for the 1st time of the day
            # Save the calculated status to DB - DAILY_REPORT table
            if status != "OK" and self.num_of_notice < 1:
                print("num_of_notice = " + str(self.num_of_notice) )
                self.database.update_daily_data(status)
                self.notice.send_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status)
                self.num_of_notice += 1

            time.sleep(self.sample_freq)

        self.database.read_dbdata()
        self.database.read_daily_data()

        # self.database.clear_dbdata()         # Uncomment this line if what to clear dumy data
        # self.database.clear_daily_data()     # Uncomment this line if what to clear dumy data

if __name__ == "__main__":
    monitor = Monitor()
    monitor.main()