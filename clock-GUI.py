import time
from time import strftime
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('clock')

def clk():
    t=time.localtime(time.time())
    stringtime=f'{t.tm_hour} : {t.tm_min} : {t.tm_sec}'
    lbl.config(text=stringtime)
    lbl.after(1000,clk)

lbl=tk.Label(win,background='black',foreground='white',font=('arial',160))
lbl.grid(row=0,column=0)
clk()

win.mainloop()