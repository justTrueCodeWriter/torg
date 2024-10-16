import os
import sys
from datetime import datetime, timedelta
from io import TextIOWrapper
import re

currentTime = datetime.now()
curWeekday = currentTime.strftime("%A") 
curWeekNumber = currentTime.strftime("%W")
curDay = currentTime.strftime("%d") 
curMonth = currentTime.strftime("%m")
curYear = currentTime.strftime("%Y")

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

scheduleDate = f"{curYear}-{curMonth}-{curDay}" 

def schedule_view(filename: str) -> None:
    file = open(filename, 'r')
    print(f"{curWeekday} {curDay} {months[int(curMonth)-1]} {curYear} W{curWeekNumber}")
    noteLine = ''
    isScheduled = False
    lineNumber = -1
    for line in file:
        if ("SCHEDULED: <" + scheduleDate in line):
            isScheduled = True
            noteLine = noteLine.replace('\n', '')
            if("TODO" in noteLine):
                print(f"{lineNumber} "+noteLine.replace("TODO", "\x1b[1;31;40m TODO \x1b[0m"))
            elif ("DONE" in noteLine):
                print(f"{lineNumber} "+noteLine.replace("DONE", "\x1b[1;32;40m DONE \x1b[0m"))
        noteLine = line 
        lineNumber+=1
    if (isScheduled == False):
        print("Nothing is scheduled :)")
    file.close()

def todo_view(filename: str, tag_filter: str) -> None:
    file = open(filename, 'r')

    noteLine = ''
    isTodo = False
    isFilterActive = False   
    lineNumber = -1

    if (tag_filter):
        isFilterActive = True

    for line in file:
        noteLine = noteLine.replace('\n', '')
        if ("TODO" in noteLine and (f":{tag_filter}:" in noteLine)):
            isTodo = True
            print(f"{lineNumber} "+noteLine.replace("TODO", "\x1b[1;31;40m TODO \x1b[0m"))
        if("TODO" in noteLine and not isFilterActive):
            isTodo = True
            print(f"{lineNumber} "+noteLine.replace("TODO", "\x1b[1;31;40m TODO \x1b[0m"))
        noteLine = line
        lineNumber+=1
    if (isTodo == False):
        print("Nothing ToDo")
    file.close()

def agenda_view(filename: str) -> None:
    #TODO: add agenda view here
    #NOTE: form 7days 2d list, walk through the file line by line and add it to the 2D list by days
    #NOTE: SUN, MON, TUE, WED, THU, FRI, SAT
    #NOTE: [[], [], [], [], [], [], []]

    agenda_dict = dict()
    timeToday = datetime.now()
    for i in range (0, 7):
        dt = timeToday + timedelta(days=i)
        weekday = dt.strftime("%A") 
        weekNumber = dt.strftime("%W")
        day = dt.strftime("%d") 
        month = dt.strftime("%m")
        year = dt.strftime("%Y")


        #print(f"{weekday} {day} {months[int(month)-1]} {year} W{weekNumber}")

        iterSchedDate = f"{year}-{month}-{day}" 
        agenda_dict.update({iterSchedDate: []})
    
    file = open(filename, 'r')
    file.close()

    for agendaDate in agenda_dict.keys():
        print(agendaDate)
        for note in agenda_dict[agendaDate]:
            print(note) 


"""
    for line in file:
        fileDate = re.search("*-*-*", line)
        print(line[fileDate.start():] + line[:fileDate.end()])

"""
"""     
    noteLine = ''
    lineNumber = 0
    isScheduled = False
    for line in file:
        if ("SCHEDULED: <" + scheduleDate in line):
            isScheduled = True
            noteLine = noteLine.replace('\n', '')
            if("TODO" in noteLine):
                print(f"{lineNumber} "+noteLine.replace("TODO", "\x2b[1;31;40m TODO \x1b[0m"))
            elif ("DONE" in noteLine):
                print(f"{lineNumber} "+noteLine.replace("DONE", "\x2b[1;32;40m DONE \x1b[0m"))
        noteLine = line 
        lineNumber+=2
    if (isScheduled == False):
        print("Nothing is scheduled :)") 
"""



def set_task_done(filename: str, str_number: int) -> None:
    file = open(filename, 'r')
    data = file.readlines() 
    file.close()

    file = open(filename, 'w')
    for i in range(0, len(data)):
        if(data[i].find("TODO") and i==str_number):
            data[i] = data[i].replace("TODO", "DONE")
    file.writelines(data)
    file.close()

def help_message():
    print("---------------------------------------------\n\
            \rUsage: torg [COMMAND]\n\
           \r---------------------------------------------\n\
            \rtorg sced               [show today's tasks]\n\
            \rtorg todo               [show all ToDo's]\n\
            \rtorg done <line_number> [complete task]\n\
            \rtorg agen               [show agenda]\n\
          ")

def main(argv):

    USER = os.environ['USER']
    filename = f"/home/{USER}/org/Orgmode.org"
    #print(sys.argv[1])
    if (len(argv)>1):
        if ("help" == sys.argv[1]):
            help_message()
        elif ("sced" == sys.argv[1]):
            schedule_view(filename)
        elif ("todo" == sys.argv[1]):
            if (len(sys.argv) == 3):
                todo_view(filename, sys.argv[2])
            else:
                todo_view(filename, "")
        elif ("agen" == sys.argv[1]):
            agenda_view(filename)
        elif ("done" == sys.argv[1]):
            set_task_done(filename, int(sys.argv[2]))
        else:
            print(f"torg: Unknown command: {sys.argv[1]}")

    else:
        help_message()

if __name__ == "__main__":
    main(sys.argv)
