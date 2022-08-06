# This program creates a GUI of a digital clock showing current time

# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# importing strftime to
# retreive system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Digital Clock')

# this function is used to display
# time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000,time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, 
            font= ('calibri', 40,'bold'),
            background = 'white',
            foreground = 'black')

# Placing clock at the center of tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()