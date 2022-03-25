from tkinter import *
from Database_files import Connection
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
import deshboard
import os
import tempfile

class MainCourse:
    def __init__(self,root,orderFrom="none",userAddress="none",id=0):
        self.root=root
        self.root.title("Magic Restaurent")
        self.root.geometry("1530x800+0+0")
        #self.root.resizable(False,False)
        self.root.config(bg="white")

        self.orderFrom=orderFrom
        self.userAddress=userAddress
        self.id=id
       

        # this is to store frame so that we have to use in flush.......
        self.dashboard_frames=[]

        # total price to checkout
        self.total=0

        # this is to hold orders 
      
        self.cartItems={
            "itemName":[],
            "itemQuantity":[],
            "itemPrice":[]
        }

        self.notificationData=[]


        #====== Title =======

        self.icon_title=Image.open("images/logo.png")
        self.icon_title=self.icon_title.resize((50,50),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Magic Restaurent",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====== logout Button=======

        self.icon_logout=Image.open("images/home.png")
        self.icon_logout=self.icon_logout.resize((40,30),Image.ANTIALIAS)
        self.icon_logout=ImageTk.PhotoImage(self.icon_logout)

        btn_logout=Button(self.root,text=" Home",font=("new time roman",15,"bold"),anchor="w",compound=LEFT,image=self.icon_logout,bg="red",cursor="hand2",fg="white",command=self.homePage).place(x=1200,y=10,height=50,width=130)

        #=======clock=====
        self.lbl_clock=Label(self.root,text="Order From : "+orderFrom,font=("time new roman",15,"bold"),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,width=1530,height=30)



        # ====== Left menu =======e

        
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=105,width=260,height=590)
        
        self.icon_side=Image.open("images/side.jpg")
        self.icon_side=self.icon_side.resize((40,40),Image.ANTIALIAS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        lbl_menu=Label(leftMenu,text="Categories",font="arial 20 bold",bg="#009688",fg="white").pack(side=TOP,fill=X)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select categoryName from foodCategories"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if(len(result)<1):
            messagebox.showerror("ERROR","No Category Found in Database")
        i=0
        temp=""
        for row in result:
            if(i==0):
                temp=row[0]
                
                i=i+1

            btn_table=Button(leftMenu,text=row[0],command=lambda x=row[0]: self.addProductDetails(x),image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


        self.checkDate()
        self.setOrderNo()

        # Right Frame

        self.rightMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        self.rightMenu.place(x=1070,y=105,width=285,height=590)
        

        billingLabel=Label(self.rightMenu,text="Orders",font="arial 20 bold",bg="#009688",fg="white")
        billingLabel.place(x=0,y=0,height=40,width=283)

        self.billingTextBox=Text(self.rightMenu,bd=3)
        self.billingTextBox.place(x=0,y=47,height=390,width=280)
        
    
        self.removeBtn=Button(self.rightMenu,text="Remove Cart Item",font="arial 15 bold",bg="#009688",fg="white",command=self.removeCartItems)
        self.removeBtn.place(x=0,y=510,height=40,width=283)

        self.placeKot=Button(self.rightMenu,text="K.O.T",font="arial 15 bold",bg="#009688",fg="white",command=lambda i=1:self.placeOrder(i))
        self.placeKot.place(x=0,y=550,height=40,width=141)

        self.placeOrderBtn=Button(self.rightMenu,text="Place Order",font="arial 15 bold",bg="#009688",fg="white",command=lambda i=0:self.placeOrder(i))
        self.placeOrderBtn.place(x=141,y=550,height=40,width=141)


        self.addProductDetails(temp)

    def checkDate(self):
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        todaydatetime=datetime.datetime.now()
        dateToday=todaydatetime.date()

        sql="select todaysDate from defaultSettings"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        if(str(result[0])!=str(dateToday)):
            dateSql="update defaultSettings set todaysDate='"+str(dateToday)+"',orderNo='0'"
            self.cursor.execute(dateSql)
            self.conn.commit()

        self.cursor.close()
        self.conn.close()



    def setOrderNo(self):
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select orderNo from defaultSettings"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        
        self.orderNo=int(result[0])+1


        self.cursor.close()
        self.conn.close()

    def addOrderNo(self):
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()


        dateSql="update defaultSettings set orderNo='"+str(self.orderNo)+"'"
        self.cursor.execute(dateSql)
        self.conn.commit()



    def removeCartItems(self):
        self.top_r=Toplevel(self.root)
        self.top_r.title("Remove Cart Items")
        self.top_r.geometry("300x130+450+250")
        

        data=[]

        for item in self.cartItems["itemName"]:
            data.append(item)


        self.tkvar = StringVar(self.root)
        
        self.tkvar.set("Choose Cart Items")

        chooseCategoryLabel_u_u=Label(self.top_r, text="Choose Cart Item : ",pady=5,width=30,font="arial 13 bold",bg="#009688",fg="white")
        chooseCategoryLabel_u_u.place(x=0,y=0)

        itemSize=OptionMenu(self.top_r,self.tkvar,*data)
        itemSize.place(x=50,y=40)

        getProductDetails_u_u=Button(self.top_r,text="Delete Item",command=self.deleteItem,bg="red",fg="white",font="arial 13 bold")
        getProductDetails_u_u.place(x=0,y=100,height=30,width=300)

        self.top_r.mainloop()


    def deleteItem(self):
        
        itemName=self.tkvar.get()
        loc=self.cartItems["itemName"].index(itemName)
        price=self.cartItems["itemPrice"][loc]
        qty=self.cartItems["itemQuantity"][loc]

        print(price)
        print(qty)
        
        self.total=float(self.total)-float(float(price)*int(qty))
        

        self.cartItems["itemName"].pop(loc)
        self.cartItems["itemQuantity"].pop(loc)
        self.cartItems["itemPrice"].pop(loc)
        messagebox.showinfo("success","Item Deleted")
        self.addBilling()
        self.setTotal()

        self.top_r.destroy()




    def setTotal(self):
        self.totalBillLabel=Label(self.rightMenu,text="Rs "+str(self.total),font="arial 20 bold",fg="#009688",bg="white")
        self.totalBillLabel.place(x=0,y=450,height=50,width=283)


    def homePage(self):
        self.root.withdraw()
        self.newWin=Toplevel(self.root)
        self.newObj=deshboard.MagicRestaurent(self.newWin)
        



    def addProductDetails(self,categoryName):
        self.qty=StringVar()
        self.itemSize=IntVar()
        self.itemQuantity=StringVar()

        self.processTableTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.processTableTitleFrame.place(x=265,y=105,height=50,width=800)

        self.processTableTitleLabel=Label(self.processTableTitleFrame,text=categoryName,font="arial 20 bold",bg="#009688",fg="white")
        self.processTableTitleLabel.place(x=300,y=5,height=30)

        self.processTableFrame=Frame(self.root,bd=3,bg="white")
        self.processTableFrame.place(x=265,y=155,height=540,width=805)

        self.row=0
        self.col=0

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
        res=self.cursor.fetchall()
        if(len(res)<1):
            messagebox.showerror("ERROR","No item found in database with this category")
        self.row=0
        self.col=0

        for row in res:
            if(int(row[1])==0 and int(row[2])!=0 and int(row[3])!=0):          
                self.uttn=Button(self.processTableFrame,text=str(row[0])+"\n H : "+str(row[2])+"  "+"  F : "+str(row[3]),font="arial 12 bold",command=lambda item=row[0],qt=0,hf=row[2],fp=row[3]: self.addCartItem(item,qt,hf,fp),width=18,bg="#f0f0f0",fg="black",pady=10,padx=5)
                self.uttn.grid(row=self.row,column=self.col)
            if(int(row[1])==0 and int(row[2])==0 and int(row[3])!=0):
                self.uttn=Button(self.processTableFrame,text=str(row[0])+"\n"+str(row[3]),font="arial 12 bold",pady=10,command=lambda item=row[0],qt=0,hf=0,fp=row[3]: self.addCartItem(item,qt,hf,fp),width=18,padx=5)
                self.uttn.grid(row=self.row,column=self.col)
            if(int(row[1])!=0 and int(row[2])!=0 and int(row[3])!=0):
                self.uttn=Button(self.processTableFrame,text=str(row[0])+"\nQ : "+str(row[1])+" H : "+str(row[2])+" F : "+str(row[3]),font="arial 12 bold",pady=10,command=lambda item=row[0],qt=row[1],hf=row[2],fp=row[3]: self.addCartItem(item,qt,hf,fp),width=18,padx=5)
                self.uttn.grid(row=self.row,column=self.col)
                




            self.col=self.col+1
            if(self.col==4):
                self.col=0
                self.row=self.row+1

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def viewItems(self):
        messagebox.showinfo("info","sucesss")

    def addCartItem(self,itemName,qt,hf,fl):
        top=Toplevel(self.root)
        top.title("Select Item size & Quantity")
        top.geometry("300x150+450+250")
        top.focus_force()

        self.val=1

        def plus():
            
            self.qtyEntry2.delete("1.0", "end")
            #self.qtyEntry2.delete(0)
            self.val=self.val+1
            self.qtyEntry2.insert(END,self.val)
            self.qtyEntry2.tag_add("tag_name", "1.0", "end")
            self.qtyEntry2.tag_configure("tag_name", justify='center')

        def minus():
            self.qtyEntry2.delete("1.0", "end")
            #self.qtyEntry2.delete(0)
            if(self.val==1):
                self.qtyEntry2.insert(END,1)
                self.qtyEntry2.tag_add("tag_name", "1.0", "end")
                self.qtyEntry2.tag_configure("tag_name", justify='center')
            else:
                self.val=self.val-1
                self.qtyEntry2.insert(END, self.val)
                self.qtyEntry2.tag_add("tag_name", "1.0", "end")
                self.qtyEntry2.tag_configure("tag_name", justify='center')

        def add():
            self.itemQuantity=self.qtyEntry2.get("1.0",END)
            
            if(self.itemSize.get()):
                if(self.itemSize.get()==0):
                    platesize=" (Quater Plate)"
                    price=qt
                elif(self.itemSize.get()==1):
                    platesize=" (Half Plate)"
                    price=hf
                elif(self.itemSize.get()==2):
                    platesize=" (Full Plate)"
                    price=fl
            else:
                platesize=""
                price=fl

            
                
            self.addCartItems(itemName,platesize,price,self.itemQuantity)

            self.addBilling()
            self.setTotal()

            top.destroy()


        self.itemSize=IntVar()
        self.itemSize.set(2)

        

        itemFrame=Frame(top,bd=3)
        itemFrame.place(x=0,y=0,height=150,width=300)

        foodTitleLabel=Label(itemFrame,text=itemName,font="sans-serif 15 bold",pady=10)
        foodTitleLabel.place(x=10,y=5,height=20,width=300)

        if(qt==0 and hf==0 and fl!=0):
            uttn=Button(itemFrame,text="-",font="arial 30 bold",pady=20,command=minus,borderwidth=0,fg="green")
            uttn.place(x=60,y=60,height=20,width=50)
            

            self.qtyEntry2=Text(itemFrame,font="arial 15 bold")
            self.qtyEntry2.place(x=130,y=60,width=30,height=30)
            self.qtyEntry2.insert(INSERT,self.val)
            self.qtyEntry2.tag_add("tag_name", "1.0", "end")
            self.qtyEntry2.tag_configure("tag_name", justify='center')

            uttn=Button(itemFrame,text="+",font="arial 30 bold",pady=0,command=plus,borderwidth=0,fg="green")
            uttn.place(x=180,y=60,height=20,width=50)


            add=Button(itemFrame,text="Add",font="arial 15 bold",pady=0,command=add,borderwidth=0,fg="white",bg="red")
            add.place(x=5,y=115,height=30,width=285)

        if(qt==0 and hf!=0 and fl!=0):
            radioHalf=Radiobutton(itemFrame,text="Half: "+"Rs "+str(hf),variable=self.itemSize,value=1,font="sans-serif 10 bold")
            radioHalf.place(x=0,y=35,width=170,height=15)

            radiofull=Radiobutton(itemFrame,text="Full: "+"Rs "+str(fl),variable=self.itemSize,value=2,font="sans-serif 10 bold")
            radiofull.place(x=0,y=55,width=170,height=15)

            uttn=Button(itemFrame,text="-",font="arial 30 bold",pady=20,command=minus,borderwidth=0,fg="green")
            uttn.place(x=60,y=80,height=20,width=50)

            self.qtyEntry2=Text(itemFrame,font="arial 15 bold")
            self.qtyEntry2.place(x=130,y=80,width=30,height=30)
            self.qtyEntry2.insert(INSERT,self.val)
            self.qtyEntry2.tag_add("tag_name", "1.0", "end")
            self.qtyEntry2.tag_configure("tag_name", justify='center')

            uttn=Button(itemFrame,text="+",font="arial 30 bold",pady=0,command=plus,borderwidth=0,fg="green")
            uttn.place(x=180,y=83,height=20,width=50)

            add=Button(itemFrame,text="Add",font="arial 15 bold",pady=0,command=add,borderwidth=0,fg="white",bg="red")
            add.place(x=5,y=115,height=30,width=285)

        if(qt!=0 and hf!=0 and fl!=0):
            radioHalf=Radiobutton(itemFrame,text="Quater: "+"Rs "+str(qt),variable=self.itemSize,value=0,font="sans-serif 10 bold")
            radioHalf.place(x=0,y=35,width=150,height=15)

            radioHalf=Radiobutton(itemFrame,text="Half: "+"Rs "+str(hf),variable=self.itemSize,value=1,font="sans-serif 10 bold")
            radioHalf.place(x=150,y=35,width=150,height=15)

            radiofull=Radiobutton(itemFrame,text="Full: "+"Rs "+str(fl),variable=self.itemSize,value=2,font="sans-serif 10 bold")
            radiofull.place(x=0,y=55,width=170,height=15)

            uttn=Button(itemFrame,text="-",font="arial 30 bold",pady=20,command=minus,borderwidth=0,fg="green")
            uttn.place(x=60,y=80,height=20,width=50)

            self.qtyEntry2=Text(itemFrame,font="arial 15 bold")
            self.qtyEntry2.place(x=130,y=80,width=30,height=30)
            self.qtyEntry2.insert(INSERT,self.val)
            self.qtyEntry2.tag_add("tag_name", "1.0", "end")
            self.qtyEntry2.tag_configure("tag_name", justify='center')

            uttn=Button(itemFrame,text="+",font="arial 30 bold",pady=0,command=plus,borderwidth=0,fg="green")
            uttn.place(x=180,y=83,height=20,width=50)

            add=Button(itemFrame,text="Add",font="arial 15 bold",pady=0,command=add,borderwidth=0,fg="white",bg="red")
            add.place(x=5,y=115,height=30,width=285)

        top.mainloop()


    def addCartItems(self,itemName,platesize,price,qty):
        f_itemName=str(itemName)+str(platesize)

        self.total=float(self.total)+float(price)*int(qty)

        flag=0
        
        for item in self.cartItems["itemName"]:
           if(f_itemName==item):
                flag=1
                loc=self.cartItems["itemName"].index(item)
                p_price=self.cartItems["itemPrice"][loc]
                p_quantity=self.cartItems["itemQuantity"][loc]


                l_price=float(price)+float(p_price)
                l_quantity=int(qty)+int(p_quantity)
                self.cartItems["itemPrice"][loc]=l_price
                self.cartItems["itemQuantity"][loc]=l_quantity 

        if(flag==0):
            self.cartItems["itemName"].append(f_itemName)
            self.cartItems["itemQuantity"].append(int(self.itemQuantity))
            self.cartItems["itemPrice"].append(price)


    

    
    def addBilling(self):
        self.billingTextBox.delete('1.0', END)
        for i in range(0,len(self.cartItems["itemName"])):
            totalPrice=0
            totalPrice=float(self.cartItems["itemPrice"][i])*int(self.cartItems["itemQuantity"][i])
            self.billingTextBox.tag_configure("center", justify='center')
            self.billingTextBox.insert(INSERT,"\n "+str(self.cartItems["itemName"][i])+":\n"+"Rs "+str(self.cartItems["itemPrice"][i])+"  X  "+str(self.cartItems["itemQuantity"][i])+" = "+"Rs "+str(totalPrice))
            self.billingTextBox.tag_add("center", "1.0", "end")

    def addTableItem(self,item,price):
        t_price=float(price)*int(self.qty.get())
        self.cartItems["itemName"].append(item)
        self.cartItems["itemQuantity"].append(self.qty.get())
        self.cartItems["itemPrice"].append(t_price)


        self.total=float(self.total)+float(price)*int(self.qty.get())

        self.addBilling()
        self.setTotal()



    def placeOrder(self,status):

        if(len(self.cartItems["itemName"])<1):
            messagebox.showerror("Error","Please select item first for print KOT")
        else:
            orderAddress=self.orderFrom
            odr=orderAddress[0:5]
            productItems=self.billingTextBox.get("1.0",'end-1c')
            now = datetime.datetime.now()
            dateTime=now.strftime("%d/%m/%Y %H:%M:%S")
            totalPrice=self.total

            if(str(odr)=="Table"):
                orderFrom="Table"
                tableNo=orderAddress[9:]
                self.db=Connection()
                self.conn=self.db.getConnection()
                self.cursor=self.db.getCursor()

                sql1="select orderAddress,productItems,totalPrice from pendingOrders where orderAddress='"+orderAddress+"'"
                self.cursor.execute(sql1)
                re=self.cursor.fetchone()
                if(re):
                    items=str(re[1])+str(productItems)
                    price=float(re[2])+float(totalPrice)
                    sql="update pendingOrders set productItems='"+str(items)+"', totalPrice='"+str(price)+"' where orderAddress='"+str(self.orderFrom)+"'"
                    self.cursor.execute(sql)
                    self.conn.commit()
                                
                else:
                    sql="insert into pendingOrders(orderId,orderFrom,productItems,orderAddress,dateTime,totalPrice) values('"+str(self.orderNo)+"','"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTime)+"','"+str(totalPrice)+"')"
                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.addOrderNo()

                    sql="update tablesData set tableStatus=1 where tableNo='"+str(tableNo)+"'"
                    self.cursor.execute(sql)
                    self.conn.commit()

                
                if(status==1):
                    self.printKOT(self.orderFrom,dateTime)
                messagebox.showinfo("success","Table Order Registered.")
                
                
                self.cursor.close()
                self.conn.close()
                self.root.withdraw()
                self.newWin=Toplevel(self.root)
                self.newObj=deshboard.MagicRestaurent(self.newWin)

            elif(orderAddress=="packing"):
                orderFrom="Packing"

                self.db=Connection()
                self.conn=self.db.getConnection()
                self.cursor=self.db.getCursor()

                sql="select orderAddress,productItems,totalPrice from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                result=self.cursor.fetchone()
                if(result):
                    items=str(result[1])+str(productItems)
                    price=float(result[2])+float(totalPrice)
                    sql="update pendingOrders set productItems='"+str(items)+"', totalPrice='"+str(price)+"' where orderId='"+self.id+"'"
                    self.cursor.execute(sql)
                    self.conn.commit()
                else:                  
                    sql="insert into pendingOrders(orderId,orderFrom,productItems,orderAddress,dateTime,totalPrice) values('"+str(self.orderNo)+"','"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTime)+"','"+str(totalPrice)+"')"
                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.addOrderNo()

                if(status==1):
                    self.printKOT(self.orderFrom,dateTime)
                messagebox.showinfo("success"," Order Registered.")
                
                
                self.cursor.close()
                self.conn.close()
                self.root.withdraw()
                self.newWin=Toplevel(self.root)
                self.newObj=deshboard.MagicRestaurent(self.newWin)

            else:
                now = datetime.datetime.now()
                dateTime=now.strftime("%d/%m/%Y %H:%M:%S")

                self.db=Connection()
                self.conn=self.db.getConnection()
                self.cursor=self.db.getCursor()

                sql="select orderAddress,productItems,totalPrice from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                result=self.cursor.fetchone()
                if(result):
                    items=str(result[1])+str(productItems)
                    price=float(result[2])+float(totalPrice)
                    sql="update pendingOrders set productItems='"+str(items)+"', totalPrice='"+str(price)+"' where orderId='"+str(self.id)+"'"
                    self.cursor.execute(sql)
                    self.conn.commit()
                else:                  
                    sql="insert into pendingOrders(orderId,orderFrom,productItems,orderAddress,dateTime,totalPrice) values('"+str(self.orderNo)+"','"+str(self.orderFrom)+"','"+str(productItems)+"','"+str(self.userAddress)+"','"+str(dateTime)+"','"+str(totalPrice)+"')"
                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.addOrderNo()

                if(status==1):
                    self.printKOT(self.orderFrom,dateTime)
                messagebox.showinfo("success","Order Registered.")
                

                self.cursor.close()
                self.conn.close()
                self.root.withdraw()
                self.newWin=Toplevel(self.root)
                self.newObj=deshboard.MagicRestaurent(self.newWin)


    def printKOT(self,orderFrom,dateTime):
        productItems=""

        items=[]
        quantity=[]
        for item in self.cartItems["itemName"]:
            items.append(item)

        for qty in self.cartItems["itemQuantity"]:
            quantity.append(qty)


        for i in range(0,len(items)):
            productItems=str(productItems)+" \n "+str(items[i])+"\t X "+str(quantity[i])


        kot="\n Bill : KOT "
        orderFrom="\n Odr By : "+str(orderFrom) 
        orderNo="\n Order No :"+str(self.orderNo)
        dateTimeOfOrder="\n "+str(dateTime)
        dash="\n __________________"
        headerItems="\n Item \t\t  Qty "
        purchasingItems="\n"+str(productItems)
        #purchasingItems="\n\n "
        textPrint=str(kot)+str(orderNo)+dash+str(orderFrom)+str(dash)+str(dateTimeOfOrder)+str(dash)+str(headerItems)+str(purchasingItems)+str(dash)

        #######
        ########printing KOT ####################

        fileName=tempfile.mktemp(".txt")
        open(fileName,"w").write(textPrint)
        os.startfile(fileName,"print")

        messagebox.showinfo("Success","K.O.T Printed Sucessfully")





if __name__=="__main__":
    root=Tk()
    obj=MainCourse(root)
    root.mainloop()