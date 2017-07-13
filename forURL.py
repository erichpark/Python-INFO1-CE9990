"""
forURL.py

Eric Park
INFO1-CE9990 Section 2
Homework for July 6, 2017

Script that converts bytes to strings that are then displayed in all lower-case letters.

"""

import sys
import urllib.request

url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

for line in lines:
    try:
        s = line.decode("utf-8") #Convert sequence of bytes to string of characters.
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    print(str.casefold(s), end = "")           #s already ends with a newline.

lines.close()
sys.exit(0)
