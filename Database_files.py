from sqlite3 import *
from tkinter import messagebox

class Connection:
    def __init__(self):
        try:
            self.conn=connect("database/MagicRestaurent.db")
        except Exception:
            messagebox.showerror("Error","Failed to connect with database")

    def getConnection(self):
        return self.conn

    def getCursor(self):
        self.cursor=self.conn.cursor()
        return self.cursor
        

    

    
