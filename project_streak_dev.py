import os
import time
import json
import subprocess

current_streak = 0

PID = subprocess.run(['PowerShell', "(Get-Process -Name Code).ProcessName[0]"], capture_output=True, text=True).stdout.strip()


local_time = time.localtime()

readable_hours = time.strftime("%H:%M", local_time)
readable_days = time.strftime("%Y/%m/%d")

streak_data = {f"{readable_days}":{
    "timestamp":readable_hours,
    "App":PID,
    "Current_Streak":current_streak
}}



if not os.path.exists("streak data_dev.json"):
    with open('streak data.json', 'w') as w:
        w.write(json.dumps(streak_data, indent=4))
else:
    print("path already exists")


with open('streak data_dev.json', 'r') as r:
    data = json.load(r)

previous_day = time.strftime("%Y/%m/%d", time.localtime(time.time() - 86400))

if previous_day in data:
    current_streak = int(data[previous_day]['Current_Streak'])
    current_streak += 1
else:
 current_streak += 1

data[readable_days] = {
    "timestamp":readable_hours,
    "App":PID,
    "Current_Streak":current_streak
}
with open('streak data_dev.json', 'w') as w:
    json.dump(data, w, indent=4)
        
#===== Debug Zone ======
print(f"Current Streak: {data[readable_days]['Current_Streak']}")