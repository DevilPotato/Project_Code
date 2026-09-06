import os
import time
import json
import subprocess

current_streak = 0

PID = subprocess.run(['PowerShell', "(Get-Process -Name Code).ProcessName[0]"], capture_output=True, text=True).stdout.strip()


temp = {}

local_time = time.localtime()

readable_hours = time.strftime("%H:%M", local_time)
readable_days = time.strftime("%Y/%m/%d")

streak_data = {f"{readable_days}":{
    "timestamp":readable_hours,
    "App":PID,
    "Current_Streak":current_streak
}}



if not os.path.exists("streak data.json"):
    with open('streak data.json', 'w') as w:
        w.write(json.dumps(streak_data, indent=4))
else:
    print("path already exists")

with open('streak data.json', 'r') as r:
    data = json.load(r)

if readable_days in data:
    print('come back tommorow')
else:
    current_streak += 1

    data[readable_days] = {
        "timestamp":readable_hours,
        "App":PID,
        "Current_Streak":current_streak
    }
    with open('streak data.json', 'w') as w:
        json.dump(data, w, indent=4)

print(data)
#===== Debug Zone ======

print('hello')