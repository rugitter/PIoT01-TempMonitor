#!/usr/bin/env python3
import requests
import json
import os

class BulletNotice:
    def __init__(self):
        self.ACCESS_TOKEN = "o.UCb2WKIWWk0RsoeEfpnrhrLd4a1ei6Ui"

    def send_notification(self, title, body):
        """ Sending notification via pushbullet.
            Args:
                title (str) : Title of text.
                body (str) : Body of text.
        """
        data = { "type": "note", "title": title, "body": body }

        response = requests.post("https://api.pushbullet.com/v2/pushes", data = json.dumps(data),
            headers = { "Authorization": "Bearer " + self.ACCESS_TOKEN, "Content-Type": "application/json" })

        if(response.status_code != 200):
            raise Exception()

        print("Notification sent.")

    # # Main function.
    # def main():
    #     # ip_address = os.popen("hostname -I").read()
    #     # send_notification(ip_address, "From Raspberry Pi")
    #     send_notification("From Laptop", "I am a robot!")

    # # Execute.
    # if __name__ == "__main__":
    #     main()