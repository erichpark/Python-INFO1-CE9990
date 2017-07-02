"""
graphpaper.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 22, 2017

"""

import sys

while True:

    try:
        rows = input("How many rows of boxes? ")
    except EOFError:
        sys.exit(0)

    try:
        rows = int(rows)
    except ValueError:
        print("Sorry,", rows, "is not a whole number.")
        rows = 0
        print("The number will default to 0.")

    try:
        columns = input("How many columns of boxes? ")
    except EOFError:
        sys.exit(0)

    try:
        columns = int(columns)
    except ValueError:
        print("Sorry,", columns, "is not a whole number.")
        columns = 0
        print("The number will default to 0.")

    try:
        rspace = input("How many rows of spaces in each box (e.g., 1)? ")
    except EOFError:
        sys.exit(0)

    try:
        rspace = int(rspace)
    except ValueError:
        print("Sorry,", rspace, "is not a whole number.")
        rspace = 0
        print("The number will default to 0.")

    try:
        cspace = input("How many columns of spaces in each box (e.g., 3)? ")
    except EOFError:
        sys.exit(0)
    
    try:
        cspace = int(cspace)
    except ValueError:
        print("Sorry,", cspace, "is not a whole number.")
        cspace = 0
        print("The number will default to 0.")

    a = 1
    while a <= rows:
        b = 1
        while b <= rspace:
            print("+", rspace * "-", sep = "", end = "")
            b += 1
        print("+") 
        c = 1
        while c <= columns:
            d = 1
            while d <= cspace:
                print("|", cspace * " ", sep = "", end = "")
                d += 1  
            c += 1 
            print("|") 
        a += 1
    a = 1
    while a <= rows:
        b = 1
        while b <= rspace:
            print("+", rspace * "-", sep = "", end = "")
            b += 1
        print("+")
        a += rows
    print() #Skip a line

sys.exit(0)
