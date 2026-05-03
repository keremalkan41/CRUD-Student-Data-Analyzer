#libraries
import pyodbc
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import tkinter as tk

load_dotenv()
server = os.getenv('DB_SERVER')
user = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

try:
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}'
    conn = pyodbc.connect(conn_str)
    print("successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")

#root settings
root = tk.Tk()
root.title("Student CRUD System")
root.geometry("800x800")
root.resizable(False,False)
root.config(background="black")
root.grid_columnconfigure(0, weight=1)

#functions
#-- Functions will be here --
def close_program():
    search_entry.delete(0, "end")
    root.destroy()


#labelframe 1
lbf1 = tk.LabelFrame(root,text="Search & Commands",bg="black",fg="white",padx=10,pady=20)
lbf1.place(x=20,y=20)

#buttons(labelframe 1)
btn1 = tk.Button(lbf1,command=close_program,text="Close Program",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn1.grid(row=0,column=0,padx=5,pady=5)

btn2 = tk.Button(lbf1,text="Sort By GPA",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn2.grid(row=1,column=0,padx=5,pady=5)

btn3 = tk.Button(lbf1,text="Clean List",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn3.grid(row=2,column=0,padx=5,pady=5)

btn4 = tk.Button(lbf1,text="Show 1. Year Students",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn4.grid(row=3,column=0,padx=5,pady=5)

#text
lbl1 = tk.Label(lbf1,text="Search:",bg="black",fg="white",padx=5,pady=5)
lbl1.grid(row=4,column=0,padx=5,pady=5,sticky="w")

#entry for search and also search by ID
search_entry = tk.Entry(lbf1,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
search_entry.grid(row=4,column=0,padx=5,pady=5,sticky="e")

btn5 = tk.Button(lbf1,text="Search by ID",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn5.grid(row=5,column=0,padx=5,pady=5)

btn6 = tk.Button(lbf1,text="Search",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn6.grid(row=6,column=0,padx=5,pady=5)

#labelframe 2
lbf2 = tk.LabelFrame(root,text="Add Data & Update Data",bg="black",fg="white",padx=10,pady=20)
lbf2.place(x=350,y=20)

lbl2 = tk.Label(lbf2,text="Name & Surname:",bg="black",fg="white",padx=5,pady=5)
lbl2.grid(row=0,column=0,padx=5,pady=5,sticky="w")

entry_name = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_name.grid(row=0,column=1,padx=5,pady=5)

lbl3 = tk.Label(lbf2,text="Department:",bg="black",fg="white",padx=5,pady=5)
lbl3.grid(row=1,column=0,padx=5,pady=5,sticky="w")

entry_department = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_department.grid(row=1,column=1,padx=5,pady=5)

lbl4 = tk.Label(lbf2,text="Number:",bg="black",fg="white",padx=5,pady=5)
lbl4.grid(row=2,column=0,padx=5,pady=5,sticky="w")

entry_number = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_number.grid(row=2,column=1,padx=5,pady=5)

lbl5 = tk.Label(lbf2,text="GPA:",bg="black",fg="white",padx=5,pady=5)
lbl5.grid(row=3,column=0,padx=5,pady=5,sticky="w")

entry_gpa = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_gpa.grid(row=3,column=1,padx=5,pady=5)

lbl6 = tk.Label(lbf2,text="Class:",bg="black",fg="white",padx=5,pady=5)
lbl6.grid(row=4,column=0,padx=5,pady=5,sticky="w")

entry_class = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_class.grid(row=4,column=1,padx=5,pady=5)

lbl7 = tk.Label(lbf2,text="ID (VERY IMPORTANT):",bg="black",fg="white",padx=5,pady=5)
lbl7.grid(row=5,column=0,padx=5,pady=5,sticky="w")

entry_id = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_id.grid(row=5,column=1,padx=5,pady=5)

btn7 = tk.Button(lbf2,text="ADD",bg="gray",fg="black",highlightbackground="black",highlightthickness=0,width=10)
btn7.grid(row=6,column=0,padx=5,pady=5,sticky="w")


btn8 = tk.Button(lbf2,text="UPDATE BY ID",bg="gray",fg="black",highlightbackground="black",highlightthickness=0,width=20)
btn8.grid(row=6,column=1,padx=5,pady=5,sticky="")

root.mainloop()