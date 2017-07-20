"""
restaurant.py

Eric Park
INFO1-CE9990 Section 2
Homework for July 13, 2017

Data Source: DOHMH New York City Restaurant Inspection Results

Output all restaurants, located in Williamsburg (BROOKLYN!), with an Inspection Grade of 'A'

"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.
import urllib.request

url = "https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv" \
    "?accessType=DOWNLOAD"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

brooklynLines = []                   #Start with an empty list.

for line in lines:
    try:
        s = line.decode("utf-8")    #s is a string
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    r = csv.reader([s])                           #[s] is a list containing one string
    fields = next(r)                              #fields is a list of strings
    if fields[5] == "11211" and fields[14] == "A" and fields[8] >= "1/01/2017": #Zip code for Williamsburg; Inspection Grade of 'A'; Inspection Date in 2017 
        brooklynLines.append(fields)

lines.close()

for line in brooklynLines:
    print(line[1], line[8])              #name and inspection date
    print("Cuisine:", line[7])           #cuisine
    print("Inspection Grade:", line[14]) #inspection grade
    print()

print()

sys.exit(0)
