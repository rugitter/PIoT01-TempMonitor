import json
filename = 'config.json'

class Range:
    # MIN_TEMPERATURE
    # MAX_TEMPERATURE
    # MIN_HUMIDITY
    # MAX_HUMIDITY

    def __init__(self):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(data)

        self.MIN_TEMPERATURE = data['min_temperature']
        self.MAX_TEMPERATURE = data['max_temperature']
        self.MIN_HUMIDITY = data['min_humidity']
        self.MAX_HUMIDITY = data['max_humidity']

    def get_min_temp(self):
        return self.MIN_TEMPERATURE

    def get_max_temp(self):
        return self.MAX_TEMPERATURE

    def get_min_humid(self):
        return self.MIN_HUMIDITY

    def get_max_humid(self):
        return self.MAX_HUMIDITY

# r = Range()
# print(r.get_max_humid())

