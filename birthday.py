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
name=input("Hello, what is your name? ")

birthmonth=input("Hello, "+name+", what was the name of the month you were born in? ")
if birthmonth == "September":
    birthyear=float(input("And what year were you born in, "+name+"? "))
    birthday=float(input("And the day? "))
    if birthday==int(21):
        print("Happy Birthday!")
       
        
    else:
        print(""+name+", why couldn't it be your birthday!?!?")
elif birthmonth=="October":
    birthyear=float(input("And what year were you born in, "+name+"? "))
    birthday=float(input("And the day? "))
    if birthday==int(31):
        print("You were born on Halloween!")
    else: 
        print(""+name+", why couldn't it be your birthday!?!?")
else:
    birthyear=input("And what year were you born in, "+name+"? ")
    birthday=input("And the day? ")
    print(""+name+", why couldn't it be your birthday!?!?")