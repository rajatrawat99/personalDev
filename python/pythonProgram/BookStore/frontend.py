"""
Create a program for book store with following options:

view all records
update
delete
search
"""
from tkinter import *
import backend


window = Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

Title_text=StringVar()
e1=Entry(window,textvariable=Title_text)
e1.grid(row=0,column=1)

Author_text=StringVar()
e2=Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)

Year_text=StringVar()
e3=Entry(window,textvariable=Year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all",width=12)
b1.grid(row=2,column=3)

b1=Button(window,text="Search",width=12)
b1.grid(row=3,column=3)

b1=Button(window,text="Add",width=12)
b1.grid(row=4,column=3)

b1=Button(window,text="Update",width=12)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete",width=12)
b1.grid(row=6,column=3)

b1=Button(window,text="Close",width=12)
b1.grid(row=7,column=3)


window.mainloop()
