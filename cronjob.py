#!/usr/bin/env python3
from crontab import CronTab

# Init cron.
pi_cron = CronTab(user = "pi")
pi_cron.remove_all()

# Add new cron job.
job = pi_cron.new(command = "/usr/bin/python3 /home/pi/piot/monitorAndNotify.py")
# Job settings.
job.day.every(1)
job.minute.every(1)
job.hour.during(9,10)

# Add new cron job.
job2 = pi_cron.new(command = "/usr/bin/python3 /home/pi/piot/pi_bluetooth.py")
# Job settings.
job2.minute.every(5)

pi_cron.write()
