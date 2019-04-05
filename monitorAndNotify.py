import time
import datetime
import os

# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector      # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
from db_handler import Database         # A utility class to handle all db operations
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

        if(not(os.path.isfile('./' + self.dbname))):
            self.database.create_dbtable()   # create db and tables if db file not existing

    def main(self):
        # Check if today's status alreay exist in DAILY_REPORT DB, and return
        # 0 - if not exist, 1 - if exist and is OK, 2 - if exist and is BAD
        status_num = self.database.check_status_exist()     
        if status_num == 0:         # If status not exists, pre-save a "OK" as today's status
            self.database.save_daily_data('OK')

        # for _ in range(0, 5):
        self.detector.getSenseData()
        monitor_time = self.detector.getTime()
        temp = self.detector.getTemp()
        humid = self.detector.getHumid()

        status = self.compare.compare_data(temp, humid)   # defect code exists here
        self.detector.sense.show_message("Status:" + status, scroll_speed=0.05)

        # Save the monitored temperature and humidity with current time to DB - TEMP_HUMID table
        self.database.save_dbdata(monitor_time, temp, humid)
        self.detector.sense.show_message("DBSaved", scroll_speed=0.05)
        
        # If exceed boundary - status is bad, 
        # and current saved status in DB is OK,
        # then update status in DB and send notification (once per day)
        if status != "OK" and status_num == 1:
            self.database.update_daily_data(status)
            self.detector.sense.show_message("DBUpdated", scroll_speed=0.05)
            self.notice.send_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status)

        # self.database.read_dbdata()
        # self.database.read_daily_data()

        # self.database.clear_dbdata()         # Uncomment this line if what to clear dumy data
        # self.database.clear_daily_data()     # Uncomment this line if what to clear dumy data

if __name__ == "__main__":
    monitor = Monitor()
    monitor.main()
