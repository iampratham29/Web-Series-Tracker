from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    series_name=e_series_name.get();
    category = e_category.get();
    star=e_star.get();

    if(series_name=="" or category =="" or star==""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:

        mydb = mysql.connect(
        host="localhost",
        
        user="root",
        passwd="admin123",
        database="dance",
        auth_plugin='mysql_native_password'
        )

        mycursor = mydb.cursor()
        mycursor.execute("insert into store values('"+ series_name +"','"+category +"','"+star +"')")
        mycursor.execute("commit");

        e_series_name.delete(0,'end')
        e_category.delete(0,'end')
        e_star.delete(0,'end')
        
        

        MessageBox.showinfo("Insert Status" ,"Inserted successfully");

        mydb.close();

def delete():
    if(e_series_name.get() ==""):
        MessageBox.showinfo("Delete Status" ,"series name is compulsory for delete");
    else:
        mydb = mysql.connect(
        host="localhost",
        
        user="root",
        passwd="admin123",
        database="dance",
        auth_plugin='mysql_native_password'
        )

        mycursor = mydb.cursor()
        mycursor.execute("delete from store where series_name='"+ e_series_name.get() +"'")
        mycursor.execute("commit");

        e_series_name.delete(0,'end')
        e_category.delete(0,'end')
        e_star.delete(0,'end')
        
        

        MessageBox.showinfo("Delete Status" ,"Deleted successfully");

        mydb.close();

def update():
    series_name=e_series_name.get();
    category = e_category.get();
    star=e_star.get();

    if(series_name=="" or category =="" or star==""):
        MessageBox.showinfo("Update Status", "All fields are required")
    else:

        mydb = mysql.connect(
        host="localhost",
        
        user="root",
        passwd="admin123",
        database="dance",
        auth_plugin='mysql_native_password'
        )

        mycursor = mydb.cursor()
        mycursor.execute("update store set category='"+ category +"',star='" +star +"' where series_name='"+ series_name +"'")
        mycursor.execute("commit");

        e_series_name.delete(0,'end')
        e_category.delete(0,'end')
        e_star.delete(0,'end')
        
        

        MessageBox.showinfo("Update Status" ,"Updated successfully");

        mydb.close();

def get():
    if(e_series_name.get() == ""):
        MessageBox.showinfo("Fetch status", "ID is compulsory for delete")
    else:
        mydb = mysql.connect(
        host="localhost",
        
        user="root",
        passwd="admin123",
        database="dance",
        auth_plugin='mysql_native_password'
        )

        mycursor = mydb.cursor()
        mycursor.execute("select * from store where series_name='" + e_series_name.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
            e_category.insert(0, row[1])
            e_star.insert(0,row[2])
        mydb.close();

        
 
def show():
        mydb = mysql.connect(
        host="localhost",
        
        user="root",
        passwd="admin123",
        database="dance",
        auth_plugin='mysql_native_password'
        )

        mycursor = mydb.cursor()
        mycursor.execute("select * from store")
        mycursor.fetchall()

        for row in rows:
            insertData = str(row[0])+ '     '+ row[1]
            list.insert(list.size()+1, insertData)
        mydb.close()


root=Tk()
root.geometry("600x300")
root.title("Python+Tkinter+Mysql")

series_name=Label(root, text='Enter series name',font=('bold',10))
series_name.place(x=20,y=30)

category=Label(root, text='Enter Category',font=('bold',10))
category.place(x=20,y=60)

star=Label(root, text='Enter lead role',font=('bold',10))
star.place(x=20,y=90)

e_series_name = Entry()
e_series_name.place(x=150, y=30)

e_category = Entry()
e_category.place(x=150,y=60)

e_star= Entry()
e_star.place(x=150, y=90)



insert =Button(root, text="Insert" ,font=("italic" ,10) ,bg="white", command=insert)
insert.place(x=20, y=140)

delete =Button(root, text="Delete" ,font=("italic" ,10) ,bg="white", command=delete)
delete.place(x=70, y=140)

update =Button(root, text="Update" ,font=("italic" ,10) ,bg="white", command=update)
update.place(x=130, y=140)

get =Button(root, text="get" ,font=("italic" ,10) ,bg="white", command=get)
get.place(x=190, y=140)

list = Listbox(root)
list.place(x=290,y=30)

root.mainloop()
#End here
