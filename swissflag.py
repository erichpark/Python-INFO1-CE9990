"""
swissflag.py

Eric Park
INFO1-CE9990 Section 2
Homework for June 29, 2017

According to Wikipedia, the flag of Switzerland is one of only two
square soverign-state flags, the other being the flag of Vatican City.

"""

import tkinter              

root = tkinter.Tk()
root.title("Flag of Switzerland")

#dimensions of flag, in pixels
height = 400  
width = 400
root.geometry(str(width) + "x" + str(height))

#flag colors
SwissRed    = "#FF0000"
SwissWhite  = "#FFFFFF"

canvas = tkinter.Canvas(root, highlightthickness = 0,
    background = SwissRed)

def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

for y in range(height):
    for x in range(width):

        #If this point is within the vertical bar or within the horizontal bar,
        if width * 13/32 <= x and x <= width * 19/32 and height * 6/32 <= y and y <= height * 26/32 \
        or width * 6/32 <= x and x <= width * 26/32 and height *13/32 <= y and y <= height * 19/32:
            drawPixel(x, y, SwissWhite)         

canvas.pack(expand = tkinter.YES, fill = "both")
