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
    "Two turtledoves",
    "Three French hens",
    "Four colly birds",
    "Five Golden Rings",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming",
    "And a partridge in a pair tree."
]

n = len(lyrics)

print("On the 1st day of Christmas")
for i in range(1):
    print(lyrics[i])
print("A partridge in a pair tree.")

print()

print("On the 2nd day of Christmas")
for i in range(2):
    print(lyrics[i])
for i in range(12, 11, -1):
    print(lyrics[i])

print()

print("On the 3rd day of Christmas")
for i in range(3):
    print(lyrics[i])
for i in range(12, 11, -1):
    print(lyrics[i])

print()

    
sys.exit(0)

