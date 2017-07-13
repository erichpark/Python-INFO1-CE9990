"""
lyrics.py

Eric Park
INFO1-CE9990 Section 2
Homework for July 6, 2017

Lyrics to the song "12 Days of Christmas"

"""

import sys

lyrics = [
    "My true love gave to me",
    "Twelve drummers drumming",
    "Eleven pipers piping",
    "Ten lords a-leaping",
    "Nine ladies dancing",
    "Eight maids a-milking",
    "Seven swans a-swimming",
    "Six geese a-laying",
    "Five Golden Rings",
    "Four colly birds",
    "Three French hens",
    "Two turtledoves",
    "And a partridge in a pair tree."
]

order = [lyrics - 1];

outer = 1
while outer <= 12:

    inner = 1
    while inner <= 12:
        print(order)
        inner +=1

    outer += 1

sys.exit(0)

