import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

root = tk.Tk()
root.title('login page')
root.geometry('1200x768')


entry1=tk.StringVar()
entry2=tk.StringVar()
def login():
    if entry1.get()=='' or entry2.get()=='':
        mbox.showerror('ERROR','Please enter your Username and Password')
    else:
        mbox.showinfo('SUCCESSFUL','You have loged in successfully')

def reset_fileds():
    entry1.set('')
    entry2.set('')

def exit_win():
    if mbox.askyesno('exit','do you really want to exit?'):
        root.destroy()
    else:
        return

tk.Label(root,text='login system',font='arial 50 bold',fg='lime',relief=tk.RAISED,padx=30,pady=30).pack(side=tk.TOP)
tk.Label(root,text='Username',font=('times new roman',30,'bold'),fg='black').place(x=250,y=250)
tk.Label(root,text='Password',font=('times new roman',30,'bold'),fg='black').place(x=250,y=350)
e1 = tk.Entry(root,font=('arial 15'),fg='blue',relief=tk.GROOVE,textvariable=entry1).place(x=650,y=250)
e2 = tk.Entry(root,font=('arial 15'),fg='blue',relief=tk.GROOVE,textvariable=entry2,show='*').place(x=650,y=350)
tk.Button(root,text='LogIn',font='arial 25 bold',fg='crimson',bg='lime',relief=tk.RAISED,command=login).place(x=200,y=450)
tk.Button(root,text='Reset',font='arial 25 bold',fg='crimson',bg='lime',relief=tk.RAISED,command=reset_fileds).place(x=450,y=450)
tk.Button(root,text='Exit',font='arial 25 bold',fg='crimson',bg='lime',relief=tk.RAISED,command=exit_win).place(x=700,y=450)

root.mainloop()