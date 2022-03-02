from tkinter import *
from tkinter.ttk import *
from datetime import date,time,datetime
import pytz
from time import strftime

root = Tk()
root.title("Mara Tan tan")

def clock():
    tic = pytz.timezone("Asia/Kolkata")
    tic = datetime.now(tic)
    tic = tic.strftime("%H:%M:%S %p")
    label.config(text=tic)
    label.after(1000,clock)
label = Label(root,font =("sans",60),background="blue",foreground="Black")
label.pack(anchor="center")
clock()
mainloop()
    
