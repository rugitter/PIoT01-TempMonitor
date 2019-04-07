""" Original provided by Matthew Bolger in tutorial at course
    Programming Internet of Things (COSC2755) RMIT University
    for teaching purposes
"""
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
