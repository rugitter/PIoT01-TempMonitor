from processjson import Range

# Compare the temp and humi data with config
class Compare():
    def CompareData(self, temp, hum):
        r = Range()
        status = ""
        reason = ""

        
        if temp < r.get_min_temp():
            status = "BAD"
            reason = "%f *C below minimum temperature" %(r.get_min_temp() - temp) 
            return status + ": " + reason

        if temp > r.get_max_temp():
            status = "BAD"
            reason = "%f *C above maximum temperature" %(temp - r.get_max_temp())
            return status + ": " + reason

        if hum < r.get_min_humid():
            status = "BAD"
            reason = "%d%% below minimum humidity" %(r.get_min_humid() - hum)
            return status + ": " + reason
    
        if hum > r.get_max_humid():
            status = "BAD"
            reason = "%d%% above maximum humidity" %(hum - r.get_max_humid())
            return status + ": " + reason
        
        status = "OK"

        return status 
