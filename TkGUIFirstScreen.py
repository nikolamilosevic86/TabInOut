'''
Created on 1 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
top = Tk()
top.title("Table InfExtractor")
top.geometry('{}x{}'.format(500, 500))
# Code to add widgets will go here...
topframe = Frame(top,height=10)
topframe.pack()
frame = Frame(top)
frame.pack()
topframe2 = Frame(top,height=10)
topframe2.pack()

middleframe = Frame(top)
middleframe.pack()
bottomframe2 = Frame(top,height=10)
bottomframe2.pack( side = BOTTOM )
bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

name = StringVar()
label_name = Label(frame,textvariable=name)
name.set("Name of task:")
label_name.pack(side = LEFT)
E1 = Entry(frame, bd =5)
E1.pack(side = LEFT)
ConfigureDB = Button(frame, text="Configure Database", fg="black")
ConfigureDB.pack( side = LEFT)
clearTable = Button(frame, text="Clear DB Table", fg="black")
clearTable.pack( side = LEFT)

Lb1 = Listbox(middleframe,width=80,height=20)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()



AddRule = Button(bottomframe, text="Add Rule", fg="black")
AddRule.pack( side = LEFT)
DeleteRule = Button(bottomframe, text="Delete Rule", fg="black")
DeleteRule.pack( side = LEFT)
EditRule = Button(bottomframe, text="Edit Rule", fg="black")
EditRule.pack( side = LEFT)
MoveUpRule = Button(bottomframe, text="Move Up Rule", fg="black")
MoveUpRule.pack( side = LEFT)
MoveDownRule = Button(bottomframe, text="Move Down Rule", fg="black")
MoveDownRule.pack( side = LEFT)
Next = Button(bottomframe, text="Next", bg="green")
Next.pack( side = LEFT)


top.mainloop()