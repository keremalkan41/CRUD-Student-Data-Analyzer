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
    print(f"CConnection failed: {e}")
