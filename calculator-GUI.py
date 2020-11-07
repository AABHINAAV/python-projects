import tkinter as tk
from tkinter import ttk
# import math

main_application = tk.Tk()
main_application.title('calculator')

# x='1+2'
# print(eval(x))
frame1=tk.LabelFrame(main_application)
frame1.pack(side=tk.TOP)
########################################################################
result_var=tk.StringVar()
result=ttk.Entry(frame1,width=30,textvariable=result_var,state='readonly')
result.pack(side=tk.TOP,padx=10,pady=10)
#.......................................................................
frame2=tk.LabelFrame(main_application)
frame2.pack(side=tk.TOP,fill=tk.BOTH)
########################################################################
# function to write into the entry box
def write_to_entry(s):
    res=result_var.get()
    res=f'{res}{s}'
    result_var.set(res)
# + btn
plus_btn=tk.Button(frame2,text='+',command=lambda:write_to_entry('+'))
plus_btn.grid(row=0,column=0)
# - btn
minus_btn=tk.Button(frame2,text='-',command=lambda:write_to_entry('-'))
minus_btn.grid(row=0,column=1)
# x btn
mul_btn=tk.Button(frame2,text='x',command=lambda:write_to_entry('*'))
mul_btn.grid(row=0,column=2)
# / btn
div_btn=tk.Button(frame2,text='/',command=lambda:write_to_entry('/'))
div_btn.grid(row=0,column=3)

# 7 btn
seven_btn=tk.Button(frame2,text='7',command=lambda:write_to_entry('7'))
seven_btn.grid(row=1,column=0)
# 8 btn
eight_btn=tk.Button(frame2,text='8',command=lambda:write_to_entry('8'))
eight_btn.grid(row=1,column=1)
# 9 btn
nine_btn=tk.Button(frame2,text='9',command=lambda:write_to_entry('9'))
nine_btn.grid(row=1,column=2)
# clear all button
def remove_all_func():
    result_var.set('')
c_btn=tk.Button(frame2,text='C',command=remove_all_func)
c_btn.grid(row=1,column=3)

# 4 btn
four_btn=tk.Button(frame2,text='4',command=lambda:write_to_entry('4'))
four_btn.grid(row=2,column=0)
# 5 btn
five_btn=tk.Button(frame2,text='5',command=lambda:write_to_entry('5'))
five_btn.grid(row=2,column=1)
# 6 btn
six_btn=tk.Button(frame2,text='6',command=lambda:write_to_entry('6'))
six_btn.grid(row=2,column=2)
# remove last button
def delete_last_func():
    result_var.set(result_var.get()[0:-1])
del_btn=tk.Button(frame2,text='DEL',command=delete_last_func)
del_btn.grid(row=2,column=3)

# 1 btn
one_btn=tk.Button(frame2,text='1',command=lambda:write_to_entry('1'))
one_btn.grid(row=3,column=0)
# 2 btn
two_btn=tk.Button(frame2,text='2',command=lambda:write_to_entry('2'))
two_btn.grid(row=3,column=1)
# 3 btn
three_btn=tk.Button(frame2,text='3',command=lambda:write_to_entry('3'))
three_btn.grid(row=3,column=2)
# = btn with evaluation function
def evaluate():
    try:
        result_var.set(eval(result_var.get()))
    except:
        return
equal_btn=tk.Button(frame2,text='=',command=evaluate)
equal_btn.grid(row=3,column=3,rowspan=2)

# . btn
dot_btn=tk.Button(frame2,text='.',command=lambda:write_to_entry('.'))
dot_btn.grid(row=4,column=0)
# 0 btn
zero_btn=tk.Button(frame2,text='0',command=lambda:write_to_entry('0'))
zero_btn.grid(row=4,column=1)
# // btn
per_btn=tk.Button(frame2,text='mod',command=lambda:write_to_entry('//'))
per_btn.grid(row=4,column=2)

main_application.mainloop()

