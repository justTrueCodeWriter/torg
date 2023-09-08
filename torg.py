import os
import sys
from datetime import datetime

currentTime = datetime.now()
curWeekday = currentTime.strftime("%A") 
curDay = currentTime.strftime("%d") 
curMonth = currentTime.strftime("%m")
curYear = currentTime.strftime("%Y")

months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}

scheduleDate = f"{curYear}-{curMonth}-{curDay}" 

def schedule_view(file):
    noteLine = ''
    for line in file:
        if ("SCHEDULED: <" + scheduleDate in line):
            noteLine = noteLine.replace('\n', '')
            if("TODO" in noteLine):
                print(noteLine.replace("TODO", "\x1b[6;30;41m TODO \x1b[0m"))
            elif ("DONE" in noteLine):
                print(noteLine.replace("DONE", "\x1b[6;30;42m DONE \x1b[0m"))
        noteLine = line

def help_message():
    print("----------------------------------\n\
            \rUsage: torg [COMMAND]\n\
           \r----------------------------------\n\
            \rtorg sched    [show today's tasks]")

def main(argv):

    USER = os.environ['USER']
    file = open(f"/home/{USER}/org/Orgmode.org", 'r')
    #print(sys.argv[1])
    if (len(argv)>1):
        if ("sched" == sys.argv[1]):
            schedule_view(file)
        elif ("help" == sys.argv[1]):
            help_message()
        else:
            print(f"torg: Unknown command: {sys.argv[1]}")

    else:
        help_message()

    file.close()

if __name__ == "__main__":
    main(sys.argv)
