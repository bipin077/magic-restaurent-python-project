from tkinter import *
from tkinter import messagebox
import login
from Database_files import Connection

class Authentication:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x200+300+200")
        self.root.focus_force()
        self.root.title("User Authentication")
        self.root.config(bg="green")

        self.OTK_key="1234567890987654"

        self.otk_key=StringVar()

        label=Label(self.root,text="Enter Authentication Key",font="sans-serif 15 bold",bg="green",fg="white")
        label.place(x=40,y=20,width=400,height=40)

        entry=Entry(self.root,font="sans-serif 15 bold",textvariable=self.otk_key)
        entry.place(x=40,y=70,width=430,height=35)
        entry.config(justify="center")

        button=Button(self.root,text="Authenticate",font="sans-serif 15 bold",bg="red",fg="white",command=self.authenticateOtk)
        button.place(x=130,y=120,width=200,height=40)

    def authenticateOtk(self):
        otk=self.otk_key.get()
        if(otk==self.OTK_key):
            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="update Admin set OTK=1"
            self.cursor.execute(sql)
            self.conn.commit()

            messagebox.showinfo("Success","User Authentication Successfull")

            self.root.withdraw()
            self.newWin=Toplevel(self.root)
            self.newObj=login.Login(self.newWin)
        else:
            messagebox.showerror("Error","Invalid Authentication Key")
            self.root.destroy()






if __name__=="__main__":
    root=Tk()
    obj=Authentication(root)
    root.mainloop()