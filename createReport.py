import csv
from db_handler import Database
class CreateReport:
    db = Database()

    def CreatCSV(self, message):
        with open("report.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])
            for m in message:
                writer.writerow([m[0], m[1]])

    def CreatSum(self, message):
        with open("summary.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["DateTime","Temp","Humid"])
            for m in message:
                writer.writerow([m[0], m[1], m[2]])
    
if __name__ == "__main__":
    cr = CreateReport()
    cr.CreatCSV(Database().read_daily_data())
    # cr.CreatSum(Database().read_dbdata())