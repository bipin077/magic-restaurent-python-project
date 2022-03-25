from tkinter import *
from Database_files import Connection
from PIL import ImageTk,Image 
import deshboard
import updateForm

class UpdateItems:
    def __init__(self,root,orderFrom="none"):
        self.root=root
        self.root.title("Magic Restaurent")
        self.root.geometry("1350x700+0+0")
        #self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.focus_force()


        #====== Title =======

        self.icon_title=Image.open("images/logo.png")
        self.icon_title=self.icon_title.resize((50,50),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Magic Restaurent",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====== logout Button=======

        self.icon_logout=Image.open("images/home.png")
        self.icon_logout=self.icon_logout.resize((40,30),Image.ANTIALIAS)
        self.icon_logout=ImageTk.PhotoImage(self.icon_logout)

        btn_deshboard=Button(self.root,text=" Home",font=("new time roman",15,"bold"),anchor="w",compound=LEFT,image=self.icon_logout,bg="red",cursor="hand2",fg="white",command=self.homePage).place(x=1150,y=10,height=50,width=130)


        #btn_deshboard=Button(self.root,text="Deshboard",font=("new time roman",15,"bold"),bg="yellow",cursor="hand2",command=self.homePage).place(x=1100,y=10,height=50,width=150)
        
        # ====== Left menu =======e

        
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=70,width=300,height=625)
        
        self.icon_side=Image.open("images/side.jpg")
        self.icon_side=self.icon_side.resize((40,40),Image.ANTIALIAS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        lbl_menu=Label(leftMenu,text="Categories",fg="white",font=("times new roman",20),bg="#009688",pady=20).pack(side=TOP,fill=X)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select categoryName from foodCategories"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            btn_table=Button(leftMenu,text=row[0],command=lambda x=row[0]: self.addProductDetails(x),image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def homePage(self):
        self.newWin=Toplevel(self.root)
        self.newObj=deshboard.MagicRestaurent(self.newWin)
        self.root.withdraw()



    def addProductDetails(self,categoryName):

        self.processTableTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.processTableTitleFrame.place(x=305,y=75,height=70,width=1030)

        self.processTableTitleLabel=Label(self.processTableTitleFrame,text=categoryName,font="arial 25 bold",bg="#009688",fg="white")
        self.processTableTitleLabel.place(x=450,y=5)

        self.processTableFrame=Frame(self.root,bd=3,bg="white")
        self.processTableFrame.place(x=305,y=155,height=540,width=1030)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select id from foodCategories where categoryName='"+categoryName+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        categoryId=result[0]

        self.half=StringVar()
        

        sql1="select foodName,quaterPlatePrice,halfPlatePrice,fullPlatePrice from foodItems where categoryId='"+str(categoryId)+"'"
        self.cursor.execute(sql1)
        resul=self.cursor.fetchall()
        self.row=0
        self.col=0
        for res in resul:
            if(int(res[1])==0 and int(res[2])==0 and int(res[3])!=0):         
                self.uttn=Button(self.processTableFrame,text=str(res[0])+"\n"+u"\u20B9 "+str(res[3]),font="arial 12 bold",pady=10,command=lambda id=categoryId,foodName=res[0],fl=res[3]:self.updateItem(id,foodName,fl),width=19)
                self.uttn.grid(row=self.row,column=self.col)
            elif(int(res[1])==0 and int(res[2])!=0 and int(res[3])!=0):
                self.uttn=Button(self.processTableFrame,text=str(res[0])+"\n F : "+str(res[3])+" H : "+str(res[2]),font="arial 12 bold",pady=10,command=lambda id=categoryId,foodName=res[0],hf=res[2],fl=res[3]:self.updateItem(id,foodName,fl,hf),width=19)
                self.uttn.grid(row=self.row,column=self.col)
            elif(int(res[1])!=0 and int(res[2])!=0 and int(res[3])!=0):
                self.uttn=Button(self.processTableFrame,text=str(res[0])+"\n Q : "+str(res[1])+" H : "+str(res[2])+" F : "+str(res[3]),font="arial 12 bold",pady=10,command=lambda id=categoryId,foodName=res[0],hf=res[2],fl=res[3],qt=res[1]:self.updateItem(id,foodName,fl,hf,qt),width=19)
                self.uttn.grid(row=self.row,column=self.col)

            
            self.col=self.col+1
            if(self.col==5):
                self.col=0
                self.row=self.row+1

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def updateItem(self,id,name,fl=0,hf=0,qt=0):
        
        self.newWin=Toplevel(self.root)
        self.newObj=updateForm.UpdateForm(self.newWin,id,name,fl,hf,qt)




if __name__=="__main__":
    root=Tk()
    obj=UpdateItems(root)
    root.mainloop()