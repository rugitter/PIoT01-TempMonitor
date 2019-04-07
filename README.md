# PIoT01-TempMonitor
This is to write a small IoT application using Raspberry Pi and Sense HAT in Python language. This is be a green house monitor which run at certain time of each day to monitor the temperature and humidity of the room.

Required package
Intall pip3 - sudo apt install python3-pip
pip3 install requests   - Required for pushbullet file
pip3 install python-crontab     - Install python-crontab package


Common command
Make file executable
    - chmod +x 06_pycurlBullet.py

Use Bluetooth module
To pair devices see: https://www.cnet.com/how-to/how-to-setup-bluetooth-on-a-raspberry-pi-3/
To import bluetooth module
# sudo apt install bluetooth bluez blueman
# pip3 install pybluez

To use bt-device: 
# sudo apt install bluez-tools

Installed on Raspberry Pi
See http://denvycom.com/blog/playing-audio-over-bluetooth-on-rasbperry-pi-command-line/
# sudo apt-get install bluealsa

Raspberry Pi Command line to connect bluetooth
# bluetoothctl

# agent on

# discoverable on
You'll have three minutes for the following steps. On the master, start bluetoothctl and enter this:
Code: Select all

# scan on
After some moments it should find the slave and print the Bluetooth device address, something like AA:BB:CC:DD:EE:FF. 
When you found your desired device, you can type in
# scan off
# pair AA:BB:CC:DD:EE:FF
Check the slave and follow any instructions; if asked to authorize, reply with 'yes', not 'y'. The master should indicate you are paired.

# trust AA:BB:CC:DD:EE:FF
and it should indicate trusted. You can now 'quit' bluetoothctl on both machines. 

# connect AA:BB:CC:DD:EE:FF     - Not succed.
This need proper protocols are installed, otherwise it will show failed.

# quit
To quit bluetoothctl

