### all functions

def addstudent():
    # def submitadd():
    #     id = entry1.get()
    #     name = entry2.get()
    #     mobile = entry3.get()
    #     email = entry4.get()
    #     address = entry5.get()
    #     if id and name and mobile and email and address:
    #         messagebox.showinfo("Success", "Student added successfully!")
    #         add.destroy()
    #     else:
    #         messagebox.showerror("Error", "Please fill all fields!")
    # global add
    # if 'add' in globals():
    #     add.destroy()
    # if 'add' in locals():
    #     add.destroy()

    add= Toplevel(master=DataEntryFrame)
    add.grab_set()
    add.title("Add Student")
    add.geometry("500x400+400+200")
    add.iconbitmap("academic.png")
    add.config(bg="grey")
    add.resizable(False, False)
    add1= Label(add, text='Enter ID:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w',borderwidth=3, relief=GROOVE)
    add1.place(x=10, y=10)
    add2= Label(add, text='Enter Name:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add2.place(x=10, y=60)
    add3= Label(add, text='Enter Mobile:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add3.place(x=10, y=110)
    add4= Label(add, text='Enter Email:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add4.place(x=10, y=160)
    add5= Label(add, text='Enter Address:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add5.place(x=10, y=210)
    add6= Label(add, text='Enter Gender:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add6.place(x=10, y=260)
    add7= Label(add, text='Enter D.O.B:', font=("arial", 15, "bold"), width=15, fg="black", anchor='w', borderwidth=3, relief=GROOVE)
    add7.place(x=10, y=310)
    namevalue= StringVar()
    agevalue= StringVar()
    classvalue= StringVar()
    rollvalue= StringVar()
    entry1= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=namevalue)
    entry1.place(x=200, y=10)
    entry2= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=agevalue)
    entry2.place(x=200, y=60)
    entry3= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=classvalue)
    entry3.place(x=200, y=110)
    entry4= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=rollvalue)
    entry4.place(x=200, y=160)
    entry5= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=rollvalue)
    entry5.place(x=200, y=210)
    entry6= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=rollvalue)
    entry6.place(x=200, y=260)
    entry7= Entry(add, font=("arial", 12, "bold"), width=25, bd=3, textvariable=rollvalue)
    entry7.place(x=200, y=310)
    
    submitbutton= Button(add, text='Submit', width=10, height=1, font=("arial", 10, "bold"), relief=RIDGE, bg="darkred", fg="white", activebackground='red', activeforeground='white', bd=5)
    submitbutton.place(x=200, y=360)
                        
def findstudent():
    print("student found successfully")

def deletestudent():
    print("student deleted successfully")

def updatestudent():
    print("student updated successfully")

def showallstudents():
    print("showing all students")

def exportdata():
    print("data exported successfully")

def exitapp():
    exitwindow= messagebox.askyesnocancel('Notification', 'Do you want to exit the application?')
    if (exitwindow == True):
        a.destroy() 





### connectdatabase
def Connectdb():
    b= Toplevel()
    b.grab_set() 
    b.title("Database Connection")
    b.geometry("400x220+400+200")
    b.iconbitmap("academic.png")
    b.config(bg="lightgrey")
    b.resizable(False, False)

    label1= Label(b,text='Enter Host :', font=("arial", 15, "bold"),width=15, fg="black", anchor='w')
    label1.place(x=10, y=10)
    label2= Label(b,text='Enter Username :', font=("arial", 15, "bold"), width=15,fg="black", anchor='w')
    label2.place(x=10, y=60)
    label3= Label(b,text='Enter Password :', font=("arial", 15, "bold"), width=15,fg="black", anchor='w')
    label3.place(x=10, y=110)

    hostvalue= StringVar()
    usernamevalue= StringVar()
    passwordvalue= StringVar()

    entry1= Entry(b, font=("arial", 10, "bold"), width=25, bd=3, textvariable=hostvalue)
    entry1.place(x=200, y=10)
    entry2= Entry(b, font=("arial", 10, "bold"), width= 25, bd=3, textvariable=usernamevalue)
    entry2.place(x=200, y=60)
    entry3= Entry(b, font=("arial", 10, "bold"), width= 25,bd=3, show='*', textvariable=passwordvalue)
    entry3.place(x=200, y=110)

    submitbutton= Button(b, text='Submit', width=10, height=1, font=("arial", 10, "bold"), relief=RIDGE, bg="darkred", fg="white", activebackground='red', activeforeground='white', bd=5)
    submitbutton.place(x=150, y=160) 
    b.mainloop()

### clock update function
def update_clock():
    time_string = time.strftime('%H:%M:%S %p')
    date_string = time.strftime('%d/%m/%Y')
    clock.config(text='Date: ' + date_string + '\nTime: ' + time_string)
    clock.after(200, update_clock) 

### colorful slider
import random
color_list = ["black", "red","blue","green"]
def Color():
    fg = random.choice(color_list)
    SliderLabel.config(fg=fg)
    SliderLabel.after(150, Color)
def Welcome():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:   
        text += ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, Welcome)


### studentmanagementsystem.py
from tkinter import *
import time
from tkinter import Toplevel, messagebox
a=Tk()
a.title("Student Management System")
a.config(bg="black")
a.geometry("1100x600+100+50")
a.iconbitmap("academic.png")
a.resizable(False, False)

### LEFT Frame
DataEntryFrame = Frame(a, bg="beige", bd=5, relief=GROOVE)
DataEntryFrame.place(x=10, y=70, width=400, height=460)
lf1 = Label(DataEntryFrame, text="----------------WELCOME----------------", font=("chiller", 25, "bold"), bg="beige", fg="black")
lf1.pack(expand=True, fill=BOTH)
addbtn = Button(DataEntryFrame, text="1. Add Student", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=addstudent)
addbtn.pack(side=TOP, expand=True)

Findbtn = Button(DataEntryFrame, text="2. Find Student", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=findstudent)
Findbtn.pack(side=TOP, expand=True)

Deletebtn = Button(DataEntryFrame, text="3. Delete Student", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE,command=deletestudent)
Deletebtn.pack(side=TOP, expand=True)

Updatebtn = Button(DataEntryFrame, text="4. Update Student", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=updatestudent)
Updatebtn.pack(side=TOP, expand=True)

Showallbtn = Button(DataEntryFrame, text="5. Show All", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=showallstudents)
Showallbtn.pack(side=TOP, expand=True)

Exportbtn = Button(DataEntryFrame, text="6. Export Data", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=exportdata)
Exportbtn.pack(side=TOP, expand=True)

Exitbtn = Button(DataEntryFrame, text="7. Exit", font=("arial", 12, "bold"), bg="lightgrey", fg="black", width=20, bd=5, relief=RIDGE, command=exitapp)
Exitbtn.pack(side=TOP, expand=True)

### RIGHT Frame
ShowDataFrame = Frame(a, bg="beige", bd=5, relief=GROOVE)
ShowDataFrame.place(x=420, y=70, width=660, height=460)

### Slider
ss= 'Student Management System'
count=0
text=''
SliderLabel = Label(a, text= ss, font=("Arial", 30, "bold"),relief=RIDGE,bd=4, width=30, bg="lightgrey", fg="black")
SliderLabel.place(x=200, y=0)
Welcome()
Color()

### clock
clock=Label(a, text="", font=("times", 10, "bold"), bg="lightgrey", fg="black", width=17, height=3)
clock.place(x=4, y=0)
update_clock()

### ConnectDatabaseButtons
connectbutton= Button(a,text='Connect to Database',width=16, height=3, font=("arial", 10, "bold"), relief=RIDGE, bg="darkred", fg="white", activebackground='red', activeforeground='white', command=Connectdb)
connectbutton.place(x=958, y=0) 


a.mainloop()