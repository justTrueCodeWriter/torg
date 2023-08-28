import os
from datetime import datetime

currentTime = datetime.now()
curWeekday = currentTime.strftime("%A") 
curDay = currentTime.strftime("%d") 
curMonth = currentTime.strftime("%m")
curYear = currentTime.strftime("%Y")

months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}

scheduleDate = f"{curYear}-{curMonth}-{curDay}" 

USER = os.environ['USER']
file = open(f"/home/{USER}/org/Orgmode.org", 'r')

noteLine = ''
for line in file:
    if (scheduleDate in line):
        noteLine = noteLine.replace('\n', '')
        if("TODO" in noteLine):
            print(noteLine.replace("TODO", "\x1b[6;30;41m TODO \x1b[0m"))
        elif ("DONE" in noteLine):
            print(noteLine.replace("DONE", "\x1b[6;30;42m DONE \x1b[0m"))
    noteLine = line

file.close()
