from tkinter import *
import datetime
from tkinter import messagebox
from Database_files import Connection



class UpdateForm:
    def __init__(self,root,id=0,foodName="none",fl=0,hf=0,qt=0):
        self.root=root
        self.root.title("Update Item")
        self.root.geometry("600x300+400+250")
        self.root.resizable(False,False)
        self.root.config(bg="#009688")
        self.root.focus_force()
        
        self.id=id
        self.fn=foodName
        self.ful=fl
        self.hff=hf
        self.qtt=qt



        self.foodName=StringVar()
        self.hf=StringVar()
        self.fl=StringVar()
        self.qt=StringVar()

        if(self.qtt==0 and self.hff==0 and self.ful!=0):
            self.labelFoodName=Label(self.root,text="Item Name : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFoodName.place(x=50,y=30,height=50,width=200)

            self.entryFoodName=Entry(self.root,textvariable=self.foodName,borderwidth=0,font="sans-serif 15 normal")
            self.entryFoodName.place(x=250,y=40,height=30,width=300)
            self.entryFoodName.insert(INSERT,self.fn)
            

            self.labelFL=Label(self.root,text="Item Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFL.place(x=50,y=80,height=50,width=200)

            self.entryFL=Entry(self.root,textvariable=self.fl,borderwidth=0,font="sans-serif 15 normal")
            self.entryFL.place(x=250,y=90,height=30,width=300)
            self.entryFL.insert(INSERT,self.ful)

            self.updateItems=Button(self.root,text="Update Item",font=("times new roman",20,"bold"),command=self.updateOrder,bg="green",fg="white",borderwidth=0)
            self.updateItems.place(x=120,y=140,height=40,width=290)

        if(self.qtt==0 and self.hff!=0 and self.ful!=0):
            
            self.labelFoodName=Label(self.root,text="Item Name : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFoodName.place(x=50,y=30,height=50,width=200)

            self.entryFoodName=Entry(self.root,textvariable=self.foodName,borderwidth=0,font="sans-serif 15 normal")
            self.entryFoodName.place(x=250,y=40,height=30,width=300)
            self.entryFoodName.insert(INSERT,self.fn)

            self.labelHF=Label(self.root,text="Half Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelHF.place(x=50,y=80,height=50,width=200)

            self.entryHF=Entry(self.root,textvariable=self.hf,borderwidth=0,font="sans-serif 15 normal")
            self.entryHF.place(x=250,y=90,height=30,width=300)
            self.entryHF.insert(INSERT,self.hff)
            
            self.labelFL=Label(self.root,text="Full Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFL.place(x=50,y=130,height=50,width=200)

            self.entryFL=Entry(self.root,textvariable=self.fl,borderwidth=0,font="sans-serif 15 normal")
            self.entryFL.place(x=250,y=140,height=30,width=300)
            self.entryFL.insert(INSERT,self.ful)

            self.updateItems=Button(self.root,text="Update Item",font=("times new roman",20,"bold"),command=self.updateOrder,bg="green",fg="white",borderwidth=0)
            self.updateItems.place(x=120,y=200,height=40,width=290)

        if(self.qtt!=0 and self.hff!=0 and self.ful!=0):

            self.labelFoodName=Label(self.root,text="Item Name : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFoodName.place(x=50,y=30,height=50,width=200)

            self.entryFoodName=Entry(self.root,textvariable=self.foodName,borderwidth=0,font="sans-serif 15 normal")
            self.entryFoodName.place(x=250,y=40,height=30,width=300)
            self.entryFoodName.insert(INSERT,self.fn)

            self.labelqt=Label(self.root,text="Quater Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelqt.place(x=50,y=80,height=50,width=200)

            self.entryqt=Entry(self.root,textvariable=self.qt,borderwidth=0,font="sans-serif 15 normal")
            self.entryqt.place(x=250,y=90,height=30,width=300)
            self.entryqt.insert(INSERT,self.qtt)

            self.labelHF=Label(self.root,text="Half Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelHF.place(x=50,y=130,height=50,width=200)

            self.entryHF=Entry(self.root,textvariable=self.hf,borderwidth=0,font="sans-serif 15 normal")
            self.entryHF.place(x=250,y=140,height=30,width=300)
            self.entryHF.insert(INSERT,self.hff)
            

            self.labelFL=Label(self.root,text="Full Plate Price : ",font=("times new roman",15,"bold"),bg="#009688")
            self.labelFL.place(x=50,y=180,height=50,width=200)

            self.entryFL=Entry(self.root,textvariable=self.fl,borderwidth=0,font="sans-serif 15 normal")
            self.entryFL.place(x=250,y=190,height=30,width=300)
            self.entryFL.insert(INSERT,self.ful)

            self.updateItems=Button(self.root,text="Update Item",font=("times new roman",20,"bold"),command=self.updateOrder,bg="green",fg="white",borderwidth=0)
            self.updateItems.place(x=120,y=250,height=40,width=290)


    def updateOrder(self):
        foodName=self.foodName.get()
        hf=self.hf.get()
        fl=self.fl.get()
        qt=self.qt.get()
        id=self.id

        if qt=="" and hf!="" and fl!="":
            qt=0
        elif qt=="" and hf=="" and fl!="":
            qt=0
            hf=0
        

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="update foodItems set foodName='"+str(foodName)+"',quaterPlatePrice='"+str(qt)+"',halfPlatePrice='"+str(hf)+"',fullPlatePrice='"+str(fl)+"' where foodName='"+str(foodName)+"'"
        self.cursor.execute(sql)
        self.conn.commit()


        messagebox.showinfo("success","Item Updated Successfully")

        self.root.destroy()
                
        self.cursor.close()
        self.conn.close()

        









if __name__=="__main__":
    root=Tk()

    obj=UpdateForm(root)

    root.mainloop()
