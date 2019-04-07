import csv
from db_handler import Database
class CreateReport:

    def CreatCSV(self, message):
        with open("report.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date","Status"])
            for m in message:
                writer.writerow([m[0], m[1]])
    
    def GetDailyData(self, day_num, message):
        day = str(day_num)
        datalist = []
        
        for m in message:
            if m[0][7] == day:
                datalist.append(m)

        return datalist

    def CreateDataCSV(self, message):
        temp_average = 0.0
        humid_average = 0

        temp = []
        humid = []
        date = []
        
        for m in message:
            date = m[0].split()
            temp_average += m[1]
            humid_average += m[2]

            temp.append(m[1])
            humid.append(m[2])
        
        temp_average = round(temp_average / 60, 1)
        humid_average = round(humid_average / 60, 0)

        with open("AnalyseData.csv", "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date[0], temp_average, humid_average, max(temp), max(humid), min(temp), min(humid)])

    def CreatAllDataCSV(self, message):
        with open("AllData.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Temp", "Humid"])
            for m in message:
                date = m[0].split()
                writer.writerow([date[0], m[1], m[2]])

            


if __name__ == "__main__":
    """ with open("AnalyseData.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date","Temp_Average","Humid_Average","Temp_Max","Humid_Max","Temp_Min","Humid_Min"]) """
    
    """ CreateReport().CreateDataCSV(CreateReport().GetDailyData(1, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(2, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(3, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(4, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(5, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(6, Database().read_dbdata()))
    CreateReport().CreateDataCSV(CreateReport().GetDailyData(7, Database().read_dbdata())) """

    #CreateReport().CreatAllDataCSV(Database().read_dbdata())

    CreateReport().CreatCSV(Database().read_daily_data)

