import time
import webbrowser

total_breaks = 3
break_count = 0

print ('This program started on' + time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open ('https://www.youtube.com/watch?v=sYqWNocRIh8&list=RDQM8GBMJIQhYMs&index=6')
    break_count = break_count + 1




