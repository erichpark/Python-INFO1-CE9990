"""
inout.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 15, 2017

The MTA and Productivity: A Program (with a sense of humor)

"""

import sys

while True:

    try:
        s = input("Enter the number of MTA delays: ")
    except EOFError:
        sys.exit(0)

    try:
        delays = int(s)
    except ValueError:
        print("Sorry,", s, "is not a whole number.")
        delays = 0
        print("The number of delays will default to 0.")

    try:
        s = input("Enter the number of minutes per delay: ")
    except EOFError:
        sys.exit(0)

    try:
        minutes = int(s)
    except ValueError:
        print("Sorry,", s, "is not a whole number.")
        minutes = 0
        print("The number of minutes will default to 0.")

    try:
        s = input("Enter the total number of riders affected: ")
    except EOFError:
        sys.exit(0)

    try:
        riders = int(s)
    except ValueError:
        print("Sorry,", s, "is not a whole number.")
        riders = 0
        print("The number of riders will default to 0.")

    hours = delays * minutes * riders / 60 

    if hours == 1:
        print("That's", int(hours), "hour of lost productivity in NYC. Hooray!")

    else:
        print("That's", int(hours), "hours of lost productivity in NYC. Hooray!")

    print() #Skip a line

    print("Back to work.")

    print() #Skip a line

sys.exit(0)
