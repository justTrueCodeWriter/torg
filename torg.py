import os
import sys
from datetime import datetime

currentTime = datetime.now()
curWeekday = currentTime.strftime("%A") 
curWeekNumber = currentTime.strftime("%W")
curDay = currentTime.strftime("%d") 
curMonth = currentTime.strftime("%m")
curYear = currentTime.strftime("%Y")

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

scheduleDate = f"{curYear}-{curMonth}-{curDay}" 

def schedule_view(file):
    noteLine = ''
    isScheduled = False
    for line in file:
        if ("SCHEDULED: <" + scheduleDate in line):
            print(f"{curWeekday} {curDay} {months[int(curMonth)-1]} {curYear} W{curWeekNumber}")
            isScheduled = True
            noteLine = noteLine.replace('\n', '')
            if("TODO" in noteLine):
                print(noteLine.replace("TODO", "\x1b[1;31;40m TODO \x1b[0m"))
            elif ("DONE" in noteLine):
                print(noteLine.replace("DONE", "\x1b[1;32;40m DONE \x1b[0m"))
        noteLine = line
    if (isScheduled == False):
        print("Nothing is scheduled :)")

def todo_view(file):
    noteLine = ''
    isTodo = False
    for line in file:
        noteLine = noteLine.replace('\n', '')
        if("TODO" in noteLine):
            isTodo = True
            print(noteLine.replace("TODO", "\x1b[1;31;40m TODO \x1b[0m"))
        noteLine = line
    if (isTodo == False):
        print("Nothing ToDo")

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
        if ("help" == sys.argv[1]):
            help_message()
        elif ("sched" == sys.argv[1]):
            schedule_view(file)
        elif ("todo" == sys.argv[1]):
            todo_view(file)
        else:
            print(f"torg: Unknown command: {sys.argv[1]}")

    else:
        help_message()

    file.close()

if __name__ == "__main__":
    main(sys.argv)
