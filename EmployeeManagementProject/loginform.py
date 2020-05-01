from tkinter import *
import os
import tkinter.messagebox as MessageBox
import pymysql

def validation():
    con = pymysql.connect(host='localhost',user='root',password='',database='employeemanagement')
    cur = con.cursor()
    username = e_user.get()
    password = e_pass.get()

    if(username == "" or password == ""):
        MessageBox.showinfo("Fetch Status","All fields are required")
    else:
        q = "SELECT * FROM login WHERE username = '" +username+ "' and password = '" +password+ "'"
        #Execute Cursor asb pass query of EMPLOYEE and data of Employee
        cur.execute(q)
        
        rows = cur.fetchall()
        for row in rows:
            os.system('python EMPLOYEE.py')
        con.close()

login_window = Tk()
login_window.title("EMPLOYEE MANAGEMENT SYSTEM")
login_window.geometry("400x300")
Label(login_window, text = 'Please enter login detail',width=400,height=2,bg='red').pack()
Label(login_window, text = "").pack()
Label(login_window, text = 'username',width=15,height=2).pack()
e_user = Entry(login_window)
e_user.pack()
Label(login_window,text="").pack()
Label(login_window,text="password",width=15,height=2).pack()
e_pass = Entry(login_window, show= "*")
e_pass.pack()
Label(login_window, text="").pack()
Button(login_window, text = 'Login',bg='yellow', width=10,height=1,command=validation).pack()
login_window.mainloop()


