"""
dictionary.py

Eric Park
INFO1-CE9990 Section 2
Homework for July 20, 2017

America's 25 Richest Families, according to Forbes
"""


import sys

families = {
    1: "Walton family",
    2: "Koch family",
    3: "Mars family",
    4: "Cargill-MacMillan family",
    5: "Cox family",
    6: "S.C. Johnson family",
    7: "Pritzker family",
    8: "(Edward) Johnson family",
    9: "Hearst family",
    10: "Duncan family",
    11: "Newhouse family",
    12: "Lauder family",
    13: "Dorrance family",
    14: "Ziff family",
    15: "Du Pont family",
    16: "Hunt family",
    17: "Goldman family",
    18: "Busch family",
    19: "Sackler family",
    20: "Brown family",
    21: "Marshall family",
    22: "Mellon family",
    23: "Butt family",
    24: "Rockefeller family",
    25: "Gallo family"
} 

while True:
    
    while True:
        try:
            rank = input("Please select a rank from 1 to 25: ")
        except EOFError:
            sys.exit(0)

        try:
            definition = families[rank]
        except KeyError:
            print()
            print("Sorry,", rank, "is not a valid selection. Please try again.")
            print()
            continue   #Go back up to the second "while"

        print()
        print("The", definition)
        print()

        break;

    while True:
        try:
            richer = input("Would you like to see which families have more Benjamins? (Y/N) ")
        except EOFError:
            sys.exit(0)

        Y = "Y"
        N = "N"
        
        if rank == 1 and richer == Y:           
            print()
            print("No one else ranks above the Waltons.")
            print()
        break
       

            
            
    
sys.exit(0)

