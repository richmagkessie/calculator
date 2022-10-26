# This program simulates a digital watch

# Making imports
from tkinter import *
from tkinter.ttk import *
from time import strftime

# defining screen
top = Tk()
top.title('Digital Clock')

# Function
def none():
    text = strftime(' %H:%M:%S:%p ')
    lbl.config(text = text)
    lbl.after(1000, none)

# defining the background
lbl = Label(top, font=('digital-7', 50, 'bold'),
        background='white', foreground='blue')

#
lbl.pack(anchor='center')
# calling the none() function
none()
# looping the screen
mainloop()
