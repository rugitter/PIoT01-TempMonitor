""" Original provided by Matthew Bolger in tutorial at course
    Programming Internet of Things (COSC2755) RMIT University, 2019 semester 1
    for teaching purposes
"""
import bluetooth
import os
import time
from sh_detector import SHDetector
from notify_bullet import BulletNotice  # A utility class used to send bullet notification

IPHONE_MAC = '1C:36:BB:C9:02:6A'
detector = SHDetector()
detector.getSenseData()
notice = BulletNotice()
# Main function.
def main():
    search()

# Search for device based on device's name.
def search():
    device_address = None
    dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
    # print("\nCurrently: {}".format(dt))
    time.sleep(3) # Sleep three seconds.
    nearby_devices = bluetooth.discover_devices()

    for mac_address in nearby_devices:
        if mac_address == IPHONE_MAC:
            device_address = mac_address
            device_name == bluetooth.lookup_name(mac_address, timeout = 5):
            # print("Found {} with MAC address: {}".format(device_name, device_address))
            break
        
    if device_address is not None:
        temp = detector.getTemp()
        humid = detector.getHumid()
        detector.show_message("Bluetooth-T:{} H:{}".format(temp, humid), 0.05)
        BulletNotice().send_notification(dt, "Blue tooth Connected\n Temperature : {}. \n Humidity : {}".format(temp, humid) )
    else:
        print("Could not find target device nearby...")

main()
