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

def add_student():
    studentname = entry_name.get().strip()
    department = entry_department.get().strip()
    number = entry_number.get().strip()
    gpa = entry_gpa.get().strip()
    class_name = entry_class.get().strip()
    student_id = entry_add_id.get().strip()
    
    try:
        if not studentname or not department or not number or not gpa or not class_name or not student_id:
            listbox.insert("end", "Please fill in all fields.")
            return
        else:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO studentsinfo (fullname, department, numberstudent, gpa, class, id) VALUES (?, ?, ?, ?, ?, ?)",(studentname, department, number, gpa, class_name, student_id))

            conn.commit()
            listbox.insert("end", "Student added successfully.")
            conn.close()
    except Exception as e:
        print(f"Error adding student: {e}")

def delete_student():
    student_id = entry_delete_id.get().strip()
    try:
        if not student_id:
            listbox.insert("end", "Please enter a student ID.")
            return
        else:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM studentsinfo WHERE id = ?", (student_id,))
            conn.commit()
            listbox.insert("end", "Student deleted successfully.")
            conn.close()
    except Exception as e:
        print(f"Error deleting student: {e}")

def clean_list():
    listbox.delete(0, "end")

def update_student():
    student_id = entry_add_id.get().strip()
    studentname = entry_name.get().strip()
    department = entry_department.get().strip()
    number = entry_number.get().strip()
    gpa = entry_gpa.get().strip()
    class_name = entry_class.get().strip()

    try:
        if not student_id or not studentname or not department or not number or not gpa or not class_name:
            listbox.insert("end", "Please fill in all fields.")
            return
        else:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("UPDATE studentsinfo SET fullname = ?, department = ?, numberstudent = ?, gpa = ?, class = ? WHERE id = ?",
                           (studentname, department, number, gpa, class_name, student_id))
            conn.commit()
            listbox.insert("end", "Student updated successfully.")
            conn.close()
    except Exception as e:
        print(f"Error updating student: {e}")

def show_students():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM studentsinfo")
        rows = cursor.fetchall()
        for row in rows:
            listbox.insert("end", row)
        conn.close()
    except Exception as e:
        print(f"Error fetching students: {e}")

def search_by_id():
    student_id = search_entry.get().strip()
    try:
        if not student_id:
            listbox.insert("end", "Please enter a student ID.")
            return
        else:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM studentsinfo WHERE id = ?", (student_id,))
            row = cursor.fetchone()
            if row:
                listbox.insert("end", row)
            else:
                listbox.insert("end", "Student not found.")
            conn.close()
    except Exception as e:
        print(f"Error searching student by ID: {e}")

def search_student():
    search_term = search_entry.get().strip()
    try:
        if not search_term:
            listbox.insert("end", "Please enter a search term.")
            return
        else:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            code = """ SELECT * FROM studentsinfo WHERE fullname LIKE ?
            OR department LIKE ? OR numberstudent LIKE ? OR gpa LIKE ? OR class LIKE ?"""
            executes = f"%{search_term}%"
            cursor.execute(code, (executes, executes, executes, executes, executes))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    listbox.insert("end", row)
            else:
                listbox.insert("end", "No students found.")
            conn.close()
    except Exception as e:
        print(f"Error searching students: {e}")

def sort_by_gpa():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM studentsinfo ORDER BY gpa DESC")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                listbox.insert("end", row)
        else:
            listbox.insert("end", "No students found.")
        conn.close()
    except Exception as e:
        print(f"Error sorting students by GPA: {e}")

#labelframe 1
lbf1 = tk.LabelFrame(root,text="Search & Commands",bg="black",fg="white",padx=10,pady=20)
lbf1.place(x=20,y=20)

#buttons(labelframe 1)
btn1 = tk.Button(lbf1,command=close_program,text="Close Program",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn1.grid(row=0,column=0,padx=5,pady=5)

btn2 = tk.Button(lbf1,command=sort_by_gpa,text="Sort By GPA",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn2.grid(row=1,column=0,padx=5,pady=5)

btn3 = tk.Button(lbf1,command=clean_list,text="Clean List",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn3.grid(row=2,column=0,padx=5,pady=5)

btn4 = tk.Button(lbf1,command=show_students,text="Show Students",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn4.grid(row=3,column=0,padx=5,pady=5)

#text
lbl1 = tk.Label(lbf1,text="Search:",bg="black",fg="white",padx=5,pady=5)
lbl1.grid(row=4,column=0,padx=5,pady=5,sticky="w")

#entry for search and also search by ID
search_entry = tk.Entry(lbf1,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
search_entry.grid(row=4,column=0,padx=5,pady=5,sticky="e")

btn5 = tk.Button(lbf1,command=search_by_id,text="Search by ID",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
btn5.grid(row=5,column=0,padx=5,pady=5)

btn6 = tk.Button(lbf1,command=search_student,text="Search",bg="white",fg="black",width=25,highlightbackground="black",highlightthickness=0)
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

entry_add_id = tk.Entry(lbf2,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_add_id.grid(row=5,column=1,padx=5,pady=5)

btn7 = tk.Button(lbf2,command=add_student,text="ADD",bg="gray",fg="black",highlightbackground="black",highlightthickness=0,width=10)
btn7.grid(row=6,column=0,padx=5,pady=5,sticky="w")


btn8 = tk.Button(lbf2,command=update_student,text="UPDATE BY ID",bg="gray",fg="black",highlightbackground="black",highlightthickness=0,width=20)
btn8.grid(row=6,column=1,padx=5,pady=5,sticky="")


#label frame 3 (listbox)
lbf3 = tk.LabelFrame(root,text="List & Delete Students",bg="black",fg="white",padx=10,pady=20)
lbf3.place(x=20,y=370)

listbox = tk.Listbox(lbf3,bg="gray",fg="black",width=79,height=17,highlightbackground="black",highlightthickness=0)
listbox.grid(row=0,column=0,padx=5,pady=5)

lbl8 = tk.Label(lbf3,text="Enter Student ID: ",bg="black",fg="white",padx=5,pady=5)
lbl8.grid(row=1,column=0,padx=5,pady=5,sticky="w")

entry_delete_id = tk.Entry(lbf3,bg="gray",fg="black",width=22,highlightbackground="black",highlightthickness=0)
entry_delete_id.place(x=150,y=310)

btn9 = tk.Button(lbf3,text="DELETE BY ID",bg="gray",fg="black",highlightbackground="black",highlightthickness=0,width=35,command=delete_student)
btn9.grid(row=1,column=0,padx=5,pady=5,sticky="e")

root.mainloop()