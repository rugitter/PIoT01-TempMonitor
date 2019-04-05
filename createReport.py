import csv
from db_handler import Database
class CreateReport:
    db = Database()

    def CreatCSV(self, message):
        with open("report.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])
            for m in message:
                writer.writerow([m[0], m[1]])

if __name__ == "__main__":
    cr = CreateReport()
    cr.CreatCSV(Database().read_daily_data())