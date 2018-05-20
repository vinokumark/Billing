from tkinter import *

list=[]
def add():
    data=Lb.get(ACTIVE)
    if data=='Pen              10/-':
        tb.insert(END,'\nPen\t10/- x %d'%(qnt.get()))
        list.append(10*qnt.get())
        
    elif data=='Pencil          5/-':
        tb.insert(END,'\nPencil\t5/- x %d'%(qnt.get()))
        list.append(5*qnt.get())

    elif data=='Eraser          10/-':
        tb.insert(END,'\nEraser\t10/- x %d'%(qnt.get()))
        list.append(10*qnt.get())

    elif data=='Sharpner     15/-':
        tb.insert(END,'\nSharpner\t15/- x %d'%(qnt.get()))
        list.append(15*qnt.get())


def total():
    messagebox.showinfo("Hello %s"%(nameinfo.get()),"Amount to be paid: Rs. %d/-"%(sum(list)))

def clr():
    tb.delete(1.0,END)
    list.clear()
    
f=Tk()
f.title("Billing")

nameinfo=StringVar()
data=IntVar()
qnt=IntVar()


name=Label(f,text='Name :')
e1=Entry(f,width=15,bd=3,textvariable=nameinfo)

prod=Label(f,text='Products :',bd=3)
Lb=Listbox(f,height=6,width=15,bd=3)
Lb.insert(0,'Items          Price\n')
Lb.insert(1,'')
Lb.insert(2,'Pen              10/-')
Lb.insert(3,'Pencil          5/-')
Lb.insert(4,'Eraser          10/-')
Lb.insert(5,'Sharpner     15/-')

quan=Label(f,text='Quantity :')
e2=Entry(f,width=15,bd=3,textvariable=qnt)

b1=Button(f,text='Add Items',width=12,bd=3,command=add)

tb=Text(f,height=5,width=20,bd=3)

b3=Button(f,text='Clear Items',width=12,bd=3,command=clr)

b2=Button(f,text='Total',width=12,bd=3,command=total)

name.grid(row=0,column=0,padx=5,pady=5)
e1.grid(row=0,column=1,padx=5,pady=5)
prod.grid(row=1,column=0,padx=5,pady=5)
Lb.grid(row=1,column=1,padx=5,pady=5)
quan.grid(row=2,column=0,padx=5,pady=5)
e2.grid(row=2,column=1,padx=5,pady=5)
b1.grid(row=3,column=1,padx=5,pady=5)
tb.grid(row=4,columnspan=2,padx=5,pady=5)
b3.grid(row=5,column=0,padx=5,pady=5)
b2.grid(row=5,column=1,padx=5,pady=5)

f.mainloop()