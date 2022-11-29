from tkinter import *
import tkinter.messagebox

import time
import sys

arguments = sys.argv[1:]


time_to_sleep = int(arguments[0])
if arguments[1].lower() in ["s", "sec", "seconds", "secs"]:
    pass
elif arguments[1].lower() in ["m", "min", "minutes", "mins"]:
    time_to_sleep = time_to_sleep * 60

time.sleep(time_to_sleep)
root = tkinter.Tk()
root.bell()
root.withdraw()
tkinter.messagebox.showinfo("Timer finished", "Your " + arguments[0] + arguments[1] + " timer ended.")





