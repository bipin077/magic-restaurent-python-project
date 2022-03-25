from tkinter import *
import datetime
from tkinter import messagebox
import mainCourse
import deshboard



class GetAddressMob:
    def __init__(self,root,orderFrom="none",id=0):
        self.root=root
        self.root.title("Address & Mobile Number")
        self.root.geometry("600x300+450+270")
        self.root.resizable(False,False)
        self.root.focus_force()
        self.root.config(bg="#009688")

        self.orderFrom=orderFrom
        self.id=id

        self.mobNo=StringVar()

        self.labelMobNo=Label(self.root,text="Enter Mobile No : ",font=("times new roman",15,"bold"),bg="#009688")
        self.labelMobNo.place(x=50,y=30,height=50,width=200)

        self.entryMobNo=Entry(self.root,textvariable=self.mobNo,font="sans-serif 15 normal",borderwidth=0)
        self.entryMobNo.place(x=250,y=40,height=30,width=300)

        self.labelAddress=Label(self.root,text="Enter Address : ",font=("times new roman",15,"bold"),bg="#009688")
        self.labelAddress.place(x=50,y=80,height=50,width=200)

        self.entryAddress=Text(self.root,font="sans-serif 15 normal",borderwidth=0)
        self.entryAddress.place(x=250,y=90,height=100,width=300)

        self.placeOrder=Button(self.root,text="Proceed Order",font=("times new roman",20,"bold"),command=self.createOrder,bg="green",fg="white",borderwidth=0)
        self.placeOrder.place(x=50,y=230,height=40,width=250)

        self.cancel=Button(self.root,text="Cancel",font=("times new roman",20,"bold"),command=self.cancel,bg="red",fg="white",borderwidth=0)
        self.cancel.place(x=320,y=230,height=40,width=250)


    def createOrder(self):
        address=self.entryAddress.get("1.0",END)
        mobNo=self.mobNo.get()

        #if(len(address)==1):
           # messagebox.showwarning("error","Address field does not empty")

        #elif(len(mobNo)<10):
           # messagebox.showwarning("error","Not a valid mobile no")
        
        #else:
        userAddress=str(address)+" ("+str(mobNo)+")"
        
        self.newWin=Toplevel(self.root)
        self.newObj=mainCourse.MainCourse(self.newWin,self.orderFrom,userAddress)
        self.root.withdraw()
    


    def cancel(self):
        self.root.destroy()









if __name__=="__main__":
    root=Tk()

    obj=GetAddressMob(root)

    root.mainloop()
