from tkinter import *
from Database_files import Connection

class PurchasingItems:
    def __init__(self,root):
        self.root=root
        

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        

        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        sql="select productItems from pendingOrders where orderId='580'"
        self.cursor.execute(sql)
        result=self.cursor.fetchone()

        label="Item \t  X \t  Quantity = \t Price \n"
        string=str(label)+str(result[0])
        
        label=Label(self.root,text=string)
        label.place(x=0,y=10,width=300,height=50)
        

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        


        






if __name__=="__main__":
    root=Tk()
    obj=PurchasingItems(root)
    root.mainloop()