import time

# from sense_hat import SenseHat        # Use this if only want to run on Pi
from sh_detector import SHDetector           # Use this if run on both Pi and Computer
from processjson import Range           # A utility class to read from Json file
from db_handler import Database
from compare import Compare         # A utility class used to compare temp and humid

sample_freq = 1 # time in seconds

def main():
    detector = SHDetector()
    database = Database()
    compare = Compare()
    database.get_today_status()

    database.create_dbtable()

    for _ in range(0, 5):
        detector.getSenseData()
        database.save_dbdata(detector.time, detector.temp, detector.humid)
        status = compare.compare_data(detector.temp, detector.humid)

        if status == "OK":
            print("status is OK")
        else:
            print("status is " + status)
            # database.save_daily_data()
        
        time.sleep(sample_freq)
    
    database.read_dbdata()

    # database.save_daily_data('OK','')
    # database.save_daily_data('BAD',': 5 *C below minimum temperature')
    database.read_daily_data()


    database.clear_dbdata()     # Uncomment this line if what to clear dumy data
    database.clear_daily_data()     # Uncomment this line if what to clear dumy data

main()