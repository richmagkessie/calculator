# Creating a simple calculator using python tkinter
# The python tkinter package is the standard python interface to the Tcl/Tk GUI toolkit
# import tkinter
from tkinter import Tk, Entry, Button, StringVar

# creating the calculator class
class Calculator:
    # function to define the screen
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        # This helps manage the value of the widget entry
        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17,bg='#ccc',font=('Aria Bold',28), textvariable=self.equation).place(x=0, y=0)

        # Buttons
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda:self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda:self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda:self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda:self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda:self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda:self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda:self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda:self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda:self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)

    # function to show numbers and operators on the form
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    # function to clear using the C button
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    # function to perform calculation
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


# creating instance of the class
root = Tk()
calculator = Calculator(root)

# keeping running loop of the app
root.mainloop()
