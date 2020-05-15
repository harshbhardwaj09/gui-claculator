from tkinter import *
from tkinter.messagebox import *
from PIL import Image , ImageTk
root=Tk()
root.geometry("500x500")
root.maxsize(600,600)
root.minsize(250,250)
root.title("claculator")
root.iconbitmap("iconcal.ico")


#background
d=Image.open("call.jpg")
bgimg=ImageTk.PhotoImage(d)
bgg=Label(root,image=bgimg)
bgg.place(x=0,y=0,relwidth=1, relheight=1)


def click(event):
    global scvalue
    b=event.widget.cget("text")
    if b=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    elif b=="C":
        scvalue.set("")
        screen.update()
        pass

    else:
        scvalue.set(scvalue.get()+b)


#functions for menu

#file
def new():
    scvalue.set("")
    screen.update()

def quit():
    c=askquestion("Exit","Do you really want to exit?")
    if c=="yes":
        exit()
    else:
        pass

#edit
def cut():
    screen.event_generate(("<<Cut>>"))

def copy():
    screen.event_generate(("<<Copy>>"))


def paste():
    screen.event_generate(("<<Paste>>"))


#other
def about():
    showinfo("About","Created by Harsh Bhardwaj..\n E-mail-bhardwajh39@gmail.com")


def help():
    showinfo("Help", "You can mail us your problem..\n E-mail-bhardwajh39@gmail.com\nwe will contact you")


#menu
mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label="New Calculation",command=new)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=filemenu)

editmenu=Menu(mainmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
mainmenu.add_cascade(label="Edit",menu=editmenu)

mainmenu.add_command(label="About us",command=about)
mainmenu.add_command(label="Help",command=help)

#for value
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,bg="#aedb9f",textvar=scvalue,font="lucida 40 ")
screen.pack(side="top",ipadx=5,ipady=5,padx=5)

f1=Frame(root,pady=7)
b=Button(f1,text="9",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f1,text="8",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f1,text="7",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f1,text="//",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)


f1.pack()

f2=Frame(root,pady=6)
b=Button(f2,text="6",bg="#aedb9f")

b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f2,text="5",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f2,text="4",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f2,text="*",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)


f2.pack()

f3=Frame(root,pady=7)
b=Button(f3,text="3",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f3,text="2",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f3,text="1",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f3,text="-",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

f3.pack()

f4=Frame(root,pady=7)
b=Button(f4,text="0",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f4,text=".",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f4,text="C",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f4,text="+",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)


f4.pack()

f5=Frame(root,pady=7)
b=Button(f5,text="%",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

b=Button(f5,text="=",bg="#aedb9f")
b.config(height=4, width=13)
b.pack(padx=9,side="left")
b.bind("<Button-1>",click)

f5.pack()

root.mainloop()