import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.title("calculator")
root.geometry("250x400+300+200")
root.resizable(0,0)

val=""
A=0
operator=""

def btn_1_clicked():
    global val
    val=val +"1"
    data.set(val)

def btn_2_clicked():
    global val
    val=val +"2"
    data.set(val)

def btn_3_clicked():
    global val
    val=val +"3"
    data.set(val)

def btn_4_clicked():
    global val
    val=val +"4"
    data.set(val)

def btn_5_clicked():
    global val
    val=val +"5"
    data.set(val)

def btn_6_clicked():
    global val
    val=val +"6"
    data.set(val)

def btn_7_clicked():
    global val
    val=val +"7"
    data.set(val)

def btn_8_clicked():
    global val
    val=val +"8"
    data.set(val)

def btn_9_clicked():
    global val
    val=val +"9"
    data.set(val)

def btn_0_clicked():
    global val
    val=val +"0"
    data.set(val)

def btn_plus_clicked():
    global  A
    global  val
    global  operator
    A=int(val)
    operator="+"
    val=val +"+"
    data.set(val)

def btn_minus_clicked():
    global  A
    global  val
    global  operator
    A=int(val)
    operator="-"
    val=val +"-"
    data.set(val)

def btn_mul_clicked():
    global  A
    global  val
    global  operator
    A=int(val)
    operator="*"
    val=val +"*"
    data.set(val)

def btn_div_clicked():
    global  A
    global  val
    global  operator
    A=int(val)
    operator="/"
    val=val +"/"
    data.set(val)

def clean_cleaked():
    global A
    global val
    global operator
    A=0
    val=""
    operator=""
    data.set(val)


def result():
    global A
    global val
    global operator
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        c=x+A
        data.set(c)
        val=str(c)
    elif operator=="-":
        x = int((val2.split("-")[1]))
        c = x - A
        data.set(c)
        val = str(c)
    elif operator=="*":
        x = int((val2.split("*")[1]))
        c = x * A
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))

        if x==0:
            messagebox.showerror("error","invaid number")
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)



data=StringVar()
lbl=Label(root,text="label",anchor=SE,font=("verdana",20),textvariable=data,background="#ffffff",fg="#000000")
lbl.pack(expand=True,fill="both")

btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=True,fill="both")


btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root,)
btnrow4.pack(expand=True,fill="both")

btn1=Button(btnrow1,text="1",font=("verdana",22,),border=0,relief=GROOVE,command=btn_1_clicked)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(btnrow1,text="2",font=("verdana",22),border=0,relief=GROOVE,command=btn_2_clicked)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(btnrow1,text="3",font=("verdana",22),border=0,relief=GROOVE,command=btn_3_clicked)
btn3.pack(side=LEFT,expand=True,fill="both")
btnplus=Button(btnrow1,text="+",font=("verdana",22),border=0,relief=GROOVE,command=btn_plus_clicked)
btnplus.pack(side=LEFT,expand=True,fill="both")


btn4=Button(btnrow2,text="4",font=("verdana",22),border=0,relief=GROOVE,command=btn_4_clicked)
btn4.pack(side=LEFT,expand=True,fill="both")
btn5=Button(btnrow2,text="5",font=("verdana",22),border=0,relief=GROOVE,command=btn_5_clicked)
btn5.pack(side=LEFT,expand=True,fill="both")
btn6=Button(btnrow2,text="6",font=("verdana",22),border=0,relief=GROOVE,command=btn_6_clicked)
btn6.pack(side=LEFT,expand=True,fill="both")
btnminus=Button(btnrow2,text="-",font=("verdana",22),border=0,relief=GROOVE,command=btn_minus_clicked)
btnminus.pack(side=LEFT,expand=True,fill="both")


btn7=Button(btnrow3,text="7",font=("verdana",22),border=0,relief=GROOVE,command=btn_7_clicked)
btn7.pack(side=LEFT,expand=True,fill="both")
btn8=Button(btnrow3,text="8",font=("verdana",22),border=0,relief=GROOVE,command=btn_8_clicked)
btn8.pack(side=LEFT,expand=True,fill="both")
btn9=Button(btnrow3,text="9",font=("verdana",22),border=0,relief=GROOVE,command=btn_9_clicked)
btn9.pack(side=LEFT,expand=True,fill="both")
btnmul=Button(btnrow3,text="*",font=("verdana",22),border=0,relief=GROOVE,command=btn_mul_clicked)
btnmul.pack(side=LEFT,expand=True,fill="both")


btnclean=Button(btnrow4,text="C",font=("verdana",22),border=0,relief=GROOVE,command=clean_cleaked)
btnclean.pack(side=LEFT,expand=True,fill="both")
btn0=Button(btnrow4,text="0",font=("verdana",22),border=0,relief=GROOVE,command=btn_0_clicked)
btn0.pack(side=LEFT,expand=True,fill="both")
btnequal=Button(btnrow4,text="=",font=("verdana",22),border=0,relief=GROOVE,command=result)
btnequal.pack(side=LEFT,expand=True,fill="both")
btndiv=Button(btnrow4,text="/",font=("verdana",22),border=0,relief=GROOVE,command=btn_div_clicked)
btndiv.pack(side=LEFT,expand=True,fill="both")

root.mainloop()