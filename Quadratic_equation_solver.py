from tkinter import *
from math import *
#used to calculate the roosts of the equation
def value_1():    
    a=int(a3.get())
    b=int(b3.get())
    c=int(c3.get())
    if a==0:       #if quotient of x^2 is 0 then it is a linear equation
        ro1= str(-c/b)
        return ro1
    else:
        if b*b < 4*a*c :       #for complex roots
            ro1=str(-b/2)+"+j"+str(sqrt(-(b*b)+(4*a*c))/2)
            ro2=str(-b/2)+"+-j"+str(sqrt(-(b*b)+(4*a*c))/2)
        else:
            ro1= str((-b+(sqrt((b*b)-(4*a*c))))/2)
            ro2= str((-b-(sqrt((b*b)-(4*a*c))))/2)
    return ro1+", "+ro2
#to display the roots of the equation
def display():    
    l=value_1()
    Label(window,text="The root(s) of the equation are: ",bg="blue",font="Helvetica 12",bd=0).place(x=0,y=225)
    output.delete("0.0","end")
    output.insert("0.0",l)
        
#create the tkinter screen and styling the screen   
window=Tk()
window.configure(bg="blue")
window.title("Quadratic equation")
window.geometry("500x400")
Label(window,text="Quadratic equation solver",bg="blue",fg="white",font="Arial 20").place(x=50,y=0)
Label(window,text="(enter the quotients of the quadratic equation)",bg="blue",fg="white",font="Helvetica 10").place(x=0,y=40)
Label(window,text="Value of a",bg="blue",fg="white",font=10).place(x=75,y=65)
Label(window,text="value of b",bg="blue",fg="white",font=10).place(x=75,y=110)
Label(window,text="value of c",bg="blue",fg="white",font=10).place(x=75,y=155)
a3=StringVar()
b3=StringVar()
c3=StringVar()
Entry(window,textvariable=a3).place(x=155,y=65)
Entry(window,textvariable=b3).place(x=155,y=110)
Entry(window,textvariable=c3).place(x=155,y=155)
ook = Button(window,text="Calculate",bg="pink",command=display).place(x=135,y=200)
output = Text(window, bg="blue", font="Helvetica 12",bd=0, width=100, height=1)
output.place(x=0,y=270)
window.mainloop()
