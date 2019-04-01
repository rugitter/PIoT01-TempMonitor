import csv
from db_handler import Database

class CreateReport:
    # db = Database()
    # print(db.read_daily_data())

    def CreatCSV(self, message):
        with open("report.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])
            for m in message:
                status = m[1] + m[2]
                writer.writerow([m[0], status])





if __name__ == "__main__":
    cr = CreateReport()
    cr.CreatCSV(Database().read_daily_data())

# db = Database()

