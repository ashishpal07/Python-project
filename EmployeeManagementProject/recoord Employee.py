import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql


# -------------ADD DETAILS-------------------------------------------------------------------------------------------------------

def createNewWindow():
    def insert():
        empid = e_id.get()
        empname = e_name.get();
        phone = e_phone.get();
        dept = e_dept.get();
        address = e_add.get();
        salary = e_sal.get();

        if (empid == "" or empname == "" or phone == "" or dept == "" or address == ""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="employeemanagement")
            cursor = con.cursor()
            cursor.execute("INSERT INTO EMPLOYEE values('" +empid+ "','" +empname+ "','" +phone+ "','" +dept+ "','" +address+ "','" +salary+ "')")
            cursor.execute("commit");

            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_dept.delete(0, 'end')
            e_add.delete(0, 'end')
            e_sal.delete(0, 'end')
            show()
            
            MessageBox.showinfo("Insert Status", "Inserted Successfully");
            con.close();

    newWindow = tk.Toplevel(app)
    newWindow.geometry("600x400")
    newWindow.title("Registration Wnindow")
    
    empid = tk.Label(newWindow, text="Enter employee id : ", font=("bold", 10))
    empid.place(x=30, y=50)
    empname = Label(newWindow, text="Enter employee name : ", font=("bold", 10))
    empname.place(x=30, y=90)
    phone = Label(newWindow, text="Enter Phone Number : ", font=("bold", 10))
    phone.place(x=30, y=130)
    dept = Label(newWindow, text="Enter Department : ", font=("bold", 10))
    dept.place(x=30, y=170)
    address = Label(newWindow, text="Enter Address : ", font=("bold", 10))
    address.place(x=30, y=210)
    salary = Label(newWindow, text="Enter Salary : ", font=("bold", 10))
    salary.place(x=30, y=250)
    
    e_id = tk.Entry(newWindow)
    e_id.place(x=170, y=50)
    e_name = tk.Entry(newWindow)
    e_name.place(x=170, y=90)
    e_phone = tk.Entry(newWindow)
    e_phone.place(x=170, y=130)
    e_dept = tk.Entry(newWindow)
    e_dept.place(x=170, y=170)
    e_add = tk.Entry(newWindow)
    e_add.place(x=170, y=210)
    e_sal = tk.Entry(newWindow)
    e_sal.place(x=170, y=250)

    
    labelExample = tk.Label(newWindow, text="Enter your Details",bg='red',width=600,height=2)
    labelExample.pack()
    
    buttonExample = tk.Button(newWindow, text="ADD", command=insert,bg='pink',width=10,height=2)
    buttonExample.place(x=250,y=280)
    

# --------------------D E L E T E----------------------------------------------------------------------------------------------------


def createNewWindow1():
    def delete():
        if (e_id.get() == ""):
            MessageBox.showinfo("Delete Status", "please Enter Valid id")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="employeemanagement")
            cursor = con.cursor()
            cursor.execute("DELETE from EMPLOYEE where empid='" + e_id.get() + "'")
            cursor.execute("commit");

            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_dept.delete(0, 'end')
            e_add.delete(0, 'end')
            e_sal.delete(0, 'end')
            show()
            
            MessageBox.showinfo("Delete Status", "deleted Successfully");
            con.close();

    newWindow = tk.Toplevel(app)
    newWindow.title("Delete Window")
    newWindow.geometry("600x400")

    empid = tk.Label(newWindow, text="Enter employee id : ", font=("bold", 10))
    empid.place(x=30, y=50)
    empname = Label(newWindow, text="Enter Full Name: ", font=("bold", 10))
    empname.place(x=30, y=90)
    phone = Label(newWindow, text="Enter Mobile Number: ", font=("bold", 10))
    phone.place(x=30, y=130)
    dept = Label(newWindow, text="Enter Department : ", font=("bold", 10))
    dept.place(x=30, y=170)
    address = Label(newWindow, text="Enter Address : ", font=("bold", 10))
    address.place(x=30, y=210)
    salary = Label(newWindow, text="Enter Salary : ", font=("bold", 10))
    salary.place(x=30, y=250)


    e_id = tk.Entry(newWindow)
    e_id.place(x=150, y=50)
    e_name = tk.Entry(newWindow)
    e_name.place(x=150, y=90)
    e_phone = tk.Entry(newWindow)
    e_phone.place(x=150, y=130)
    e_dept = tk.Entry(newWindow)
    e_dept.place(x=150, y=170)
    e_add = tk.Entry(newWindow)
    e_add.place(x=150, y=210)
    e_sal = tk.Entry(newWindow)
    e_sal.place(x=150, y=250)



    labelExample = tk.Label(newWindow, text="Enter your details",width=600,height=2,bg='red')
    labelExample.pack()
    
    buttonExample2 = tk.Button(newWindow, text="Delete", command=delete,bg='pink',width=10,height=2)
    buttonExample2.place(x=250,y=280)
    

# -----------------U P D A T E-----------------------------------------------------------------------------------------------------

def createNewWindow2():
    def update():
        empid = e_id.get()
        empname = e_name.get();
        phone = e_phone.get();
        dept = e_dept.get();
        address = e_add.get();
        salary = e_sal.get();

        if (empid == "" or empname == "" or phone == ""):
            MessageBox.showinfo("Update Status", "All Fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="employeemanagement")
            cursor = con.cursor()
            cursor.execute("UPDATE EMPLOYEE SET empname='" +empname+ "',phone='" +phone+ "',dept='" +dept+ "',address='" +address+ "',salary='" +salary+ "'where empid='" +empid+ "'")
            cursor.execute("commit");

            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_dept.delete(0, 'end')
            e_add.delete(0, 'end')
            e_sal.delete(0, 'end')
            show()
            
            MessageBox.showinfo("update Status", "update Successfully");
            con.close();

    newWindow = tk.Toplevel(app)
    newWindow.title("Update Window")
    newWindow.geometry("600x400")

    empid = tk.Label(newWindow, text="Enter employee id: ", font=("bold", 10))
    empid.place(x=30, y=50)
    empname = Label(newWindow, text="Enter Full Name: ", font=("bold", 10))
    empname.place(x=30, y=90)
    phone = Label(newWindow, text="Enter Phone Number: ", font=("bold", 10))
    phone.place(x=30, y=130)
    dept = Label(newWindow, text="Enter Department : ", font=("bold", 10))
    dept.place(x=30, y=170)
    address = Label(newWindow, text="Enter Address : ", font=("bold", 10))
    address.place(x=30, y=210)
    salary = Label(newWindow, text="Enter Salary : ", font=("bold", 10))
    salary.place(x=30, y=250)


    e_id = tk.Entry(newWindow)
    e_id.place(x=150, y=50)
    e_name = tk.Entry(newWindow)
    e_name.place(x=150, y=90)
    e_phone = tk.Entry(newWindow)
    e_phone.place(x=150, y=130)
    e_dept = tk.Entry(newWindow)
    e_dept.place(x=150, y=170)
    e_add = tk.Entry(newWindow)
    e_add.place(x=150, y=210)
    e_sal = tk.Entry(newWindow)
    e_sal.place(x=150, y=250)


    labelExample = tk.Label(newWindow, text="Enter your details",width=600,height=2,bg='red')
    labelExample.pack()
    
    buttonExample3 = tk.Button(newWindow, text="Update", command=update,bg='pink',width=10,height=2)
    buttonExample3.place(x=250,y=280)
    

# ----------------SEARCH---------------------------------------------------------------------------------------------------------
def createNewWindow3():
    def search():
        if (e_id.get() == ""):
            MessageBox.showinfo("Fetch Status", "please Enter Valid id")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="employeemanagement")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM EMPLOYEE where empid='" + e_id.get() + "'")
            rows = cursor.fetchall()

            for row in rows:
                e_name.insert(0, row[1])
                e_phone.insert(0, row[2])
                e_dept.insert(0, row[3])
                e_add.insert(0, row[4])
                e_sal.insert(0, row[5])


        con.close();

    newWindow = tk.Toplevel(app)
    newWindow.title("Search Window")
    newWindow.geometry("600x400")

    empid = tk.Label(newWindow, text="Enter Employee id : ", font=("bold", 10))
    empid.place(x=30, y=50)
    empname = Label(newWindow, text="Enter Employee Name : ", font=("bold", 10))
    empname.place(x=30, y=90)
    phone = Label(newWindow, text="Enter mobile Number : ", font=("bold", 10))
    phone.place(x=30, y=130)
    dept = Label(newWindow, text="Enter Department : ", font=("bold", 10))
    dept.place(x=30, y=170)
    address = Label(newWindow, text="Enter Address : ", font=("bold", 10))
    address.place(x=30, y=210)
    salary = Label(newWindow, text="Enter Salary : ", font=("bold", 10))
    salary.place(x=30, y=250)



    e_id = tk.Entry(newWindow)
    e_id.place(x=150, y=50)
    e_name = tk.Entry(newWindow)
    e_name.place(x=150, y=90)
    e_phone = tk.Entry(newWindow)
    e_phone.place(x=150, y=130)
    e_dept = tk.Entry(newWindow)
    e_dept.place(x=150, y=170)
    e_add = tk.Entry(newWindow)
    e_add.place(x=150, y=210)
    e_sal = tk.Entry(newWindow)
    e_sal.place(x=150, y=250)


    labelExample = tk.Label(newWindow, text="Enter your detail",width=600,height=2,bg='red')
    labelExample.pack()
    
    buttonExample4 = tk.Button(newWindow, text="SEARCH", command=search,bg='pink',width=10,height=2)
    buttonExample4.place(x=250,y=280)
    


# -----------L I S T B O X-----------------------------------------------------------------------------------------------------------

def show():
    con = pymysql.connect(host="localhost", user="root", password="", database="employeemanagement")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0]) + '   ' + row[1]
        list.insert(list.size() + 1, insertData)
    con.close()


app = tk.Tk()
app.title("OPTIONS TO CHOOSE")

# -----------------ADD BUTTON------------------------------------------
app.geometry("600x400")
Label(app,text="Chose yor option",bg='red',width=600,height=2).pack()
Label(app,text="",height=1).pack()
buttonExample = tk.Button(app, text="ADD",width=10,height=2,command=createNewWindow,bg='yellow')
buttonExample.place(x=50,y=60)
Label(app,text="").pack()

# -------------------DELETE BUTTON-------------------------------------------------
buttonExample2 = tk.Button(app, text="DELETE",width=10,height=2,command=createNewWindow1,bg='yellow')
app.geometry("600x400")
buttonExample2.place(x=50,y=120)
Label(app,text="",height=1).pack()
# ------------------UPDATE BUTTON--------------------------------------------------
buttonExample3 = tk.Button(app, text="UPDATE",width=10,height=2,command=createNewWindow2,bg='yellow')
app.geometry("600x400")
buttonExample3.place(x=50,y=180)
Label(app,text="",height=1).pack()
# ------------------GET BUTTON-------------------------------------
buttonExample4 = tk.Button(app, text="SEARCH",width=10,height=2,command=createNewWindow3,bg='yellow')
app.geometry("600x400")
buttonExample4.place(x=50,y=240)
# -------------------LISTBOX-----------------------------------------
list = Listbox(app)
list.place(x=290,y=100)
show()

app.mainloop()
           
