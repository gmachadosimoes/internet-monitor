import speedtest
import datetime
import time
import csv

s = speedtest.Speedtest()

with open('monitor.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        time_now = datetime.datetime.now().strftime("%h: %m: %s")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")

        # 60 seconds sleep
        time.sleep(60)
