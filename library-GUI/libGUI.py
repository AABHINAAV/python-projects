import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictReader, DictWriter
import os
import time

############## GUI initialisation
root = tk.Tk()
root.title('library gui')
root.geometry('1000x600+200+70')
############################################################ heading label
tk.Label(text='welcome to python gui powered library system',font='arial 30 bold',fg='red',bg='yellow').pack(side=tk.TOP,padx=20,pady=20)

    # main GUI####
############################################################ notebook
options = ttk.Notebook(root)
options.pack(side=tk.TOP,expand=True,fill='both')


############################################################ frames variables
add_book_frame = ttk.Frame(options)
delete_book_frame = ttk.Frame(options)
show_book_frame = ttk.Frame(options)
issue_book_frame = ttk.Frame(options)
return_book_frame = ttk.Frame(options)
show_all_data_frame = ttk.Frame(options)

##### adding frames to notebook
frame_dict={
    add_book_frame:'ADD BOOK',
    delete_book_frame:'DELETE BOOK',
    show_book_frame:'SHOW BOOK',
    issue_book_frame:'ISSUE BOOK',
    return_book_frame:'RETURN BOOK',
    show_all_data_frame:'SHOW ALL DATA'
}
for frame_var,frame_name in frame_dict.items():
    options.add(frame_var,text = frame_name)


####################################################### add book frame
    # central frame ----->
f1 = tk.LabelFrame(add_book_frame)
f1.pack(side=tk.TOP,pady=30)

    # label ----->
tk.Label(f1,text='Enter the Book Id = ').grid(row=0,column=0,padx=10,pady=10)
    # book id entry field ----->
add_book_frame_id=tk.Entry(f1,width=30)
add_book_frame_id.grid(row=0,column=1,padx=10,pady=10)
    
    # label ----->
tk.Label(f1,text='Enter the Book Name = ').grid(row=1,column=0,padx=10,pady=10)
    # book name entry field ----->
add_book_frame_name=tk.Entry(f1,width=30)
add_book_frame_name.grid(row=1,column=1,padx=10,pady=10)

    # add book button ----->
add_book_frame_btn=tk.Button(add_book_frame,text='Add Book',font='arial 20 bold')
add_book_frame_btn.pack(side=tk.TOP,padx=20,pady=20)

    # add book status label ----->
add_book_frame_sts=tk.Label(add_book_frame)
add_book_frame_sts.pack(side=tk.TOP,padx=10,pady=10)


####################################################### delete book frame
    # central frame ----->
f2 = tk.LabelFrame(delete_book_frame)
f2.pack(side=tk.TOP,pady=30)

    # label ----->
tk.Label(f2,text='Enter the Book Id = ').grid(row=0,column=0,padx=10,pady=10)
    # book id entry field ----->
delete_book_frame_id=tk.Entry(f2,width=30)
delete_book_frame_id.grid(row=0,column=1,padx=10,pady=10)

    # delete book button ----->
delete_book_frame_btn=tk.Button(delete_book_frame,text='Delete Book',font='arial 20 bold')
delete_book_frame_btn.pack(side=tk.TOP,padx=20,pady=20)

    # delete book status label ----->
delete_book_frame_sts=tk.Label(delete_book_frame)
delete_book_frame_sts.pack(side=tk.TOP,padx=10,pady=10)


####################################################### show book frame
    # show button ----->
show_book_frame_btn=tk.Button(show_book_frame,text='Show Books')
show_book_frame_btn.pack(side=tk.TOP,padx=20,pady=20)

    #text field ----->
show_book_frame_result=tk.Text(show_book_frame,font='arial 14 bold',height=23,width=70,bg='pink')
show_book_frame_result.pack(side=tk.TOP,padx=10,pady=10)


####################################################### issue book frame
    # central frame ----->
f4 = tk.LabelFrame(issue_book_frame)
f4.pack(side=tk.TOP,pady=30)

    # label ----->
tk.Label(f4,text='Enter the Book Id = ').grid(row=0,column=0,padx=10,pady=10)
    # book id entry field ----->
issue_book_frame_id=tk.Entry(f4,width=30)
issue_book_frame_id.grid(row=0,column=1,padx=10,pady=10)

    # label ----->
tk.Label(f4,text='Enter the Student Id = ').grid(row=1,column=0,padx=10,pady=10)
    # book id entry field ----->
issue_book_frame_StdId=tk.Entry(f4,width=30)
issue_book_frame_StdId.grid(row=1,column=1,padx=10,pady=10)

    # label ----->
tk.Label(f4,text='Enter the Student Name = ').grid(row=2,column=0,padx=10,pady=10)
    # book id entry field ----->
issue_book_frame_StnName=tk.Entry(f4,width=30)
issue_book_frame_StnName.grid(row=2,column=1,padx=10,pady=10)

    # issue book button ----->
issue_book_frame_btn=tk.Button(issue_book_frame,text='Issue Book',font='arial 20 bold')
issue_book_frame_btn.pack(side=tk.TOP,padx=20,pady=20)

    # issue book status label ----->
issue_book_frame_sts=tk.Label(issue_book_frame)
issue_book_frame_sts.pack(side=tk.TOP,padx=10,pady=10)


####################################################### return book frame
    # central frame ----->
f5 = tk.LabelFrame(return_book_frame)
f5.pack(side=tk.TOP,pady=30)

    # label ----->
tk.Label(f5,text='Enter the Book Id = ').grid(row=0,column=0,padx=10,pady=10)
    # book id entry field ----->
return_book_frame_id=tk.Entry(f5,width=30)
return_book_frame_id.grid(row=0,column=1,padx=10,pady=10)

    # label ----->
tk.Label(f5,text='Enter the Student Id = ').grid(row=1,column=0,padx=10,pady=10)
    # book id entry field ----->
return_book_frame_StdId=tk.Entry(f5,width=30)
return_book_frame_StdId.grid(row=1,column=1,padx=10,pady=10)

    # label ----->
tk.Label(f5,text='Enter the Student Name = ').grid(row=2,column=0,padx=10,pady=10)
    # book name entry field ----->
return_book_frame_StnName=tk.Entry(f5,width=30)
return_book_frame_StnName.grid(row=2,column=1,padx=10,pady=10)

    # return book button ----->
return_book_frame_btn=tk.Button(return_book_frame,text='Return Book',font='arial 20 bold')
return_book_frame_btn.pack(side=tk.TOP,padx=20,pady=20)

    # return book status label ----->
return_book_frame_sts=tk.Label(return_book_frame)
return_book_frame_sts.pack(side=tk.TOP,padx=10,pady=10)


####################################################### show all data frame
    # central frame ----->
f6 = tk.LabelFrame(show_all_data_frame)
f6.pack(side=tk.TOP,pady=30)

    # label ----->
tk.Label(f6,text='Id : ').grid(row=0,column=0,padx=10,pady=10)
    # librarian id entry field ----->
show_all_data_frame_id=tk.Entry(f6,width=30)
show_all_data_frame_id.grid(row=0,column=1,padx=10,pady=10)
    
    # label ----->
tk.Label(f6,text='Password : ').grid(row=1,column=0,padx=10,pady=10)
    # password entry field ----->
show_all_data_frame_pswd=tk.Entry(f6,width=30,show='#')
show_all_data_frame_pswd.grid(row=1,column=1,padx=10,pady=10)

    # Show all data button ----->
show_all_data_frame_btn=tk.Button(show_all_data_frame,text='Authorise And Show',font='arial 20 bold')
show_all_data_frame_btn.pack(side=tk.TOP,padx=10,pady=10)

    # Show all data text area ----->
show_all_data_frame_result=tk.Text(show_all_data_frame,font='arial 14 bold',height=23,width=70,bg='pink')
show_all_data_frame_result.pack(side=tk.TOP,padx=10,pady=10)



###################### functionality using class
class library:
    filename = 'lib.csv'
    exist = False

    # funciton to check file exist or not-----
    def add_book_func(self):
        add_book_frame_sts['text']=''
        if(not(os.path.exists(self.filename))):
            with open(self.filename, 'a+') as lib:
                filewriter = DictWriter(lib, fieldnames=['BookName', 'BookId', 'Date', 'IssueStatus'])
                filewriter.writeheader()
        self.addData()
    # adding data for lib-----
    def addData(self):
        with open(self.filename, 'a+') as lib:
            filewriter = DictWriter(lib, fieldnames=['BookName', 'BookId', 'Date', 'IssueStatus'])
            bookid = add_book_frame_id.get()
            bookname = add_book_frame_name.get()
            filewriter.writerow({
                'BookName': bookname.upper(),
                'BookId': bookid.upper(),
                'Date': time.asctime(time.localtime(time.time())),
                'IssueStatus': 'not issued'
            })
        add_book_frame_sts['text']='Book Added To Library Successfully'

    # to delete the data of an existing and unissued book-----
    def delete_book_func(self):
        delete_book_frame_sts['text']=''
        bookid = delete_book_frame_id.get()
        with open(self.filename) as rf:
            with open('tempfile.csv', 'a') as wf:
                data = DictReader(rf)
                updatedFile = DictWriter(wf, fieldnames=['BookName', 'BookId', 'Date', 'IssueStatus'])
                updatedFile.writeheader()
                for row in data:
                    if row['BookId'] == bookid.upper():
                        self.exist=True
                        if row['IssueStatus'] == 'not issued':
                            delete_book_frame_sts['text']=f'BookName : {row["BookName"]}\nBookId : {row["BookId"]}\nData Of This Book Has Been Deleted Sucessfully.....'
                        else:
                            delete_book_frame_sts['text']=f'Sorry Can\'t Delete This Book Data Because It Is Currently Issued By {row["IssueStatus"]}'
                            updatedFile.writerow({
                                'BookName': row['BookName'],
                                'BookId': row['BookId'],
                                'Date': row['Date'],
                                'IssueStatus': row['IssueStatus']
                            })
                    else:
                        updatedFile.writerow({
                            'BookName': row['BookName'],
                            'BookId': row['BookId'],
                            'Date': row['Date'],
                            'IssueStatus': row['IssueStatus']
                        })
        if self.exist == False:
            delete_book_frame_sts['text']=f'Sorry... Shere Is No Such Book With Book Id "{bookid}" In Our Library'
        os.remove(self.filename)
        os.rename('tempfile.csv',self.filename)
        self.exist == False


    #function to show books name-----
    def show_book_func(self):
        show_book_frame_result.delete(1.0,tk.END)
        with open(self.filename,'r') as fr:
            data = DictReader(fr)
            for row in data:
                show_book_frame_result.insert(tk.END,f'\n\t{row["BookName"]}')


    # function to issue book to student-----
    def issue_book_func(self):
        issue_book_frame_sts['text']=''
        bookid = issue_book_frame_id.get()
        with open(self.filename, 'r') as rf:
            with open('tempfile.csv', 'a') as wf:
                data = DictReader(rf)
                updatedFile = DictWriter(wf, fieldnames=['BookName', 'BookId', 'Date', 'IssueStatus'])
                updatedFile.writeheader()
                for row in data:
                    if row['BookId'] == bookid.upper():
                        self.exist = True
                        if row['IssueStatus'] == 'not issued':
                            studentId = issue_book_frame_StdId.get()
                            studentName = issue_book_frame_StnName.get()
                            studentInfo = (studentId + '--' + studentName).upper()
                            updatedFile.writerow({
                                'BookName': row['BookName'],
                                'BookId': row['BookId'],
                                'Date': time.asctime(time.localtime(time.time())),
                                'IssueStatus': studentInfo
                            })
                            issue_book_frame_sts['text']='Book Has Been Successfully Issued To You'
                        else:
                            issue_book_frame_sts['text']=f'Book with id \'{bookid}\' Is Already Issued To Someone Else'
                            updatedFile.writerow({
                                'BookName': row['BookName'],
                                'BookId': row['BookId'],
                                'Date': row['Date'],
                                'IssueStatus': row['IssueStatus']
                            })
                    else:
                        updatedFile.writerow({
                            'BookName': row['BookName'],
                            'BookId': row['BookId'],
                            'Date': row['Date'],
                            'IssueStatus': row['IssueStatus']
                        })
            if not(self.exist):
                issue_book_frame_sts['text']='There Is No Such Book'
            os.remove(self.filename)
            os.rename('tempfile.csv', self.filename)
            self.exist=False


    # to return book-----
    def return_book_func(self):
        return_book_frame_sts['text']=''
        bookid = return_book_frame_id.get()
        studentId = return_book_frame_StdId.get()
        studentName = return_book_frame_StnName.get()
        studentInfo = (studentId + '--' + studentName).upper()
        with open(self.filename, 'r') as rf:
            with open('tempfile.csv', 'a') as wf:
                data = DictReader(rf)
                updatedFile = DictWriter(wf, fieldnames=['BookName', 'BookId', 'Date', 'IssueStatus'])
                updatedFile.writeheader()
                for row in data:
                    if row['BookId'] == bookid.upper():
                        self.exist=True
                        if row['IssueStatus'] == studentInfo:
                            return_book_frame_sts['text']=f"{row['BookName']} Is Being Issued By:- \nStudent Name : {studentName}\nStudent Id : {studentId}\nThe Book Is Sucessfully Returned....."
                            updatedFile.writerow({
                                'BookName': row['BookName'],
                                'BookId': row['BookId'],
                                'Date': time.asctime(time.localtime(time.time())),
                                'IssueStatus': 'not issued'
                            })
                        else:
                            if row['IssueStatus'] == 'not issued':
                                return_book_frame_sts['text']=f"This Book Is Not Issued By You....."
                            else:
                                return_book_frame_sts['text']=f"This Book Is Issued By Someone Else"
                            updatedFile.writerow({
                                'BookName': row['BookName'],
                                'BookId': row['BookId'],
                                'Date': row['Date'],
                                'IssueStatus': row['IssueStatus']
                            })
                    else:
                        updatedFile.writerow({
                            'BookName': row['BookName'],
                            'BookId': row['BookId'],
                            'Date': row['Date'],
                            'IssueStatus': row['IssueStatus']
                        })
            if not(self.exist):
                return_book_frame_sts['text']=f'There Is No Such Book With Book Id "{bookid}" In Library'
            os.remove(self.filename)
            os.rename('tempfile.csv',self.filename)
            self.exist=False


    # to show data of all books-----
    def show_all_data_func(self):
        show_all_data_frame_result.delete(1.0,tk.END)
        authorised_personal=False
        libId = show_all_data_frame_id.get()
        libpswd = show_all_data_frame_pswd.get()
        if libId=='' or libpswd=='':
            m_box.showerror('Log-In Error','Please Enter The Both Id and Password')
        else:
            with open('libraryId.csv','r') as fr:
                data = DictReader(fr)
                for row in data:
                    if(libId==row['id'] and libpswd==row['password']):
                        authorised_personal=True
                        show_all_data_frame_result.insert(1.0,f'\n\tHello, {row["name"]}\n\t{"-"*50}')
                        self.printData()
                if not(authorised_personal):
                    m_box.showerror('Log-In Error','Invalid User-Id or Password')
    def printData(self):
        with open('lib.csv','r') as fr:
            data = DictReader(fr)
            for row in data:
                show_all_data_frame_result.insert(tk.END,f'\n\n\tBook Id : {row["BookId"]}\t\tBook Name : {row["BookName"]}\n\tDate : {row["Date"]}\n\tIssueStatus : {row["IssueStatus"]}\n\t{"-"*50}')



################ main function
if __name__ == "__main__":
    obj = library()
    add_book_frame_btn['command']=obj.add_book_func
    delete_book_frame_btn['command']=obj.delete_book_func
    show_book_frame_btn['command']=obj.show_book_func
    issue_book_frame_btn['command']=obj.issue_book_func
    return_book_frame_btn['command']=obj.return_book_func
    show_all_data_frame_btn['command']=obj.show_all_data_func


root.mainloop()

                                         #### purn viram #