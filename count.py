"""
count.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 29, 2017

Count to 10 in Japanese and Russian, ascending and descending
"""

import sys

#a is a list containing two items: a[0] is Japanese and a[1] is Russian.
#a[0] is a list containing two items: a[0][0] is Japanese ascending,
#and a[0][1] is Japanese descending.
#a[1] is a list containing two items: a[1][0] is Russian ascending,
#and a[1][1] is Russian descending.
#Finally, a[0][0] is a list containing 10 items.

a = [
    [
        [
            "ichi  (いち)", #Japanese ascending, 1 to 10
            "ni    (に)",
            "san   (さん)",
            "yon   (よん)",
            "go    (ご)",
            "roku  (ろく)",
            "nana  (なな)",
            "hachi (はち)",
            "kyuu  (きゅう)",
            "jyuu  (じゅう)"
        ],
        [
            "jyuu  (じゅう)",  #Japanese descending, 10 to 1
            "kyuu  (きゅう)",
            "hachi (はち)",
            "nana  (なな)",
            "roku  (ろく)",
            "go    (ご)",
            "yon   (よん)",
            "san   (さん)",
            "ni    (に)",
            "ichi  (いち)"
        ],
    ],

    [
        [
            "a-deen      (Один)", #Russian ascending, 1 to 10
            "dva         (Два)",
            "tree        (Три)",
            "chye-tir-ye (Четыре)",
            "pyat        (Пять)",
            "shest       (Шесть)",
            "syem        (Семь)",
            "vo-syem     (Восемь)",
            "dyev-yat    (Девять)",
            "dyes-yat    (Десять)"
        ],
        [
            "dyes-yat    (Десять)", #Russian descending 10 to 1
            "dyev-yat    (Девять)",
            "vo-syem     (Восемь)",
            "syem        (Семь)",
            "shest       (Шесть)",
            "pyat        (Пять)",
            "chye-tir-ye (Четыре)",
            "tree        (Три)",
            "dva         (Два)",
            "a-deen      (Один)"
        ]
    ]
]

while True:

    while True:
        try:
            language = input("Enter '1' for Japanese or '2' for Russian: ")
        except EOFError:
            sys.exit(0)

        try:
            language = int(language)
        except ValueError:
            print("Sorry,", language, "is not an int. Please try again.")
            print()
            continue   #Go back up to the word "while"

        if language == 1 or language == 2:
            break;

        print("Sorry, the int must be 1 or 2. Please try again.")
        print()

    while True:
        try:
            order = input("Enter '1' for ascending order or '2' for descending order: ")
        except EOFError:
            sys.exit(0)

        try:
            order = int(order)
        except ValueError:
            print("Sorry,", order, "is not an int. Please try again.")
            print()
            continue   #Go back up to the word "while"

        if order == 1 or order == 2:
            break;

        print("Sorry, the int must be 1 or 2. Please try again.")
        print()

    print() #Skip a line

    for s in a[language-1][order-1]:
        print(s)

    print() #Skip a line
