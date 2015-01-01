#python file
#This is my feeble attempt at a timer

import time, sys 

def Timer():

    #variables
    global hrs
    global mins
    global secs
    global i
    global s

    hrs,mins,secs = 0,0,0
    i,s = "",""
    print("Starting timer now! ... ")

    try:
        while True:
            time.sleep(1)
            secs += 1

            if secs == 60:
                mins += 1
                secs = 0
            if mins == 60:
                hours += 1
                mins = 0

            s = ("Current Time: " + repr(hrs) + "hrs"+ repr(mins) +
            "mins"+ repr(secs) + "secs" + "\tPress Ctrl+C stop timer.")
            print(s, end='\r')

    except KeyboardInterrupt:
        s = ("\nEnding Time: " + repr(hrs) + "hrs"+ repr(mins) +
        "mins"+ repr(secs) + "secs\n")
        print(s)


Timer()
