from tkinter import *
from tkinter import messagebox
from Database_files import Connection
import datetime
import os
import tempfile
from PIL import ImageTk,Image
import deshboard

class PaymentAndBill:
    def __init__(self,root,id=0):
        self.root=root
        self.root.title("Payment And Print Bill ")
        self.root.geometry("1100x600+150+50")
        self.root.resizable(False,False)
        self.root.config(bg="gray")
        self.root.focus_force()

        self.id=id
        self.total=0

################# Left Main Frame ##########################

        self.leftFrame=Frame(self.root,bd=5)
        self.leftFrame.place(x=0,y=0,width=750,height=600)

        self.icon_title=Image.open("images/back1.png")
        self.icon_title=self.icon_title.resize((40,30),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)

        leftFrameTitle=Button(self.leftFrame,image=self.icon_title,font="arial 20 bold",borderwidth=0,bg="blue",command=self.homePage)
        leftFrameTitle.place(x=0,y=0,width=60,height=50)
        
        leftFrameTitle=Label(self.leftFrame,text="Select Payment Mode",font="arial 20 bold",padx=5,pady=5,bg="blue",fg="white")
        leftFrameTitle.place(x=60,y=0,width=680,height=50)

        self.leftTopFrame=Frame(self.root,bd=2,relief=GROOVE,bg="#d4d4d4")
        self.leftTopFrame.place(x=5,y=60,width=740,height=535)

        self.radio=IntVar()

        self.paymentFrame=Frame(self.leftTopFrame,bg="#d4d4d4",relief=GROOVE,bd=2)
        self.paymentFrame.place(x=5,y=5,width=727,height=180)
      

        self.byCard=Radiobutton(self.paymentFrame,text="By Debit/Credit Card",cursor="hand2",value=1,bg="#d4d4d4",variable=self.radio,padx=30,font="arial 13 bold",pady=10,bd=2)
        self.byCard.place(x=70,y=30)
        

        self.byCash=Radiobutton(self.paymentFrame,text="By Cash",padx=30,cursor="hand2",bg="#d4d4d4",font="arial 13 bold",value=2,variable=self.radio,pady=10,bd=2)
        self.byCash.place(x=300,y=30)

        self.byNetBanking=Radiobutton(self.paymentFrame,text="By NetBanking",cursor="hand2",bg="#d4d4d4",padx=30,font="arial 13 bold",value=3,variable=self.radio,pady=10,bd=2)
        self.byNetBanking.place(x=420,y=30)
        

        self.pay=Button(self.paymentFrame,text="Generate Bill",bd=3,padx=30,cursor="hand2",bg="red",font="arial 15 bold",fg="white",pady=5,command=self.generateBill)
        self.pay.place(x=250,y=100)

        ################### Right Main Frame #####################

        rightFrame=Frame(self.root,bg="#d4d4d4",relief=GROOVE,bd=2)
        rightFrame.place(x=750,y=0,width=350,height=600)

        title=Label(rightFrame,text="Billing",font="sans-serif 15 bold",bg="blue",fg="white",bd=4)
        title.place(x=0,y=0,height=50,width=340)

        self.billArea=Text(rightFrame,bd=5,font="arial 13 bold")
        self.billArea.place(x=0,y=55,width=335,height=485)

        printBtn=Button(rightFrame,text="Print Bill",font="sans-serif 15 bold",bg="red",fg="white",bd=5,cursor="hand2",command=self.closeOrder)
        printBtn.place(x=0,y=545,height=45,width=340)

    def homePage(self):
        self.newWin=Toplevel(self.root)
        self.newObj=deshboard.MagicRestaurent(self.newWin)
        self.root.withdraw()

    def generateBill(self):

        #################################
        
        orderAddress=""
        dateTime=""
        totalPrice=""
        productItems=""

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select orderAddress,dateTime,totalPrice,productItems,orderFrom from pendingOrders where orderId='"+str(self.id)+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            orderAddress=row[0]
            dateTime=row[1]
            totalPrice=row[2]
            productItems=row[3]
            orderFrom=row[4]


        cgst=0
        sgst=0
        discount=0
        self.total=totalPrice
        sql11="select CGST,SGST,Discount from additionalTaxes"
        self.cursor.execute(sql11)
        result11=self.cursor.fetchall()
        for row in result11:
            cgst=row[0]
            sgst=row[1]
            discount=row[2]
            
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        ###########  Calcutationg additional taxes ################

        ttl_cgst=float(cgst)*float(totalPrice)/float(100)
        ttl_sgst=float(sgst)*float(totalPrice)/100
        ttl_discount=float(totalPrice)*float(discount)/100
        ttl=round(float(totalPrice)-float(ttl_discount)+float(ttl_sgst)+float(ttl_cgst),3)
        self.g_total=round(float(ttl),3)

        ##################################################

        self.paymentBillFrame=Frame(self.leftTopFrame,bg="#d4d4d4",relief=GROOVE,bd=2)
        self.paymentBillFrame.place(x=5,y=190,width=727,height=330)

        if self.radio.get()==1:
            self.payment_mode="card"
            
            self.payedAmountLabel=Label(self.paymentBillFrame,text="Total :- "+u"\u20B9 "+str(self.g_total)+"/-",padx=30,font="arial 25 bold",pady=10)
            self.payedAmountLabel.place(x=200,y=100)
                        

        elif self.radio.get()==2:
            self.payment_mode="cash"

            self.payAmount=StringVar()

            self.payedAmountLabel=Label(self.paymentBillFrame,text=" Payed Amount: ",padx=30,font="arial 15 bold",pady=10,bg="#d4d4d4")
            self.payedAmountLabel.place(x=20,y=100)
            

            self.payedAmountEntry=Entry(self.paymentBillFrame,textvariable=self.payAmount,bd=2,width=25,font="arial 15 bold")
            self.payedAmountEntry.place(x=250,y=110)        

            
            self.totalAmount=Button(self.paymentBillFrame,text="Total Bill",padx=30,bd=3,font="arial 15 bold",command=self.totalPayReturn,cursor="hand2",compound=LEFT,anchor="w",bg="red",fg="white")
            self.totalAmount.place(x=300,y=160)
            

        elif self.radio.get()==3:
            self.payment_mode="NetBanking"

            self.payedAmountLabel=Label(self.paymentBillFrame,text="Total :- "+u"\u20B9 "+str(self.g_total)+"/-",padx=30,font="arial 25 bold",pady=10)
            self.payedAmountLabel.place(x=200,y=100)
            
            

        else:
            messagebox.showerror("error","select a payment mode first")




#############################################################
        dsh="\n___________________"
        address="\nNear Ujala Hospital \n\tKusumkhera"
        mob_email="\nMob :- 9988776655"
        orderFrom="\nOdr by : "+str(orderFrom)
        tableorder="\n"+str(orderAddress)
        dateTime=str(dateTime)
        orderItemstitle="\nitem    qty    Price"
        items=str(productItems)+" \n"
        bill="\nTotal :  Rs "+str(totalPrice)+"\n"
        l_cgst="\nCGST : "+ str(cgst) +"%  Rs "+str(ttl_cgst)
        l_sgst="\nSGST : "+ str(sgst) +"%  Rs "+str(ttl_sgst)
        l_discount="\nDiscount : "+ str(discount) +"%  Rs -"+str(ttl_discount)
        l_Gt="\nGROSS TOTAL : Rs "+str(self.g_total)
        modePayment="\nPayment Mode : "+str(self.payment_mode)
        
        thankUmsg="\n\nHave a nice day ahead."



        self.cpt_bill=dsh+address+mob_email+dsh+orderFrom+tableorder+dsh+modePayment+dsh+orderItemstitle+items+dsh+bill+l_cgst+l_sgst+l_discount+dsh+l_Gt+thankUmsg

        self.billArea.delete(1.0, 'end')
        self.billArea.tag_configure("center", justify='center')
        self.billArea.insert(INSERT,self.cpt_bill)
        self.billArea.tag_add("center", "1.0", "end")
        


        
        

    def totalPayReturn(self):
        amount=self.payAmount.get()
        totalPayble=float(amount)-float(self.g_total)

        self.totalPaybleAmount=Label(self.paymentBillFrame,text="Return Amount :- "+u"\u20B9 "+str(totalPayble)+"/-",bd=3,padx=30,font="arial 25 bold",pady=10)
        self.totalPaybleAmount.place(x=150,y=250)


    def closeOrder(self):
        if self.total==0:
            messagebox.showerror("Error","Select Payment Mode First")
        else:
            self.db=Connection()
            self.conn=self.db.getConnection()
            self.cursor=self.db.getCursor()

            sql1="select orderAddress,productItems,orderFrom,dateTime,totalPrice from pendingOrders where orderId='"+str(self.id)+"'"
            self.cursor.execute(sql1)
            res=self.cursor.fetchone()
            orderAddress=res[0]
            productItems=res[1]
            orderFrom=res[2]
            dateTimeOfOrder=res[3]

            now = datetime.datetime.now()
            dateTimeOfDelivered=now.strftime("%Y/%m/%d %H:%M:%S")
            totalPrice=res[4]

            if(orderFrom=="Table"):
                tableNo=int(orderAddress[9:])

                sql2="update tablesData set tableStatus=0 where tableNo='"+str(tableNo)+"'"
                self.cursor.execute(sql2)
                self.conn.commit()

                sql_1="insert into transactionHistory(orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,paymentMode) values('"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTimeOfOrder)+"','"+str(dateTimeOfDelivered)+"','"+str(totalPrice)+"','"+str(self.payment_mode)+"')"
                self.cursor.execute(sql_1)
                self.conn.commit()

                sql="delete from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()
            

            if(orderFrom=="zomato"):
                sql_1="insert into transactionHistory(orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,paymentMode) values('"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTimeOfOrder)+"','"+str(dateTimeOfDelivered)+"','"+str(totalPrice)+"','"+str(self.payment_mode)+"')"
                self.cursor.execute(sql_1)
                self.conn.commit()

                sql="delete from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()
                

            if(orderFrom=="swiggi"):
                sql_1="insert into transactionHistory(orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,paymentMode) values('"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTimeOfOrder)+"','"+str(dateTimeOfDelivered)+"','"+str(totalPrice)+"','"+str(self.payment_mode)+"')"
                self.cursor.execute(sql_1)
                self.conn.commit()

                sql="delete from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()

            if(orderFrom=="homeDelivery"):
                sql_1="insert into transactionHistory(orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,paymentMode) values('"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTimeOfOrder)+"','"+str(dateTimeOfDelivered)+"','"+str(totalPrice)+"','"+str(self.payment_mode)+"')"
                self.cursor.execute(sql_1)
                self.conn.commit()

                sql="delete from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()

            if(orderFrom=="Packing"):
                sql_1="insert into transactionHistory(orderFrom,productItems,orderAddress,dateTimeOfOrderPlaced,dateTimeOfOrderDelivered,totalPrice,paymentMode) values('"+str(orderFrom)+"','"+str(productItems)+"','"+str(orderAddress)+"','"+str(dateTimeOfOrder)+"','"+str(dateTimeOfDelivered)+"','"+str(totalPrice)+"','"+str(self.payment_mode)+"')"
                self.cursor.execute(sql_1)
                self.conn.commit()

                sql="delete from pendingOrders where orderId='"+str(self.id)+"'"
                self.cursor.execute(sql)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()

            

            
        #########################################

            fileName=tempfile.mktemp(".txt")
            open(fileName,"w").write(self.cpt_bill)
            os.startfile(fileName,"print")



        #############################


            messagebox.showinfo("success","Order Successfull")
            self.homePage()
            self.root.withdraw()
            


if __name__=="__main__":
    root=Tk()

    obj=PaymentAndBill(root)

    root.mainloop()