from tkinter import * 
from tkinter.ttk import *
from time import strftime 


rage = Tk() 
rage.title("Clock")

def time():
    timestring = strftime("%H:%M:%S %p")
    label.config(text = timestring)
    label.after(1000, time)
    
label = Label(rage, font=("bernard-mt", 80), background="black", foreground="red")
label.pack(anchor = "center", expand=True, fill=BOTH)
time()

rage.mainloop()