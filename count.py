"""
count.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 29, 2017

Count to 10 in Two Languages

"""

import sys

while True:

    try:
        language = input("Enter '1' for Japanese or '2' for Russian: ")
    except EOFError:
        sys.exit(0)

    try:
        language = int(language)
    except ValueError:
        print("Sorry,", language, "is not an integer. Please try again.")
        print()
        continue #Go back up to the word "while"

    try:
        order = input("Enter '1' for ascending order or '2' for descending order: ")
    except EOFError:
        sys.exit(0)

    try:
        order = int(order)
    except ValueError:
        print("Sorry,", order, "is not an integer. Please try again.")
        print()
        continue #Go back up to the word "while"

    print() #Skip a line

    if language != 1 and order == 2 \
    and language != 2 and order == 2:   
        for i in range(10, 0, -1):
            print (i)   

    elif language == 1 and order == 1:
        print(1 , " ichi  (いち)")
        print(2 , " ni    (に)")
        print(3 , " san   (さん)")
        print(4 , " yon   (よん)")
        print(5 , " go    (ご)")
        print(6 , " roku  (ろく)")
        print(7 , " nana  (なな)")
        print(8 , " hachi (はち)")
        print(9 , " kyuu  (きゅう)")
        print(10 , "jyuu  (じゅう)")

    elif language == 1 and order == 2:
        print(10 , "jyuu  (じゅう)")
        print(9 , " kyuu  (きゅう)")
        print(8 , " hachi (はち)")
        print(7 , " nana  (なな)")
        print(6 , " roku  (ろく)")
        print(5 , " go    (ご)")
        print(4 , " yon   (よん)")
        print(3 , " san   (さん)")
        print(2 , " ni    (に)")
        print(1 , " ichi  (いち)")

    elif language == 2 and order == 1:
        print(1 , " a-deen      (Один)")
        print(2 , " dva         (Два)")
        print(3 , " tree        (Три)")
        print(4 , " chye-tir-ye (Четыре)")
        print(5 , " pyat        (Пять)")
        print(6 , " shest       (Шесть)")
        print(7 , " syem        (Семь)")
        print(8 , " vo-syem     (Восемь)")
        print(9 , " dyev-yat    (Девять)")
        print(10 , "dyes-yat    (Десять)")

    elif language == 2 and order == 2:
        print(10 , "dyes-yat    (Десять)")
        print(9 , " dyev-yat    (Девять)")
        print(8 , " vo-syem     (Восемь)")
        print(7 , " syem        (Семь)")
        print(6 , " shest       (Шесть)")
        print(5 , " pyat        (Пять)")
        print(4 , " chye-tir-ye (Четыре)")
        print(3 , " tree        (Три)")
        print(2 , " dva         (Два)")
        print(1 , " a-deen      (Один)")

    else:
        for i in range(1, 11):
            print(i)
	
    print() #Skip a line

sys.exit(0)
