###Empty window
##import tkinter
##top = tkinter.Tk()
##top.mainloop()

###Button
##from tkinter import *
##top=Tk()
##top.geometry('600x200')
##from tkinter import messagebox
##def helloCallBack():
##    messagebox.showinfo("Hello, User","Hello, Guest")
##def helloCallBack2():
##    messagebox.showinfo("Hello, User","Hello, Guest")
##B=Button(top,text="Initiate",command=helloCallBack)
##B.place(x=300,y=100)
##C=Button(top,text="Initiate2",command=helloCallBack2)
##C.place(x=400,y=100)

###Canvas
##from tkinter import *
##top=Tk()
##C=Canvas(top,bg="magenta",height=300,width=400)
##coord=60,150,200,350
##arc=C.create_arc(coord,start=0,extent=97,fill='yellow')
##line=C.create_line(10,10,80,70,fill='green')
##C.pack()

#Checkbutton
from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry('600x200')
top.configure(background='magenta')
CheckVar1=IntVar()
CheckVar2=IntVar()
C1=Checkbutton(top,text="Pizza",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C2=Checkbutton(top,text="Fries",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C1.pack()
C2.pack()
def totalBill():
    total = 0
    if CheckVar1.get() == 1:
        total += 200
    if CheckVar2.get() == 1:
        total += 100
    messagebox.showinfo("Bill Details:","Total Amount to be paid: "+str(total))
B = Button(top,text="Print Bill",command = totalBill)
B.place(x=300,y=150)

###Entry
##from tkinter import *
##top=Tk()
##top.geometry('600x500')
##L1=Label(top,text="Enter Employee Name")
##L1.place(x=150,y=50)
##E1=Entry(top,bd=3)
##E1.place(x=310,y=50)
##L2=Label(top,text="Enter Employee Designation")
##L2.place(x=150,y=75)
##E2=Entry(top,bd=3)
##E2.place(x=310,y=75)
##L3=Label(top,text="Enter Employee Salary")
##L3.place(x=150,y=100)
##E3=Entry(top,bd=3)
##E3.place(x=310,y=100)
##def dispDetails():
##    L4=Label(top,text="Employee Details Saved:\n"+"Employee Name:\t\t"+E1.get()+"\nEmployee Designation: "+E2.get()+"\nEmployee Salary:\t\t"+E3.get())
##    L4.place(x=200,y=180)
##B = Button(top,text="Save",command = dispDetails)
##B.place(x=300,y=150)

###Frame
##from tkinter import *
##top=Tk()
##top.geometry('350x200')
##frame=Frame(top)
##frame.pack()
##frametwo=Frame(top)
##frametwo.pack(side=BOTTOM)
##redbutton=Button(frame,text="One",fg="red")
##redbutton.pack(side=LEFT)
##bluebutton=Button(frame,text="Two",fg="blue")
##bluebutton.pack(side=LEFT)
##greenbutton=Button(frametwo,text="Three",fg="green")
##greenbutton.pack(side=BOTTOM)
