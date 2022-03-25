from tkinter import *
from PIL import ImageTk,Image


class Quantity:
    def __init__(self,root):
        self.root=root
        self.root.title("select Quantity")
        self.root.geometry("400x200+400+300")
        self.root.resizable(False,False)
        self.root.focus_force()

        self.half=StringVar()

        self.itemFrame=Frame(self.root,bd=3)
        self.itemFrame.place(x=0,y=0,height=100,width=150)

        self.foodTitleLabel=Label(self.itemFrame,text="tandoori roti",font="arial 15 bold")
        self.foodTitleLabel.place(x=0,y=0,height=15,width=150)


        self.radioHalf=Radiobutton(self.itemFrame,text="Half: "+str(100)+" X ",variable=self.half,value="halfPlate")
        self.radioHalf.place(x=0,y=20,width=100,height=15)

        self.qtyEntry1=Entry(self.itemFrame)
        self.qtyEntry1.place(x=105,y=20,width=20,height=15)

        self.radiofull=Radiobutton(self.itemFrame,text="Full: "+str(200)+" X ",variable=self.half,value="fullPlate")
        self.radiofull.place(x=0,y=40,width=100,height=15)

        self.qtyEntry2=Entry(self.itemFrame)
        self.qtyEntry2.place(x=105,y=40,width=20,height=15)

        self.uttn=Button(self.itemFrame,text="add to cart",font="arial 10 bold")
        self.uttn.place(x=0,y=60,height=20,width=150)





        







if __name__=="__main__":
    root=Tk()
    qty=Quantity(root)
    root.mainloop()