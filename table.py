from tkinter import *
from Database_files import Connection
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
from datetime import timedelta
from tkinter import simpledialog
import time
from tkcalendar import Calendar,DateEntry
from tkinter import ttk


class Table:
    def __init__(self,root):
        self.root=root
        self.root.title("Table")
        self.root.geometry("970x550+380+160")

        self.tableFrame=Frame(self.root,bd=3)
        self.tableFrame.place(x=320,y=110,height=570,width=950)
        self.row=0
        self.col=0

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()


        sql="select tableNo,color from tablesData"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            color=row[1]
            self.col=self.col+1
            self.tableNo=Button(self.tableFrame,text=row[0],bg=color,font="Arial 30 bold",padx=60,pady=10,width=5,command=lambda x=row[0]: self.addTableItem(x))
            self.tableNo.grid(row=self.row,column=self.col)
            
            if(self.col==4):
                self.col=0
                self.row=self.row+1

        self.conn.commit()
        self.cursor.close()
        self.conn.close()













if __name__=="__main__":
    root=Tk()
    obj=Table(root)
    root.mainloop()