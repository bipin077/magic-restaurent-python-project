from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk,Image
from Database_files import Connection
import deshboard
import userAuthentication

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login | Magic Restaurent")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="#00a3a3")

        self.icon_title=Image.open("images/restaurent.jpg")
        self.icon_title=self.icon_title.resize((1530,800),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)

        canvas1 = Canvas( root, width = 400,height = 400)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image( 0, 0, image = self.icon_title, anchor = "nw")

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        sql="select OTK from Admin"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        OTK=result[0]

        if(OTK==0):
            self.root.withdraw()
            self.newWin=Toplevel(self.root)
            self.newObj=userAuthentication.Authentication(self.newWin)
        else:
            self.adminIcon=Image.open("images/admin.png")
            self.adminIcon=self.adminIcon.resize((50,50),Image.ANTIALIAS)
            self.adminIcon=ImageTk.PhotoImage(self.adminIcon)


            adminLoginFrame=Frame(self.root,bg="#009688",bd=5)
            adminLoginFrame.place(x=300,y=150,width=700,height=400)


            self.userName=StringVar()
            self.password=StringVar()

            title=Label(adminLoginFrame,text="  Admin Login ",font="sans-serif 20 bold",image=self.adminIcon,bg="#010c48",compound=LEFT,fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

            userNameLabel=Label(adminLoginFrame,text="User Name : ",font="sans-serif 15 bold",bg="#009688")
            userNameLabel.place(x=50,y=120,height=50,width=200)

            userNameEntry=Entry(adminLoginFrame,font="sans-serif 15 bold",textvariable=self.userName)
            userNameEntry.place(x=260,y=130,height=35,width=300)

            passwordLabel=Label(adminLoginFrame,text="Password : ",font="sans-serif 15 bold",bg="#009688")
            passwordLabel.place(x=50,y=180,height=50,width=200)

            passwordEntry=Entry(adminLoginFrame,font="sans-serif 15 bold",textvariable=self.password)
            passwordEntry.place(x=260,y=190,height=35,width=300)

            submitButton=Button(adminLoginFrame,text="Log In ",font="sans-serif 15 bold",bg="red",fg="white",cursor="hand2",command=self.validateUser)
            submitButton.place(x=100,y=260,height=50,width=200)


    def validateUser(self):
        userName=self.userName.get()
        password=self.password.get()

        if userName!="" and password!="":
            self.connection=Connection()
            self.conn=self.connection.getConnection()
            self.cursor=self.connection.getCursor()

            sql="select name,password from Admin"
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            for user in result:
                if(user[0]==userName and user[1]==password):
                    self.newWin=Toplevel(self.root)
                    self.newObj=deshboard.MagicRestaurent(self.newWin)
                    self.root.withdraw()
                else:
                    messagebox.showinfo("Failed","User Not Found")
        else:
            messagebox.showinfo("info","User Name And Password Field Does Not Empty")

        self.cursor.close()
        self.conn.close()



if __name__=="__main__":
    root=Tk()
    oj=Login(root)

    root.mainloop()