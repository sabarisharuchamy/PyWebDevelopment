from tkinter import *
top=Tk()
top.geometry('600x200')
CheckVar1=IntVar()
CheckVar2=IntVar()
C1=Checkbutton
C1=Checkbutton(top,text="Pizza",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C2=Checkbutton(top,text="Fries",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C1.pack()
C2.pack()
def helloCallBack():
    Label(top, text = CheckVar1.get()).place(x = 30,y = 50)
    Label(top, text = CheckVar2.get()).place(x = 30, y = 90)
B=Button(top,text="Initiate",command=helloCallBack)
B.place(x=200,y=100)

