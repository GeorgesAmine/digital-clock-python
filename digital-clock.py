# This program creates a GUI of a digital clock showing current time

# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# importing date to retrieve 
# today's date and time
from datetime import datetime

# creating tkinter window
root = Tk()
root.title('Digital Clock')

# this function is used to display
# time on the label
def time():
    now = datetime.now()
    string = now.strftime('%H:%M:%S %p')
    lbl_time.config(text = string)
    lbl_time.after(1000,time)

# this function is used to display
# today's date me on the label
def date():
    today = datetime.today()
    string = today.strftime("%B %d, %Y")
    lbl_date.config(text = string)

# Styling the label widget so that clock
# will look more attractive
lbl_time = Label(root, 
            font= ('calibri', 40,'bold'),
            background = 'white',
            foreground = 'black')

# Styling the label widget so that date
# will look more attractive
lbl_date = Label(root, 
            font= ('calibri', 40,'bold'),
            background = 'white',
            foreground = 'black')

# Placing clock at the center of tkinter window
lbl_time.pack(anchor = 'center')
# Placing date on the bottom
lbl_date.pack(anchor = 's')
time()
date()

mainloop()