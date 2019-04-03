#!/usr/bin/env python3
from crontab import CronTab

# Init cron.
pi_cron = CronTab(user = "pi")
pi_cron.remove_all()

# Add new cron job.
job = pi_cron.new(command = "/usr/bin/python /home/pi/piot/monitorAndNotify.py")

# Job settings.
job.day.every(1)
job.minute.every(1)
job.hour.on(19)
pi_cron.write()
