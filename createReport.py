import csv

class CreatReport():

    def CreatCSV(self, message = []):
        with open("report.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])
            for m in message:
                status = m[1] + m[2]
                writer.writerow([m[0], status])

    