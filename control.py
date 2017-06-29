"""
control.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 22, 2017

School Lunch and High Poverty Schools

"""

import sys

while True:

    try:
        lunch = input("Enter the number of students in your school who qualify for free or reduced lunch: ")
    except EOFError:
        sys.exit(0)

    try:
        lunch = int(lunch)
    except ValueError:
        print("Sorry,", s, "is not a whole number.")
        lunch = 0
        print("The number of students will default to 0.")

    try:
        nolunch = input("Enter the number of students in your school who do NOT qualify for free or reduced lunch: ")
    except EOFError:
        sys.exit(0)

    try:
        nolunch = int(nolunch)
    except ValueError:
        print("Sorry,", s, "is not a whole number.")
        nolunch = 0
        print("The number of students will default to 0.")

    print() #Skip a line

    total = lunch + nolunch	    #total represents the total number of students at a school.
    
    if total == 0:
        print("There are no students at your school.")
        sys.exit(0)

    povertyrate = lunch / total	    #povertyrate represents the poverty rate of students at a school.

    if povertyrate > .75:
        print("More than 75% of your students qualify for free or reduced lunch. According to the federal government, this statistic defines your school as a high-poverty school.")

    else:
        print("According to the federal government, your school does not meet the threshold of students qualifying for free or reduced lunch and is therefore NOT defined as a high-poverty school.")
	
    print() #Skip a line

sys.exit(0)
