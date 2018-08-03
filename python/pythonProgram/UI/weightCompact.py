from tkinter import *

window = Tk()

def km_to_miles():
    if b1.text ==
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)

    pound=float(e1_value.get())*2.20462
    t2.insert(END,pound)

    ounce=float(e1_value.get())*35.274
    t3.insert(END,ounce)

l0=Label(window,text="KG")
l0.grid(row=0,column=0)

b1=Button(window,text="Grams", command=km_to_miles)
b1.grid(row=0,column=2)

b2=Button(window,text="Pounds", command=km_to_miles)
b2.grid(row=0,column=3)

b3=Button(window,text="Ounces", command=km_to_miles)
b3.grid(row=0,column=4)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

l1=Label(window,text="Grams")
l1.grid(row=2,column=1)


window.mainloop()
