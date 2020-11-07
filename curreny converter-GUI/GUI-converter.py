import tkinter as tk
from tkinter import ttk

data={}
with open('data.txt','r') as fr:
    lines = fr.readlines()

for line in lines:
    rawData=line.split('\t')
    data[rawData[0]] = rawData[2]

currencyNames=[]
currencyNames.append('INDIAN RUPEES')
currencyNames.extend([i for i in data])

#################################################
###################### GUI ######################
#################################################
# main window
main_application = tk.Tk()
main_application.title('Currency Converter')
main_application.geometry('500x400+400+150')

# Label Frame for old currency
cur1_frame=ttk.LabelFrame(main_application,text='select your current currency')
cur1_frame.pack(side=tk.TOP,fill=tk.X,padx=5,pady=10)

###########################
# input list for old currency
cur1_var=tk.StringVar()
cur1_select = ttk.Combobox(cur1_frame,width=30,state='readonly',textvariable=cur1_var)
cur1_select.pack(side=tk.TOP,padx=5,pady=10)
cur1_select['values']=currencyNames
cur1_select.current(0)

# label for old currency
cur1_lbl = ttk.Label(cur1_frame,text='Enter your currency : ')
cur1_lbl.pack(side=tk.LEFT,padx=30)

# entry box for old currency
cur1_entry_var = tk.IntVar()
cur1_entry=ttk.Entry(cur1_frame,width=30,textvariable=cur1_entry_var)
cur1_entry.pack(side=tk.TOP,pady=10)

# Label Frame for new currency
cur2_frame=ttk.LabelFrame(main_application,text='select new currency ')
cur2_frame.pack(side=tk.TOP,fill=tk.X,padx=5,pady=10)

###########################
# input list for new currency
cur2_var=tk.StringVar()
cur2_select = ttk.Combobox(cur2_frame,width=30,state='readonly',textvariable=cur2_var)
cur2_select.pack(side=tk.TOP,padx=5,pady=10)
cur2_select['values']=currencyNames
cur2_select.current(0)

# button.....................................
# working of convert button
def convertCurrencyFun():
    try:
        old_currency=cur1_var.get()
        new_currency=cur2_var.get()
        oldAmount=cur1_entry_var.get()

        if old_currency == 'INDIAN RUPEES':
            if new_currency == 'INDIAN RUPEES':
                newAmount=oldAmount
            else:
                newAmount = oldAmount/float(data[new_currency])
        else:
            # firstly converting into rupees-----
            mid = oldAmount*float(data[old_currency])

            # checking if want to convert into currency other than rupees-----
            if new_currency == 'INDIAN RUPEES':
                newAmount = mid
            else:
                newAmount = mid/float(data[new_currency])
        result_frame.pack(side=tk.TOP,fill=tk.BOTH,padx=10,pady=30)
        result_label.config(text=f'your {oldAmount} in {old_currency} \nis equal to \n{newAmount} in {new_currency}')
    except:
        return

    # convert button
btn=ttk.Button(main_application,text='CONVERT',command=convertCurrencyFun)
btn.pack(side=tk.TOP,padx=5,pady=10)

# result frame
result_frame = ttk.LabelFrame(main_application,text='Result')

# result label
result_label=ttk.Label(result_frame)
result_label.pack(anchor='center')
main_application.mainloop()