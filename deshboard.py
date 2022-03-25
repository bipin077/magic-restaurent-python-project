from sqlite3.dbapi2 import DateFromTicks
from tkinter import *
from Database_files import Connection
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
import time
from tkcalendar import DateEntry
from tkinter import ttk
import mainCourse 
import UpdateItems
import askAddressMob
import login
import paymentAndPrint


class MagicRestaurent:
    def __init__(self,root):
        self.root=root
        self.root.title("Magic Restaurent")
        self.root.geometry("1530x800+0+0")
        #self.root.resizable(False,False)
        self.root.config(bg="white")

        # this is to store frame so that we have to use in flush.......
        self.dashboard_frames=[]

        # total price to checkout
        self.total=0

        # this is to hold orders 
      
        self.holdOrders=[]

        self.notificationData=[]


        ##########################icons for bottom frame #############

        self.icon_addItems=Image.open("images/addItems.png")
        self.icon_addItems=self.icon_addItems.resize((30,30),Image.ANTIALIAS)
        self.icon_addItems=ImageTk.PhotoImage(self.icon_addItems)

        self.icon_viewOrders=Image.open("images/viewOrders.png")
        self.icon_viewOrders=self.icon_viewOrders.resize((30,30),Image.ANTIALIAS)
        self.icon_viewOrders=ImageTk.PhotoImage(self.icon_viewOrders)

        self.icon_proceed=Image.open("images/proceed.png")
        self.icon_proceed=self.icon_proceed.resize((40,25),Image.ANTIALIAS)
        self.icon_proceed=ImageTk.PhotoImage(self.icon_proceed)

        self.icon_newOrder=Image.open("images/newOrders.png")
        self.icon_newOrder=self.icon_newOrder.resize((30,30),Image.ANTIALIAS)
        self.icon_newOrder=ImageTk.PhotoImage(self.icon_newOrder)

        ###############################


        style = ttk.Style(root)
        # set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("clam")
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black", rowheight=50,font="arial 12 bold")
        style.configure('Treeview.Heading', foreground='brown', background='white',font="arial 12 bold",padding=5)
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        #====== Title =======

        

        self.icon_title=Image.open("images/logo.png")
        self.icon_title=self.icon_title.resize((50,50),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Magic Restaurent",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====== logout Button=======

        self.icon_logout=Image.open("images/logout.png")
        self.icon_logout=self.icon_logout.resize((40,30),Image.ANTIALIAS)
        self.icon_logout=ImageTk.PhotoImage(self.icon_logout)

        btn_logout=Button(self.root,text="Logout",font=("new time roman",15,"bold"),anchor="w",compound=LEFT,image=self.icon_logout,bg="red",cursor="hand2",fg="white",command=self.logout).place(x=1150,y=10,height=50,width=150)

        #=======clock======

        x = datetime.datetime.now()
        dateToday=x.strftime("%d/%m/%Y")

        self.lbl_clock=Label(self.root,text="Welcome To Magic Restaurent \t\t\t Date : "+ str(dateToday) +"\t\t\t\t Time : ",font=("time new roman",15,"bold"),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        self.timelabel = Label(self.root,font="arial 15 bold",bg="#4D636D",fg="white")
        self.timelabel.place(x=1200,y=70)

        self.timesnow()


        # ====== Left menu =======

        self.menuLogo=Image.open("images/logo_1.png")
        self.menuLogo=self.menuLogo.resize((300,120),Image.ANTIALIAS)
        self.menuLogo=ImageTk.PhotoImage(self.menuLogo)
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        #leftMenu.place(x=0,y=102,width=300,height=565)
        leftMenu.place(x=0,y=102,width=300,height=590)
        
        lbl_menuLogo=Label(leftMenu,image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side0=Image.open("images/allOrders.png")
        self.icon_side0=self.icon_side0.resize((40,40),Image.ANTIALIAS)
        self.icon_side0=ImageTk.PhotoImage(self.icon_side0)

        self.icon_side1=Image.open("images/table.png")
        self.icon_side1=self.icon_side1.resize((40,40),Image.ANTIALIAS)
        self.icon_side1=ImageTk.PhotoImage(self.icon_side1)

        self.icon_side2=Image.open("images/zomato_logo.png")
        self.icon_side2=self.icon_side2.resize((40,40),Image.ANTIALIAS)
        self.icon_side2=ImageTk.PhotoImage(self.icon_side2)

        self.icon_side3=Image.open("images/swiggy.png")
        self.icon_side3=self.icon_side3.resize((40,40),Image.ANTIALIAS)
        self.icon_side3=ImageTk.PhotoImage(self.icon_side3)

        self.icon_side4=Image.open("images/delivery.png")
        self.icon_side4=self.icon_side4.resize((40,40),Image.ANTIALIAS)
        self.icon_side4=ImageTk.PhotoImage(self.icon_side4)

        self.icon_side5=Image.open("images/food_package.png")
        self.icon_side5=self.icon_side5.resize((40,40),Image.ANTIALIAS)
        self.icon_side5=ImageTk.PhotoImage(self.icon_side5)

        self.icon_side6=Image.open("images/transaction.png")
        self.icon_side6=self.icon_side6.resize((40,40),Image.ANTIALIAS)
        self.icon_side6=ImageTk.PhotoImage(self.icon_side6)

        self.icon_side7=Image.open("images/admin_setting.png")
        self.icon_side7=self.icon_side7.resize((40,40),Image.ANTIALIAS)
        self.icon_side7=ImageTk.PhotoImage(self.icon_side7)

        lbl_menu=Label(leftMenu,text="Menu",font=("times new roman",20),bg="#009688",fg="white").pack(side=TOP,fill=X)

        btn_table=Button(leftMenu,text="  All Orders",command=self.allOrders,image=self.icon_side0,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_table=Button(leftMenu,text="  Table",command=self.table,image=self.icon_side1,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_zomato=Button(leftMenu,text="  Zomato",command=self.zomato,image=self.icon_side2,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_swiggi=Button(leftMenu,text="  Swiggi",command=self.swiggi,image=self.icon_side3,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_homeDevivery=Button(leftMenu,text="  Home Delivery",command=self.homeDelivery,image=self.icon_side4,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_packing=Button(leftMenu,text="  Packing",command=self.packing,image=self.icon_side5,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_totalTransaction=Button(leftMenu,text="  Total Transaction",command=self.totalTransaction,image=self.icon_side6,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_admin=Button(leftMenu,text="  Admin Area",image=self.icon_side7,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold"),command=self.adminPanel).pack(side=TOP,fill=X)
     
        self.allOrders()

            
    def timesnow(self):
        self.currentime=time.strftime ("%H:%M:%S")
        d = datetime.datetime.strptime(self.currentime, "%H:%M:%S")
        #self.timelabel.config (text=d.strftime("%I:%M %p"))
        self.timelabel.config (text=d.strftime("%r"))
        self.timelabel.after(1000,self.timesnow)


        #d = datetime.strptime("22:30", "%H:%M")
        #d.strftime("%I:%M %p")

    def logout(self):
        self.newWin=Toplevel(self.root)
        self.newObj=login.Login(self.newWin)
        self.root.withdraw()

    def dashboardFlush(self):
        for i in self.dashboard_frames:
            i.destroy()


    def processTable(self):

        self.processTableTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.processTableTitleFrame.place(x=303,y=103,height=50,width=1050)
        

        self.processTableTitleLabel=Label(self.processTableTitleFrame,text="Table",font="arial 20 bold",bg="#009688",fg="white")
        self.processTableTitleLabel.place(x=400,y=0)

        self.processTableFrame=Frame(self.root,bd=3)
        self.processTableFrame.place(x=300,y=153,height=537,width=1055)
        self.dashboard_frames.append(self.processTableFrame)

        self.row=0
        self.col=0

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select tableNo,tableStatus from tablesData"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if(len(result)<1):
            messagebox.showerror("ERROR","No Table Found in Database")
        for row in result:
            self.col=self.col+1
            if(row[1]==0):
                self.tableNo=Button(self.processTableFrame,text=row[0],bg="red",font="Arial 30 bold",padx=58,pady=6,width=3,command=lambda x=row[0]: self.addTableItem(x),bd=5)
                self.tableNo.grid(row=self.row,column=self.col)
            else:
                self.tableNo=Button(self.processTableFrame,text=row[0],bg="green",font="Arial 30 bold",padx=58,pady=6,width=3,command=self.showError,bd=5)
                self.tableNo.grid(row=self.row,column=self.col)
            
            if(self.col==5):
                self.col=0
                self.row=self.row+1

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def showError(self):
        messagebox.showinfo("error","Table order already in process")

    def addTableItem(self,id):
        tableNo="Table No "+str(id)
        self.newWin=Toplevel(self.root)
        self.newObj=mainCourse.MainCourse(self.newWin,tableNo,"None")
        self.root.withdraw()

    def allOrders(self):
        self.allOrdersTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.allOrdersTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.allOrdersTitleFrame)
        
        self.searchId=StringVar()

        self.allOrdersImage=Image.open("images/allOrders.png")
        self.allOrdersImage=self.allOrdersImage.resize((40,40),Image.ANTIALIAS)
        self.allOrdersImage=ImageTk.PhotoImage(self.allOrdersImage)


        self.allOrdersTitleLabel=Label(self.allOrdersTitleFrame,text="  All Running Orders",anchor="w",compound=LEFT,image=self.allOrdersImage,font="arial 20 bold",bg="#009688",fg="white")
        self.allOrdersTitleLabel.place(x=200,y=0)


        self.allOrdersEntry=Entry(self.allOrdersTitleFrame,font="sans-serif 15 normal",textvariable=self.searchId)
        self.allOrdersEntry.place(x=750,y=10)

        self.searchBtn=Image.open("images/search.png")
        self.searchBtn=self.searchBtn.resize((40,30),Image.ANTIALIAS)
        self.searchBtn=ImageTk.PhotoImage(self.searchBtn)

        self.allOrdersButton=Button(self.allOrdersTitleFrame,image=self.searchBtn,font="arial 12 bold",bg="#009688",borderwidth=0,cursor="hand2",command=self.searchOrderId)
        self.allOrdersButton.place(x=990,y=5)
        

        self.allOrdersFrame=Frame(self.root,bd=3)
        self.allOrdersFrame.place(x=300,y=153,height=470,width=1055)
        self.dashboard_frames.append(self.allOrdersFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

              
        

        columns = ("Order No","Order From","Order Address","DateTime Of Order","Total Price")
        self.treeview_allOrders = ttk.Treeview(self.allOrdersFrame, height=18, show="headings", columns=columns)


        self.treeview_allOrders.column("Order No", width=50, anchor='center')
        self.treeview_allOrders.column("Order From", width=50, anchor='center')
        self.treeview_allOrders.column("Order Address", width=350, anchor='center')
        self.treeview_allOrders.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_allOrders.column("Total Price", width=100, anchor='center')
 
        self.treeview_allOrders.heading("Order No", text="Order No")
        self.treeview_allOrders.heading("Order From", text="Order From")
        self.treeview_allOrders.heading("Order Address", text="Order Address") 
        self.treeview_allOrders.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_allOrders.heading("Total Price", text="Total Price")
        #self.treeview_allOrders.bind('<Button-1>', self.tableViewItems)
        #self.treeview_allOrders.bind('<Button-1>', self.processOrderAndPrint_table)
        #self.treeview_allOrders.bind("<Double-Button-1>", self.processOrderAllOrders)
        
 
        self.treeview_allOrders.place(x=0,y=0,height=535,width=1050)

        sql="select * from pendingOrders"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_allOrders.focus_set()
        for row in result:
            self.treeview_allOrders.insert(parent='', index=0, text='', values=(row[0],row[1],row[3],row[4],"Rs "+row[5]))
            children = self.treeview_allOrders.get_children()
            if children:
                self.treeview_allOrders.focus(children[0])
                self.treeview_allOrders.selection_set(children[0])


        self.allOrdersBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.allOrdersBottomFrame.place(x=303,y=630,height=60,width=1050)


        self.addItems=Button(self.allOrdersBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsAllOrders,bd=3,cursor="hand2")
        self.addItems.place(x=200,y=5,width=150)

        self.viewOrderItems=Button(self.allOrdersBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.allOrdersViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=370,y=5,width=175)

        self.proceedOrder=Button(self.allOrdersBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAllOrders,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=565,y=5,width=170)


    def searchOrderId(self):
        orderId=self.searchId.get()
        sql="select * from pendingOrders where orderId='"+str(orderId)+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_allOrders.focus_set()
        for row in result:
            for i in self.treeview_allOrders.get_children():
                self.treeview_allOrders.delete(i)
            self.treeview_allOrders.insert(parent='', index=0, text='', values=(row[0],row[1],row[3],row[4],row[5]+" Rs"))
            children = self.treeview_allOrders.get_children()
            if children:
                self.treeview_allOrders.focus(children[0])
                self.treeview_allOrders.selection_set(children[0])

    def processOrderAllOrders(self):
        curItem = self.treeview_allOrders.focus()
        values=self.treeview_allOrders.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.process(id)
        
    def table(self):
        
        orderFrom="Table"
        self.tableTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.tableTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.tableTitleFrame)

        self.tableImage=Image.open("images/table.png")
        self.tableImage=self.tableImage.resize((40,40),Image.ANTIALIAS)
        self.tableImage=ImageTk.PhotoImage(self.tableImage)

        self.tableTitleLabel=Label(self.tableTitleFrame,text=" Table Running Orders",anchor="w",image=self.tableImage,compound=LEFT,font="arial 20 bold",bg="#009688",fg="white")
        self.tableTitleLabel.place(x=300,y=0)

        self.tableFrame=Frame(self.root,bd=3)
        self.tableFrame.place(x=300,y=153,height=475,width=1055)
        self.dashboard_frames.append(self.tableFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

              
        

        columns = ("Order No","Order Address","DateTime Of Order","Total Price")
        self.treeview_table = ttk.Treeview(self.tableFrame, height=18, show="headings", columns=columns)


        self.treeview_table.column("Order No", width=50, anchor='center')
        self.treeview_table.column("Order Address", width=350, anchor='center')
        self.treeview_table.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_table.column("Total Price", width=100, anchor='center')
 
        self.treeview_table.heading("Order No", text="Order No")
        self.treeview_table.heading("Order Address", text="Order Address") 
        self.treeview_table.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_table.heading("Total Price", text="Total Price")
        self.treeview_table.bind('<Button-1>', self.tableViewItems)
        self.treeview_table.bind('<Button-1>', self.processOrderAndPrint_table)
        
 
        self.treeview_table.place(x=0,y=0,height=470,width=1050)

        sql="select orderAddress,dateTime,totalPrice,orderId from pendingOrders where orderFrom='"+orderFrom+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_table.focus_set()
        for row in result:
            #self.treeview_table.insert(parent='', index=0, iid=0, text='', values=(row[3],row[0],row[1],u"\u20B9 "+row[2]))
            self.treeview_table.insert(parent='', index=0, text='', values=(row[3],row[0],row[1],"Rs "+row[2]))
            children = self.treeview_table.get_children()
            if children:
                self.treeview_table.focus(children[0])
                self.treeview_table.selection_set(children[0])

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


        self.tableBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.tableBottomFrame.place(x=303,y=630,height=60,width=1050)
        self.dashboard_frames.append(self.tableBottomFrame)


        self.addItems=Button(self.tableBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsTable,bd=3,cursor="hand2")
        self.addItems.place(x=150,y=5,width=150)

        self.viewOrderItems=Button(self.tableBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.tableViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=320,y=5,width=175)

        self.proceedOrder=Button(self.tableBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAndPrint_table,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=515,y=5,width=150)

        self.addNewOrder=Button(self.tableBottomFrame,text=" New Order",anchor="w",compound=LEFT,image=self.icon_newOrder,font="Arial 15 bold",width=17,command=lambda x=orderFrom: self.processAddNewOrder(x),bd=3,bg="green",fg="white",cursor="hand2")
        self.addNewOrder.place(x=685,y=5,width=160)

    def addMoreItemsAllOrders(self):
        curItem = self.treeview_allOrders.focus()
        values=self.treeview_allOrders.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            orderFrom=values[2]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,orderFrom,"None",id)
    
    def addMoreItemsTable(self):
        curItem = self.treeview_table.focus()
        values=self.treeview_table.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            orderFrom=values[1]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,orderFrom,"None",id)

    def addMoreItemsZomato(self):
        curItem = self.treeview_zomato.focus()
        values=self.treeview_zomato.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,"Zomato","None",id)

    def addMoreItemsSwiggi(self):
        curItem = self.treeview_swiggi.focus()
        values=self.treeview_swiggi.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,"Swiggi","None",id)

    def addMoreItemsHomeDelivery(self):
        curItem = self.treeview_homeDelivery.focus()
        values=self.treeview_homeDelivery.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,"Home Delivery","None",id)

    def addMoreItemsPacking(self):
        curItem = self.treeview_packing.focus()
        values=self.treeview_packing.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,"Packing","None",id)

    def tableViewItems(self):
        curItem = self.treeview_table.focus()
        values=self.treeview_table.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item \t  X \t  Quantity = \t Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def zomato(self):
        orderFrom="zomato"
        self.zomatoTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.zomatoTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.zomatoTitleFrame)

        self.zomatoImage=Image.open("images/zomato_logo.png")
        self.zomatoImage=self.zomatoImage.resize((40,40),Image.ANTIALIAS)
        self.zomatoImage=ImageTk.PhotoImage(self.zomatoImage)

        self.zomatoTitleLabel=Label(self.zomatoTitleFrame,text=" Zommato Running Orders",anchor="w",compound=LEFT,image=self.zomatoImage,font="arial 20 bold",bg="#009688",fg="white")
        self.zomatoTitleLabel.place(x=300,y=0)

        self.zomatoFrame=Frame(self.root,bd=3)
        self.zomatoFrame.place(x=300,y=153,height=475,width=1055)
        self.dashboard_frames.append(self.zomatoFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        columns = ("Order No","Order Address","DateTime Of Order","Total Price")
        self.treeview_zomato = ttk.Treeview(self.zomatoFrame, height=18, show="headings", columns=columns)

        self.treeview_zomato.column("Order No", width=50, anchor='center')
        self.treeview_zomato.column("Order Address", width=350,anchor='center')
        self.treeview_zomato.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_zomato.column("Total Price", width=100, anchor='center')
 
        self.treeview_zomato.heading("Order No", text="Order No")
        self.treeview_zomato.heading("Order Address", text="Order Address") 
        self.treeview_zomato.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_zomato.heading("Total Price", text="Total Price")
        self.treeview_zomato.bind('<Button-1>', self.zomatoViewItems)
        self.treeview_zomato.bind('<Button-1>', self.processOrderAndPrint_zomato)

        #self.treeview_zomato.focus('column')
 
        self.treeview_zomato.place(x=0,y=0,height=470,width=1050)

        sql="select orderId,orderAddress,dateTime,totalPrice from pendingOrders where orderFrom='"+orderFrom+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_zomato.focus_set()
        for row in result:
            self.treeview_zomato.insert(parent='', index=0, text='', values=(row[0],row[1],row[2],"Rs "+row[3]))
            children = self.treeview_zomato.get_children()
            if children:
                self.treeview_zomato.focus(children[0])
                self.treeview_zomato.selection_set(children[0])


        self.conn.commit()
        self.cursor.close()
        self.conn.close()



        self.zomatoBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.zomatoBottomFrame.place(x=303,y=630,height=60,width=1050)
        self.dashboard_frames.append(self.zomatoBottomFrame)

        self.addItems=Button(self.zomatoBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsZomato,bd=3,cursor="hand2")
        self.addItems.place(x=150,y=5,width=150)

        self.viewOrderItems=Button(self.zomatoBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.zomatoViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=320,y=5,width=175)

        self.proceedOrder=Button(self.zomatoBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAndPrint_zomato,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=515,y=5,width=150)

        self.addNewOrder=Button(self.zomatoBottomFrame,text=" New Order",anchor="w",compound=LEFT,image=self.icon_newOrder,font="Arial 15 bold",width=17,command=lambda x=orderFrom: self.processAddNewOrder(x),bd=3,bg="green",fg="white",cursor="hand2")
        self.addNewOrder.place(x=685,y=5,width=160)

    def swiggi(self):
        orderFrom="swiggi"
        self.swiggiTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.swiggiTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.swiggiTitleFrame)

        self.swiggiImage=Image.open("images/swiggy.png")
        self.swiggiImage=self.swiggiImage.resize((40,40),Image.ANTIALIAS)
        self.swiggiImage=ImageTk.PhotoImage(self.swiggiImage)


        self.swiggiTitleLabel=Label(self.swiggiTitleFrame,text="  Swiggi Running Orders",anchor="w",image=self.swiggiImage,compound=LEFT,font="arial 20 bold",bg="#009688",fg="white")
        self.swiggiTitleLabel.place(x=300,y=0)

        self.swiggiFrame=Frame(self.root,bd=3)
        self.swiggiFrame.place(x=300,y=153,height=475,width=1055) 
        self.dashboard_frames.append(self.swiggiFrame)  


        self.swiggiBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.swiggiBottomFrame.place(x=303,y=630,height=60,width=1050)
        self.dashboard_frames.append(self.swiggiBottomFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        columns = ("Order No","Order Address","DateTime Of Order","Total Price")
        self.treeview_swiggi = ttk.Treeview(self.swiggiFrame, height=18, show="headings", columns=columns)

        self.treeview_swiggi.column("Order No", width=50, anchor='center')
        self.treeview_swiggi.column("Order Address", width=350, anchor='center')
        self.treeview_swiggi.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_swiggi.column("Total Price", width=100, anchor='center')
 
        self.treeview_swiggi.heading("Order No", text="Order No")
        self.treeview_swiggi.heading("Order Address", text="Order Address") 
        self.treeview_swiggi.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_swiggi.heading("Total Price", text="Total Price")
        self.treeview_swiggi.bind('<Button-1>', self.swiggiViewItems)
        self.treeview_swiggi.bind('<Button-1>', self.processOrderAndPrint_swiggi)
 
        self.treeview_swiggi.place(x=0,y=0,height=470,width=1050)

        sql="select orderId,orderAddress,dateTime,totalPrice from pendingOrders where orderFrom='"+orderFrom+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_swiggi.focus_set()
        for row in result:
            self.treeview_swiggi.insert(parent='', index=0, text='', values=(row[0],row[1],row[2],row[3]))
            children = self.treeview_swiggi.get_children()
            if children:
                self.treeview_swiggi.focus(children[0])
                self.treeview_swiggi.selection_set(children[0])


        self.conn.commit()
        self.cursor.close()
        self.conn.close()


        self.addItems=Button(self.swiggiBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsSwiggi,bd=3,cursor="hand2")
        self.addItems.place(x=150,y=5,width=150)

        self.viewOrderItems=Button(self.swiggiBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.swiggiViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=320,y=5,width=175)

        self.proceedOrder=Button(self.swiggiBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAndPrint_swiggi,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=515,y=5,width=150)

        self.addNewOrder=Button(self.swiggiBottomFrame,text=" New Order",anchor="w",compound=LEFT,image=self.icon_newOrder,font="Arial 15 bold",width=17,command=lambda x=orderFrom: self.processAddNewOrder(x),bd=3,bg="green",fg="white",cursor="hand2")
        self.addNewOrder.place(x=685,y=5,width=160)

    def homeDelivery(self):
        orderFrom="homeDelivery"

        self.homeDeliveryTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.homeDeliveryTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.homeDeliveryTitleFrame)

        self.homeDeliveryImage=Image.open("images/delivery.png")
        self.homeDeliveryImage=self.homeDeliveryImage.resize((40,40),Image.ANTIALIAS)
        self.homeDeliveryImage=ImageTk.PhotoImage(self.homeDeliveryImage)


        self.homeDeliveryTitleLabel=Label(self.homeDeliveryTitleFrame,text="  Home Delivery Running Orders",anchor="w",image=self.homeDeliveryImage,compound=LEFT,font="arial 20 bold",bg="#009688",fg="white")
        self.homeDeliveryTitleLabel.place(x=300,y=0)

        self.homeDeliveryFrame=Frame(self.root,bd=3)
        self.homeDeliveryFrame.place(x=300,y=153,height=475,width=1055)  
        self.dashboard_frames.append(self.homeDeliveryFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        columns = ("Order No","Order Address","DateTime Of Order","Total Price")
        self.treeview_homeDelivery = ttk.Treeview(self.homeDeliveryFrame, height=18, show="headings", columns=columns)

        self.treeview_homeDelivery.column("Order No", width=50, anchor='center')
        self.treeview_homeDelivery.column("Order Address", width=350, anchor='center')
        self.treeview_homeDelivery.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_homeDelivery.column("Total Price", width=100, anchor='center')
 
        self.treeview_homeDelivery.heading("Order No", text="Order No")
        self.treeview_homeDelivery.heading("Order Address", text="Order Address") 
        self.treeview_homeDelivery.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_homeDelivery.heading("Total Price", text="Total Price")
        self.treeview_homeDelivery.bind('<Button-1>',self.homeDeliveryViewItems)
        self.treeview_homeDelivery.bind('<Button-1>', self.processOrderAndPrint_homeDelivery)
 
        self.treeview_homeDelivery.place(x=0,y=0,height=470,width=1050)

        sql="select orderId,orderAddress,dateTime,totalPrice from pendingOrders where orderFrom='"+orderFrom+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_homeDelivery.focus_set()
        for row in result:
            self.treeview_homeDelivery.insert(parent='', index=0, text='', values=(row[0],row[1],row[2],"Rs "+row[3]))
            children = self.treeview_homeDelivery.get_children()
            if children:
                self.treeview_homeDelivery.focus(children[0])
                self.treeview_homeDelivery.selection_set(children[0])


        self.conn.commit()
        self.cursor.close()
        self.conn.close()


        self.homeDeliveryBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.homeDeliveryBottomFrame.place(x=303,y=630,height=60,width=1050)
        self.dashboard_frames.append(self.homeDeliveryBottomFrame)


        self.addItems=Button(self.homeDeliveryBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsHomeDelivery,bd=3,cursor="hand2")
        self.addItems.place(x=150,y=5,width=150)

        self.viewOrderItems=Button(self.homeDeliveryBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.homeDeliveryViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=320,y=5,width=175)

        self.proceedOrder=Button(self.homeDeliveryBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAndPrint_homeDelivery,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=515,y=5,width=150)

        self.addNewOrder=Button(self.homeDeliveryBottomFrame,text=" New Order",anchor="w",compound=LEFT,image=self.icon_newOrder,font="Arial 15 bold",width=17,command=lambda x=orderFrom: self.processAddNewOrder(x),bd=3,bg="green",fg="white",cursor="hand2")
        self.addNewOrder.place(x=685,y=5,width=160)

    def packing(self):
        orderFrom="Packing"

        self.packingTitleFrame=Frame(self.root,bd=3,bg="#009688")
        self.packingTitleFrame.place(x=303,y=103,height=50,width=1050)
        self.dashboard_frames.append(self.packingTitleFrame)

        self.packingImage=Image.open("images/food_package.png")
        self.packingImage=self.packingImage.resize((40,40),Image.ANTIALIAS)
        self.packingImage=ImageTk.PhotoImage(self.packingImage)


        self.packingTitleLabel=Label(self.packingTitleFrame,text="  Packing Running Orders",anchor="w",image=self.packingImage,compound=LEFT,font="arial 20 bold",bg="#009688",fg="white")
        self.packingTitleLabel.place(x=300,y=0)

        self.packingFrame=Frame(self.root,bd=3)
        self.packingFrame.place(x=300,y=153,height=475,width=1055)  
        self.dashboard_frames.append(self.packingFrame)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        columns = ("Order No","Order Address","DateTime Of Order","Total Price")
        self.treeview_packing = ttk.Treeview(self.packingFrame, height=18, show="headings", columns=columns)

        self.treeview_packing.column("Order No", width=50, anchor='center')
        self.treeview_packing.column("Order Address", width=350, anchor='center')
        self.treeview_packing.column("DateTime Of Order", width=100, anchor='center')
        self.treeview_packing.column("Total Price", width=100, anchor='center')
 
        self.treeview_packing.heading("Order No", text="Order No")
        self.treeview_packing.heading("Order Address", text="Order Address") 
        self.treeview_packing.heading("DateTime Of Order", text="DateTime Of Order")
        self.treeview_packing.heading("Total Price", text="Total Price")
        self.treeview_packing.bind('<Button-1>',self.homeDeliveryViewItems)
        self.treeview_packing.bind('<Button-1>', self.processOrderAndPrint_packing)
 
        self.treeview_packing.place(x=0,y=0,height=470,width=1050)

        sql="select orderId,orderAddress,dateTime,totalPrice from pendingOrders where orderFrom='"+orderFrom+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.treeview_packing.focus_set()
        for row in result:
            self.treeview_packing.insert(parent='', index=0, text='', values=(row[0],row[1],row[2],"Rs "+row[3]))
            children = self.treeview_packing.get_children()
            if children:
                self.treeview_packing.focus(children[0])
                self.treeview_packing.selection_set(children[0])


        self.conn.commit()
        self.cursor.close()
        self.conn.close()


        self.packingBottomFrame=Frame(self.root,bd=3,bg="#009688")
        self.packingBottomFrame.place(x=303,y=630,height=60,width=1050)
        self.dashboard_frames.append(self.packingBottomFrame)
        

        self.addItems=Button(self.packingBottomFrame,text=" Add Items",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_addItems,font="Arial 15 bold",width=17,command=self.addMoreItemsPacking,bd=3,cursor="hand2")
        self.addItems.place(x=150,y=5,width=150)

        self.viewOrderItems=Button(self.packingBottomFrame,text=" View Orders",anchor="w",bg="green",fg="white",compound=LEFT,image=self.icon_viewOrders,font="Arial 15 bold",width=20,command=self.packingViewItems,bd=3,cursor="hand2")
        self.viewOrderItems.place(x=320,y=5,width=175)

        self.proceedOrder=Button(self.packingBottomFrame,text="Checkout",anchor="w",compound=LEFT,image=self.icon_proceed,command=self.processOrderAndPrint_packing,font="Arial 15 bold",width=16,bd=3,bg="green",fg="white",cursor="hand2")
        self.proceedOrder.place(x=515,y=5,width=150)

        self.addNewOrder=Button(self.packingBottomFrame,text=" New Order",anchor="w",compound=LEFT,image=self.icon_newOrder,font="Arial 15 bold",width=17,command=lambda x=orderFrom: self.processAddNewOrder(x),bd=3,bg="green",fg="white",cursor="hand2")
        self.addNewOrder.place(x=685,y=5,width=160)

    def processAddNewOrder(self,orderFrom):
        if(orderFrom=="swiggi"):
            self.newWin=Toplevel(self.root)
            self.newObj=askAddressMob.GetAddressMob(self.newWin,"swiggi",id)

        if(orderFrom=="zomato"):
            self.newWin=Toplevel(self.root)
            self.newObj=askAddressMob.GetAddressMob(self.newWin,"zomato",id)

        if(orderFrom=="homeDelivery"):
            self.newWin=Toplevel(self.root)
            self.newObj=askAddressMob.GetAddressMob(self.newWin,"homeDelivery",id)

        if(orderFrom=="Table"):
            self.processTable()

        if(orderFrom=="Packing"):
            self.newWin=Toplevel(self.root)
            self.newObj=mainCourse.MainCourse(self.newWin,"packing","None",id)
            self.root.withdraw()

    def processOrderAndPrint_swiggi(self):
        curItem = self.treeview_swiggi.focus()
        values=self.treeview_swiggi.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]    
            self.process(id)

    def processOrderAndPrint_table(self):
        curItem = self.treeview_table.focus()
        values=self.treeview_table.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.process(id)

    def processOrderAndPrint_zomato(self):
        curItem = self.treeview_zomato.focus()
        values=self.treeview_zomato.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            
            self.process(id)

    def processOrderAndPrint_packing(self):
        curItem = self.treeview_packing.focus()
        values=self.treeview_packing.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            self.process(id)

    def processOrderAndPrint_homeDelivery(self):
        curItem = self.treeview_homeDelivery.focus()
        values=self.treeview_homeDelivery.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]
            
            self.process(id)

    def process(self,id):
        self.newWin=Toplevel(self.root)
        self.newObj=paymentAndPrint.PaymentAndBill(self.newWin,id)
        self.root.withdraw()
        
        

    
    def adminPanel(self):
        self.adminPanelFrame=Frame(self.root,bd=3,bg="gray")
        self.adminPanelFrame.place(x=303,y=103,height=590,width=1050)  

        self.adminTopFrame1=Frame(self.adminPanelFrame,bd=2,bg="#009688")
        self.adminTopFrame1.place(x=0,y=0,width=1050,height=50)

        self.adminTopFrame2=Frame(self.adminPanelFrame,bd=2,bg="#009688")
        self.adminTopFrame2.place(x=0,y=55,width=1050,height=50)

        ################# Admin frame 1 items #####################

        self.addCategory=Button(self.adminTopFrame1,text="Add Category",font="Arial 15 bold",width=20,bg="#f8c471",command=self.addNewCategory)
        self.addCategory.place(x=10,y=3,width=150,height=40)

        self.addProduct=Button(self.adminTopFrame1,text="Add Item",font="Arial 15 bold",width=20,bg="#f8c471",command=self.addNewItem)
        self.addProduct.place(x=170,y=3,width=150,height=40)

        self.updateProduct=Button(self.adminTopFrame1,text="Update Item",font="Arial 15 bold",width=20,bg="#f8c471",command=self.updateItem)
        self.updateProduct.place(x=330,y=3,width=150,height=40)

        self.deleteProduct=Button(self.adminTopFrame1,text="Delete Item",font="Arial 15 bold",width=20,bg="#f8c471",command=self.deleteItem)
        self.deleteProduct.place(x=490,y=3,width=150,height=40)

        self.addTable=Button(self.adminTopFrame1,text="Add Table",font="Arial 15 bold",width=20,bg="#f8c471",command=self.addTableData)
        self.addTable.place(x=650,y=3,width=150,height=40)

        self.deleteTable=Button(self.adminTopFrame1,text="Delete Table",font="Arial 15 bold",width=20,bg="#f8c471",command=self.deleteTableData)
        self.deleteTable.place(x=810,y=3,width=150,height=40)

        ################# Admin frame 2 items #####################


        self.removeCategory=Button(self.adminTopFrame2,text="Update Category",font="Arial 15 bold",width=20,bg="#f8c471",command=self.updateCategoryData)
        self.removeCategory.place(x=10,y=3,width=180,height=40)

        

        self.updateTaxes=Button(self.adminTopFrame2,text="Update Taxes",font="Arial 15 bold",width=20,bg="#f8c471",command=self.updateTaxesData)
        self.updateTaxes.place(x=200,y=3,width=150,height=40)

        self.addNewCategory()

  
    def updateTaxesData(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1050,height=550)

        self.addNewCategoryFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.addNewCategoryFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.addNewCategoryFrame,text="Update Taxes ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select * from additionalTaxes"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        cgst=result[0]
        sgst=result[2]
        discount=result[2]


        self.cgst=StringVar()
        self.sgst=StringVar()
        self.discount=StringVar()


        self.updateTaxFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="#009688")
        self.updateTaxFrame.place(x=15,y=70,width=1010,height=350)

        cgstLabel=Label(self.updateTaxFrame,text="CGST : ",font="arial 15 bold",bg="#009688")
        cgstLabel.place(x=200,y=50,width=100,height=50)

        cgstEntry=Entry(self.updateTaxFrame,font="sans-serif 15 bold",textvariable=self.cgst)
        cgstEntry.place(x=350,y=60,width=200,height=30)
        cgstEntry.insert(INSERT,cgst)


        cgstPstLabel=Label(self.updateTaxFrame,text=" %",font="arial 15 bold",bg="#009688")
        cgstPstLabel.place(x=570,y=50,width=100,height=50)

        sgstLabel=Label(self.updateTaxFrame,text="SGST : ",font="arial 15 bold",bg="#009688")
        sgstLabel.place(x=200,y=100,width=100,height=50)

        sgstEntry=Entry(self.updateTaxFrame,font="sans-serif 15 bold",textvariable=self.sgst)
        sgstEntry.place(x=350,y=110,width=200,height=30)
        sgstEntry.insert(INSERT,sgst)

        sgstPstLabel=Label(self.updateTaxFrame,text=" %",font="arial 15 bold",bg="#009688")
        sgstPstLabel.place(x=570,y=100,width=100,height=50)

        discountLabel=Label(self.updateTaxFrame,text="Discount : ",font="arial 15 bold",bg="#009688")
        discountLabel.place(x=200,y=150,width=100,height=50)

        discountEntry=Entry(self.updateTaxFrame,font="sans-serif 15 bold",textvariable=self.discount)
        discountEntry.place(x=350,y=160,width=200,height=30)
        discountEntry.insert(INSERT,discount)

        discountPstLabel=Label(self.updateTaxFrame,text=" %",font="arial 15 bold",bg="#009688")
        discountPstLabel.place(x=570,y=150,width=100,height=50)

        updateTaxesBtn=Button(self.updateTaxFrame,text="Update Taxes",font="sans-serif 15 bold",bg="red",fg="white",command=self.updateTaxesDb)
        updateTaxesBtn.place(x=250,y=230,width=150,height=40)

    def updateTaxesDb(self):
        cgst=self.cgst.get()
        sgst=self.sgst.get()
        discount=self.discount.get()

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="update additionalTaxes set CGST='"+str(cgst)+"', SGST='"+str(sgst)+"',Discount='"+str(discount)+"'"
        self.cursor.execute(sql)
        self.conn.commit()

        messagebox.showinfo("success","Taxes Updated Sucessfully")

        self.cursor.close()
        self.conn.close()

        self.adminPanel()
        
    def updateCategoryData(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1050,height=550)

        self.updateCategoryFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.updateCategoryFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.updateCategoryFrame,text="Update Category ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.updateFrame=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.updateFrame.place(x=15,y=75,width=1010,height=50)

        self.tkvar = StringVar(self.root)
        self.tkvar.set("None") 
    

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()
        
        self.updateCategoryLabel=Label(self.updateFrame, text="Choose Category : ",pady=10,width=30,font="arial 15 bold",bg="#009688",fg="white")
        self.updateCategoryLabel.place(x=50,y=0)

        query="select categoryName from foodCategories"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        data=[]
        for row in records:
            data.append(row[0])
        

        self.chooseCategory_u_u=OptionMenu(self.updateFrame,self.tkvar,*data)
        self.chooseCategory_u_u.place(x=380,y=10)

        self.foodName=StringVar()
        

        self.getProductDetails_u_u=Button(self.updateFrame,text="Get items",font="arial 12 bold",fg="white",bg="red",command=self.updateCategoryForm)
        self.getProductDetails_u_u.place(x=570,y=5)

    def updateCategoryForm(self):
        self.updateFrameForm=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.updateFrameForm.place(x=15,y=140,width=1010,height=300)

        categoryName=self.tkvar.get()
        self.categoryname=StringVar()

        label=Label(self.updateFrameForm,text="Category Name  : ",font="arial 15 bold",bg="#009688")
        label.place(x=200,y=50,width=200,height=50)

        entry=Entry(self.updateFrameForm,font="sans-serif 15 bold",textvariable=self.categoryname)
        entry.place(x=450,y=60,width=200,height=30)
        entry.insert(INSERT,categoryName)

        updateTaxesBtn=Button(self.updateFrameForm,text="Update Category",font="sans-serif 15 bold",bg="red",fg="white",command=self.updateCategoryDb)
        updateTaxesBtn.place(x=300,y=130,width=200,height=40)
        
    def updateCategoryDb(self):
        o_categoryName=self.tkvar.get()
        u_categoryName=self.categoryname.get()

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="update foodCategories set categoryName='"+u_categoryName+"' where categoryName='"+o_categoryName+"'"
        self.cursor.execute(query)
        self.conn.commit()

        messagebox.showinfo("Success","Category Updated Sucessfully")

        self.cursor.close()
        self.conn.close()

        self.adminPanel()



    def deleteTableData(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1050,height=550)

        self.addNewCategoryFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.addNewCategoryFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.addNewCategoryFrame,text="Delete Table Data ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.tkvar = StringVar(self.root)
        self.tkvar.set("None") 

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()


        query="select tableNo from tablesData"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        items=[]
        for row in records:
            items.append(row[0])

        self.deleteItemFrame_s=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.deleteItemFrame_s.place(x=15,y=80,width=1010,height=50)


        self.chooseCategoryLabel_u_u=Label(self.deleteItemFrame_s, text="Choose Table No : ",pady=10,width=30,font="arial 15 bold",bg="#009688",fg="white")
        self.chooseCategoryLabel_u_u.place(x=50,y=0)
      

        self.chooseCategory_u_u=OptionMenu(self.deleteItemFrame_s,self.tkvar,*items)
        self.chooseCategory_u_u.place(x=380,y=10)
        

        self.getProductDetails_u_u=Button(self.deleteItemFrame_s,text="Delete Table",command=self.deleteTableDb,font="arial 12 bold",bg="red",fg="white")
        self.getProductDetails_u_u.place(x=550,y=5)


    def deleteTableDb(self):
        tableNo=self.tkvar.get()

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()


        query="delete from tablesData where tableNo='"+str(tableNo)+"'"
        self.cursor.execute(query)
        self.conn.commit()

        messagebox.showinfo("Success","Table Deleted Sucessfully")
        self.deleteTableData()


    def addTableData(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1050,height=550)

        self.addNewCategoryFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.addNewCategoryFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.addNewCategoryFrame,text="Add Table Data",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)


        self.addTableFrame=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.addTableFrame.place(x=15,y=80,width=1010,height=50)


        self.chooseCategoryLabel_u_u=Label(self.addTableFrame, text="Choose Table No : ",pady=10,width=30,font="arial 13 bold",bg="#009688",fg="white")
        self.chooseCategoryLabel_u_u.place(x=100,y=0)
      

        self.EnterTabelNo=Spinbox(self.addTableFrame, from_= 1, to = 50,font="arial 15 bold")  
        self.EnterTabelNo.place(x=400,y=10,width=50)
        

        self.getProductDetails_u_u=Button(self.addTableFrame,text="Add Table",command=self.addTableDb,font="arial 13 bold",bg="red",fg="white")
        self.getProductDetails_u_u.place(x=580,y=5)

    def addTableDb(self):
        tableNo=self.EnterTabelNo.get()
        temp=0

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="select tableNo from tablesData"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        items=[]
        for row in records:
            if str(row[0])==str(tableNo):
                temp=1
        
        if temp!=0:
            messagebox.showerror("ERROR","Table already Exist")
            self.addTableData()
        else:
            query="insert into tablesData(tableNo,tableStatus) values('"+tableNo+"','0')"
            self.cursor.execute(query)
            self.conn.commit()

            messagebox.showinfo("Success","Table Inserted Sucessfully")
            self.addTableData()



    def deleteItem(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1030,height=520)

        self.deleteItemLabelFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.deleteItemLabelFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.deleteItemLabelFrame,text="Delete Item ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.deleteItemFrame=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.deleteItemFrame.place(x=15,y=75,width=1010,height=50)


        self.tkvar = StringVar(self.root)
        self.tkvar.set("None") 

        
        self.tkvar1 = StringVar(self.root)
        self.tkvar1.set("None") 
    

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()
        
        self.chooseCategoryLabel_u_u=Label(self.deleteItemFrame, text="Choose Category : ",pady=10,width=30,font="arial 15 bold",bg="#009688",fg="white")
        self.chooseCategoryLabel_u_u.place(x=100,y=0)

        query="select categoryName from foodCategories"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        data=[]
        for row in records:
            data.append(row[0])
        

        self.chooseCategory_u_u=OptionMenu(self.deleteItemFrame,self.tkvar,*data)
        self.chooseCategory_u_u.place(x=430,y=10)

        self.foodName=StringVar()
        

        self.getProductDetails_u_u=Button(self.deleteItemFrame,text="Get Items",command=self.delSelItem,font="arial 12 bold",bg="red",fg="white")
        self.getProductDetails_u_u.place(x=600,y=10)

    def delSelItem(self):
        categoryName=self.tkvar.get()

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="select id from foodCategories where categoryName='"+str(categoryName)+"'"
        self.cursor.execute(query)
        records=self.cursor.fetchone()
        id=records[0]


        query="select foodName from foodItems where categoryId='"+str(id)+"'"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        items=[]
        for row in records:
            items.append(row[0])

        self.deleteItemFrame_s=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.deleteItemFrame_s.place(x=15,y=130,width=1010,height=50)


        self.chooseCategoryLabel_u_u=Label(self.deleteItemFrame_s, text="Choose Item : ",pady=10,width=30,font="arial 15 bold",bg="#009688",fg="white")
        self.chooseCategoryLabel_u_u.place(x=100,y=0)
      

        self.chooseCategory_u_u=OptionMenu(self.deleteItemFrame_s,self.tkvar1,*items)
        self.chooseCategory_u_u.place(x=430,y=10)

        self.foodName=StringVar()
        

        self.getProductDetails_u_u=Button(self.deleteItemFrame_s,text="Delete Item",command=self.deleteItemDb,font="arial 12 bold",bg="red",fg="white")
        self.getProductDetails_u_u.place(x=600,y=5)

    def deleteItemDb(self):
        foodName=self.tkvar1.get()

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="delete from foodItems where foodName='"+str(foodName)+"'"
        self.cursor.execute(query)
        self.conn.commit()

        messagebox.showinfo("Success","Item delete Successfully")

        self.adminPanel()



    def addNewCategory(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1050,height=550)

        self.addNewCategoryFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.addNewCategoryFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.addNewCategoryFrame,text="Add New Category: ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.addCategory=StringVar()

        self.addNewCategoryFormFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="#009688")
        self.addNewCategoryFormFrame.place(x=15,y=80,width=1010,height=350)

        self.labelAddNC=Label(self.addNewCategoryFormFrame,text="Enter New Category : ",font="arial 15 bold",bg="#009688")
        self.labelAddNC.place(x=200,y=50)

        self.entryAddNC=Entry(self.addNewCategoryFormFrame,font="arial 15 bold",textvariable=self.addCategory,bd=3)
        self.entryAddNC.place(x=450,y=50)

        self.buttonAddNC=Button(self.addNewCategoryFormFrame,text="Add Category",font="arial 15 bold",bg="red",fg="white",command=self.confirmCategory)
        self.buttonAddNC.place(x=350,y=100)


    def confirmCategory(self):
        categoryName=self.addCategory.get()

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="insert into foodCategories(categoryName) values('"+categoryName+"')"
        self.cursor.execute(sql)

        messagebox.showinfo("success","Category Added Successful.")

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        self.adminPanel()


    def addNewItem(self):
        self.adminBottomFrame=Frame(self.adminPanelFrame,bd=2,bg="#e0e0e0")
        self.adminBottomFrame.place(x=0,y=110,width=1030,height=520)

        self.addNewItemLabelFrame=Frame(self.adminBottomFrame,bd=5,relief=RIDGE,bg="green")
        self.addNewItemLabelFrame.place(x=15,y=15,width=1010,height=50)

        self.labelAddNC=Label(self.addNewItemLabelFrame,text="Add New Item ",font="arial 18 bold",bg="green",fg="white")
        self.labelAddNC.place(x=400,y=2)

        self.addNewItemFrame=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.addNewItemFrame.place(x=15,y=75,width=1010,height=50)

        plateSize=["Quater","Half","Full"]

        self.tkvar = StringVar(self.root)
        self.tkvar1 = StringVar(self.root)
        
        self.tkvar.set("None")
        self.tkvar1.set("None")
    

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()
        
        self.chooseCategoryLabel_u_u=Label(self.addNewItemFrame, text="Choose Category : ",font="arial 15 bold",bg="#009688",fg="white")
        self.chooseCategoryLabel_u_u.place(x=100,y=5)

        query="select categoryName from foodCategories"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        data=[]
        for row in records:
            data.append(row[0])
        

        self.chooseCategory_u_u=OptionMenu(self.addNewItemFrame,self.tkvar,*data)
        self.chooseCategory_u_u.place(x=380,y=5)

        self.itemSize=OptionMenu(self.addNewItemFrame,self.tkvar1,*plateSize)
        self.itemSize.place(x=500,y=5)

        self.foodName=StringVar()
        

        self.getProductDetails_u_u=Button(self.addNewItemFrame,text="Get Item",command=self.addFoodItem,font="arial 12 bold",bg="red",fg="white")
        self.getProductDetails_u_u.place(x=600,y=5)

    def addFoodItem(self):
        self.addFoodItemFrame=Frame(self.adminBottomFrame,bd=2,relief=RIDGE,bg="#009688")
        self.addFoodItemFrame.place(x=15,y=130,width=1010,height=340)


        self.itemName=StringVar()
        self.quaterPlate=StringVar()
        self.halfPlate=StringVar()
        self.fullPlate=StringVar()

        if(self.tkvar1.get()=="Quater"):
            self.itemNameLabel=Label(self.addFoodItemFrame,text="Item Name : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemNameLabel.place(x=100,y=50)

            self.itemNameEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.itemName,font="arial 15 bold")
            self.itemNameEntry.place(x=350,y=60)

            self.quaterPlateLabel=Label(self.addFoodItemFrame,text="Quater Plate Price  : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.quaterPlateLabel.place(x=100,y=100)

            self.quaterPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.quaterPlate,font="arial 15 bold")
            self.quaterPlateEntry.place(x=350,y=110)

            self.itemHalfPlateLabel=Label(self.addFoodItemFrame,text="Half Plate Price : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemHalfPlateLabel.place(x=100,y=150)

            self.halfPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.halfPlate,font="arial 15 bold")
            self.halfPlateEntry.place(x=350,y=160)

            self.fullPlateLabel=Label(self.addFoodItemFrame,text="Full Plate Price  : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.fullPlateLabel.place(x=100,y=200)

            self.fullPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.fullPlate,font="arial 15 bold")
            self.fullPlateEntry.place(x=350,y=210)

            self.addItemBtn=Button(self.addFoodItemFrame,text="Add Item",font="arial 15 bold",command=self.submitFoodItem,bg="red",fg="white")
            self.addItemBtn.place(x=250,y=270)

        elif(self.tkvar1.get()=="Half"):
            self.itemNameLabel=Label(self.addFoodItemFrame,text="Item Name : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemNameLabel.place(x=100,y=50)

            self.itemNameEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.itemName,font="arial 15 bold")
            self.itemNameEntry.place(x=350,y=60)

            self.itemHalfPlateLabel=Label(self.addFoodItemFrame,text="Half Plate Price : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemHalfPlateLabel.place(x=100,y=100)

            self.halfPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.halfPlate,font="arial 15 bold")
            self.halfPlateEntry.place(x=350,y=110)

            self.fullPlateLabel=Label(self.addFoodItemFrame,text="Full Plate Price  : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.fullPlateLabel.place(x=100,y=150)

            self.fullPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.fullPlate,font="arial 15 bold")
            self.fullPlateEntry.place(x=350,y=160)

            self.addItemBtn=Button(self.addFoodItemFrame,text="Add Item",font="arial 15 bold",command=self.submitFoodItem,bg="red",fg="white")
            self.addItemBtn.place(x=250,y=220)

        elif(self.tkvar1.get()=="Full"):

            self.itemNameLabel=Label(self.addFoodItemFrame,text="Item Name : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemNameLabel.place(x=100,y=50)

            self.itemNameEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.itemName,font="arial 15 bold")
            self.itemNameEntry.place(x=350,y=60)

            self.itemHalfPlateLabel=Label(self.addFoodItemFrame,text="Item Price : ",padx=20,pady=10,font="arial 15 bold",bg="#009688")
            self.itemHalfPlateLabel.place(x=100,y=100)

            self.halfPlateEntry=Entry(self.addFoodItemFrame,width=40,textvariable=self.fullPlate,font="arial 15 bold")
            self.halfPlateEntry.place(x=350,y=110)

            self.addItemBtn=Button(self.addFoodItemFrame,text="Add Item",font="arial 15 bold",command=self.submitFoodItem,bg="red",fg="white")
            self.addItemBtn.place(x=250,y=170)


    def submitFoodItem(self):
        itemName=self.itemName.get()
        halfPlate=self.halfPlate.get()
        fullPlate=self.fullPlate.get()
        quaterPlate=self.quaterPlate.get()

        categoryName=self.tkvar.get()
        plateSize=self.tkvar1.get()

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="select id from foodCategories where categoryName='"+str(categoryName)+"'"
        self.cursor.execute(query)
        records=self.cursor.fetchone()
        categoryId=records[0]

        if(plateSize=="Quater"):
            sql="insert into foodItems(foodName,quaterPlatePrice,halfPlatePrice,fullPlatePrice,categoryId) values('"+str(itemName)+"','"+str(quaterPlate)+"','"+str(halfPlate)+"','"+str(fullPlate)+"','"+str(categoryId)+"')"
            self.cursor.execute(sql)
            self.conn.commit()
        elif(plateSize=="Half"):
            sql="insert into foodItems(foodName,quaterPlatePrice,halfPlatePrice,fullPlatePrice,categoryId) values('"+str(itemName)+"','0','"+str(halfPlate)+"','"+str(fullPlate)+"','"+str(categoryId)+"')"
            self.cursor.execute(sql)
            self.conn.commit()
        elif(plateSize=="Full"):
            sql="insert into foodItems(foodName,quaterPlatePrice,halfPlatePrice,fullPlatePrice,categoryId) values('"+str(itemName)+"','0','0','"+str(fullPlate)+"','"+str(categoryId)+"')"
            self.cursor.execute(sql)
            self.conn.commit()

        self.cursor.close()
        self.conn.close()

        messagebox.showinfo("success","Item Added Successfully")
        self.addFoodItem()


    def updateItem(self):
        self.newWin=Toplevel(self.root)
        self.newObj=UpdateItems.UpdateItems(self.newWin)
        self.root.withdraw()

    def totalTransaction(self):
        self.totalTransactionFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        self.totalTransactionFrame.place(x=303,y=103,height=590,width=1050)

        self.totalTransactionTopFrame=Frame(self.totalTransactionFrame,bd=2,relief=RIDGE,bg="#009688")
        self.totalTransactionTopFrame.place(x=10,y=10,width=1025,height=50)

        self.chooseHistoryLabel=Label(self.totalTransactionTopFrame, text="Choose  Date : ",pady=10,bg="#009688",fg="white",font="arial 15 bold")
        self.chooseHistoryLabel.place(x=200,y=0)

        self.cal = DateEntry(self.totalTransactionTopFrame,bg="darkblue",fg="brown",font="arial 15 bold", locale='en_US', date_pattern='y/mm/dd')
        self.cal.place(x=400,y=10)

        self.getProductDetails=Button(self.totalTransactionTopFrame,text="Get Transactions",command=self.getTransactionHistory,font="arial 14 bold")
        self.getProductDetails.place(x=600,y=4)

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()



        self.getAllDetails=Button(self.totalTransactionFrame,text="Get Details",command=self.getAllHistory,font="arial 15 bold",bg="red",bd=3,fg="white")
        self.getAllDetails.place(x=800,y=545,height=40,width=200)

        self.getTransactionHistory()

    def getTransactionHistory(self):
        self.transactionHistoryFrame=Frame(self.totalTransactionFrame,bd=2,relief=RIDGE,bg="white")
        self.transactionHistoryFrame.place(x=10,y=70,width=1025,height=470)

        total=0
        card=0
        cash=0
        dateChoosen=self.cal.get()

        query="select totalPrice from transactionHistory where dateTimeOfOrderDelivered like '%"+str(dateChoosen)+"%'"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        total=0
        for ttl in result:
            total=float(total)+float(ttl[0])


        query1="select totalPrice from transactionHistory where paymentMode='NetBanking' and dateTimeOfOrderDelivered like '%"+str(dateChoosen)+"%' or paymentMode='card' and dateTimeOfOrderDelivered like '%"+str(dateChoosen)+"%'"
        self.cursor.execute(query1)
        resultCard=self.cursor.fetchall()
        card=0
        for ttl in resultCard:
            card=float(card)+float(ttl[0])

        print(card)

        query2="select totalPrice from transactionHistory where dateTimeOfOrderDelivered like '%"+str(dateChoosen)+"%' and paymentMode='cash'"
        self.cursor.execute(query2)
        resultCash=self.cursor.fetchall()
        cash=0
        for ttl in resultCash:
            cash=float(cash)+float(ttl[0])


        self.totalTransactionLabel=Label(self.totalTransactionFrame,text="Total Transaction : "+"Rs "+str(total),font="arial 12 bold",bg="white",bd=3,fg="green")
        self.totalTransactionLabel.place(x=0,y=545,height=40,width=300)

        self.totalTransactionLabel=Label(self.totalTransactionFrame,text="By Cash : "+"Rs "+str(cash),font="arial 12 bold",bg="white",bd=3,fg="green")
        self.totalTransactionLabel.place(x=320,y=545,height=40,width=200)

        self.totalTransactionLabel=Label(self.totalTransactionFrame,text="By Card : "+"Rs "+str(card),font="arial 12 bold",bg="white",bd=3,fg="green")
        self.totalTransactionLabel.place(x=550,y=545,height=40,width=200)

           

        columns = ("ID","Order From", "Order Address","Order On","Deliver On","Total Price","Payment Mode")
        self.treeview = ttk.Treeview(self.transactionHistoryFrame, height=18, show="headings", columns=columns)

        self.treeview.column("ID", width=50, anchor='center')
        self.treeview.column("Order From", width=150, anchor='center')
        self.treeview.column("Order Address", width=350, anchor='center')
        self.treeview.column("Order On", width=100, anchor='center')
        self.treeview.column("Deliver On", width=100, anchor='center')
        self.treeview.column("Total Price", width=130, anchor='center')
        self.treeview.column("Payment Mode", width=130, anchor='center')
 
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Order From", text="Order From")
        self.treeview.heading("Order Address", text="Order Address")
        self.treeview.heading("Order On", text="Order On")
        self.treeview.heading("Deliver On", text="Deliver On") 
        self.treeview.heading("Total Price", text="Total Price")
        self.treeview.heading("Payment Mode", text="Payment Mode")

        self.treeview.bind('<Button-1>', self.getAllHistory)
 
        self.treeview.place(x=0,y=0,width=1023,height=467)

        # database programming started from there...

        choosenDate=self.cal.get()
   

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="select orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,id,paymentMode from transactionHistory where dateTimeOfOrderDelivered like '%"+str(choosenDate)+"%'"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        self.treeview.focus_set()
        for row in records:
            onOrder=row[3]
            onDelevered=row[4]
            self.treeview.insert(parent='', index=0, text='', values=(row[6],row[0],str(row[2]),onOrder[11:19],onDelevered[11:19],"Rs "+row[5],row[7]))
            children = self.treeview.get_children()
            if children:
                self.treeview.focus(children[0])
                self.treeview.selection_set(children[0])


    def getAllHistory(self):
        curItem = self.treeview.focus()
        values=self.treeview.item(curItem)["values"]
        id=values[0]

        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="select productItems from transactionHistory where id='"+str(id)+"'"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
       

        buyProducts="Product \t Quantity \t Price \n"+records[0][0]

        messagebox.showinfo("History",buyProducts)


    def packingViewItems(self):
        curItem = self.treeview_packing.focus()
        values=self.treeview_packing.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item  X  Quantity =  Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def allOrdersViewItems(self):
        curItem = self.treeview_allOrders.focus()
        values=self.treeview_allOrders.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item  X  Quantity =  Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()
    
    def zomatoViewItems(self):
        curItem = self.treeview_zomato.focus()
        values=self.treeview_zomato.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item  X  Quantity =  Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def swiggiViewItems(self):
        curItem = self.treeview_swiggi.focus()
        values=self.treeview_swiggi.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item  X  Quantity =  Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def homeDeliveryViewItems(self):
        curItem = self.treeview_homeDelivery.focus()
        values=self.treeview_homeDelivery.item(curItem)["values"]
        if(values==""):
            messagebox.showerror("Error","No items in pending")
        else:
            id=values[0]

            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql="select productItems from pendingOrders where orderId='"+str(id)+"'"
            self.cursor.execute(sql)
            result=self.cursor.fetchone()

            label="Item  X  Quantity =  Price \n"
            string=str(label)+str(result[0])
            
            messagebox.showinfo("User Buy Products",string)

            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            


if __name__=="__main__":
    root=Tk()
    obj=MagicRestaurent(root)
    root.mainloop()