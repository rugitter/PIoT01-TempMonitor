from processjson import Range
import csv
# r = Range()
# print(r.get_max_humid())
temp = list()
hum = list()

temp.append(20)
temp.append(30)
temp.append(40)
temp.append(20)

hum.append(50)
hum.append(55)
hum.append(55)
hum.append(50)

# Compare the temp and humi data with config
def CompareData(temp, hum):
    r = Range()
    status = ""
    reason = ""

    for t in temp:
        if t < r.get_min_temp():
            status = "BAD"
            reason = "%d *C below minimum temperature" %(r.get_min_temp() - t) 
            return status + ": " + reason

        if t > r.get_max_temp():
            status = "BAD"
            reason = "%d *C above maximum temperature" %(t - r.get_max_temp())
            return status + ": " + reason

        for h in hum:
            if h < r.get_min_humid():
                status = "BAD"
                reason = "%d%% below minimum humidity" %(r.get_min_humid() - h)
                return status + ": " + reason
            
            if h > r.get_max_humid():
                status = "BAD"
                reason = "%d%% above maximum humidity" %(h - r.get_max_humid())
                return status + ": " + reason
        
        status = "OK"

    return status 

with open("report.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date","Status"])
    writer.writerow(["09/03/2019",CompareData(temp, hum)])
# print(CompareData(temp, hum))


    