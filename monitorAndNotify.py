import time
import datetime

# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
from db_handler import Database
from compare import Compare             # A utility class used to compare temp and humid
from notify_bullet import BulletNotice  # A utility class used to send bullet notification

sample_freq = 1 # time in seconds

def main():
    # Initiate all the necessary database and utilities
    detector = SHDetector()
    database = Database()
    compare = Compare()
    notice = BulletNotice()

    database.create_dbtable()   # create sqlite3 db file if not existing, plus tables
    num_of_notice = 0       # record of notification sent today
    # print(database.check_status_exist())

    database.save_daily_data('OK')

    for _ in range(0, 5):
        detector.getSenseData()
        database.save_dbdata(detector.time, detector.temp, detector.humid)
        status = compare.compare_data(detector.temp, detector.humid)
        print("status is " + status)

        if status != "OK" and num_of_notice < 1:
            print("num_of_notice = " + str(num_of_notice) )
            database.update_daily_data(status)
            notice.send_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status)
            num_of_notice += 1

        time.sleep(sample_freq)
    
    database.read_dbdata()
    database.read_daily_data()

    database.clear_dbdata()         # Uncomment this line if what to clear dumy data
    database.clear_daily_data()     # Uncomment this line if what to clear dumy data
    
main()