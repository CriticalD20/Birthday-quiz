"""
birthday.py
Author: James Napier
Credit:
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day


name=input("Hello, what is your name? ")

birthmonth=input("Hi "+name+", what was the name of the month you were born in? ")
month = month_name[todaymonth]
if birthmonth == month:
#I NEED TO FIX THE FREAKING YEAR PARTS!!! AGGGGGHHHHH

    birthyear=float(input("And what year were you born in, "+name+"? "))
    birthday=float(input("And the day? "))
    if birthday==int(todaydate):
        print("Happy birthday!")
       
    
    else:
        if birthyear >=2000:
            if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
                print(""+name+", you are a fall baby of the two thousands.")
            elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
                print(""+name+", you are a winter baby of the two thousands.")
            elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
                print(""+name+", you are a spring baby of the two thousands.")
            else:
                print(""+name+", you are a summer baby of the two thousands.")
        elif birthyear>=1990 and birthyear<2000:
            if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
                print(""+name+", you are a fall baby of the nineties.")
            elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
                print(""+name+", you are a winter baby of the nineties.")
            elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
                print(""+name+", you are a spring baby of the nineties.")
            else:
                print(""+name+", you are a summer baby of the nineties.")
        elif birthyear>=1980 and birthyear<1990:
            if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
                print(""+name+", you are a fall baby of the eighties.")
            elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
                print(""+name+", you are a winter baby of the eighties.")
            elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
                print(""+name+", you are a spring baby of the eighties.")
            else:
                print(""+name+", you are a summer baby of the eighties.")
        else:
            if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
                print(""+name+", you are a fall baby of the stone age.")
            elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
                print(""+name+", you are a winter baby of the stone age.")
            elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
                print(""+name+", you are a spring baby of the stone age.")
            else:
                print(""+name+", you are a summer baby of the stone age.")
elif birthmonth=="October":
    birthyear=float(input("And what year were you born in, "+name+"? "))
    birthday=float(input("And the day? "))
    if birthday==int(31):
        print("You were born on Halloween!")
    elif birthyear >=2000:
        print(""+name+", you are a fall baby of the two thousands.")
    elif birthyear>=1990 and birthyear<2000:
        print(""+name+", you are a fall baby of the nineties.")
    elif birthyear>=1980 and birthyear<1990:
        print(""+name+", you are a fall baby of the eighties.")
    else:
        print(""+name+", you are a fall baby of the stone age.")
        
        
else:
    birthyear=input("And what year were you born in, "+name+"? ")
    birthday=input("And the day? ")
    if birthyear >=str(2000):
        if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
            print(""+name+", you are a fall baby of the two thousands.")
        elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
            print(""+name+", you are a winter baby of the two thousands.")
        elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
                print(""+name+", you are a spring baby of the two thousands.")
        else:
            print(""+name+", you are a summer baby of the two thousands.")
    elif birthyear>=str(1990) and birthyear<str(2000):
        if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
            print(""+name+", you are a fall baby of the nineties.")
        elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
            print(""+name+", you are a winter baby of the nineties.")
        elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
            print(""+name+", you are a spring baby of the nineties.")
        else:
            print(""+name+", you are a summer baby of the nineties.")
    elif birthyear>=str(1980) and birthyear<str(1990):
        #There s something wrong with the stone age timeline. Try to fix it after quiz
        if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
             print(""+name+", you are a fall baby of the eighties.")
        elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
            print(""+name+", you are a winter baby of the eighties.")
        elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
            print(""+name+", you are a spring baby of the eighties.")
        else:
            print(""+name+", you are a summer baby of the eighties.")
    else:
        if birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
            print(""+name+", you are a fall baby of the stone age.")
        elif birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
            print(""+name+", you are a winter baby of the stone age.")
        elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
            print(""+name+", you are a spring baby of the stone age.")
        else:
            print(""+name+", you are a summer baby of the stone age.")
      