'''
Created on 1 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import tkMessageBox
import FileManipulationHelper
Lb1 = None
Lb3 = None   

def RemoveRule():
    try:
        # get selected line index
        index = Lb1.curselection()[0]
        Lb1.delete(index)
    except IndexError:
        pass

def MoveRuleUp():
    try:
        pos = Lb1.curselection()[0]
        # get selected line index
        if pos == 0:
            return

        text = Lb1.get(pos)
        Lb1.delete(pos)
        Lb1.insert(pos-1, text)
    except IndexError:
        pass

def MoveRuleDown():
    try:
        pos = Lb1.curselection()[0]
        # get selected line index
        if pos == Lb1.size():
            return

        text = Lb1.get(pos)
        Lb1.delete(pos)
        Lb1.insert(pos+1, text)
    except IndexError:
        pass

def AddEditRule():
    add = Tk()
    add.title("Add/Edit Rule")
    add.geometry('{}x{}'.format(200, 200))
    itemsFrame = Frame(add,height=130)
    itemsFrame.pack()
    leftFrame = Frame(itemsFrame,height=130)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(itemsFrame,height=130)
    rightFrame.pack(side=LEFT)
    editWhiteList = Button(leftFrame,text="Edit White List")
    editWhiteList.pack()
    editBlackList = Button(leftFrame,text="Edit White List")
    editBlackList.pack()
    text_of_where_to_look = StringVar()
    where_to_look = Label(rightFrame,text="Where to look?").grid(row=0,sticky='w')
    HeaderCB = Checkbutton(rightFrame,text="Header").grid(row=1,sticky='w')
    StubCB = Checkbutton(rightFrame,text="Stub").grid(row=2,sticky='w')
    SuperRowCB = Checkbutton(rightFrame,text="Super-row").grid(row=3,sticky='w')
    DataCB = Checkbutton(rightFrame,text="Data").grid(row=4,sticky='w')
    EverywhereCB = Checkbutton(rightFrame,text="Everywhere").grid(row=5,sticky='w')
    bottomframe2 = Frame(add,height=1)
    bottomframe2.pack(side=BOTTOM)
    bottomframe = Frame(add,height=40)
    bottomframe.pack(side=BOTTOM)
    save = Button(bottomframe, text="Save", fg="black")
    save.pack()
    

def AddRule():
    AddEditRule()
    pass

def EditRule():
    AddEditRule()
    pass

def LoadFirstCfGScreen(project_name):
    top = Toplevel()
    top.title("Table InfExtractor")
    top.geometry('{}x{}'.format(500, 500))
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



    AddRules = Button(bottomframe, text="Add Rule", fg="black",command=AddRule)
    AddRules.pack( side = LEFT)
    DeleteRule = Button(bottomframe, text="Delete Rule", fg="black",command=RemoveRule)
    DeleteRule.pack( side = LEFT)
    EditRule = Button(bottomframe, text="Edit Rule", fg="black",command=AddRule)
    EditRule.pack( side = LEFT)
    MoveUpRule = Button(bottomframe, text="Move Up Rule", fg="black",command=MoveRuleUp)
    MoveUpRule.pack( side = LEFT)
    MoveDownRule = Button(bottomframe, text="Move Down Rule", fg="black",command=MoveRuleDown)
    MoveDownRule.pack( side = LEFT)
    Next = Button(bottomframe, text="Next", bg="green")
    Next.pack( side = LEFT)

def EnableLB(Lb3,E2):
    Lb3.configure(exportselection=True)
    Lb3.configure(state=NORMAL)
    E2.configure(state=DISABLED)
    E2.configure(exportselection=False)

def EnableLEntity(E2,Lb3):
    E2.configure(exportselection=True)
    E2.configure(state=NORMAL)
    Lb3.configure(state=DISABLED)
    Lb3.configure(exportselection=False)

def ShowChoice():
    print variab.get()
    
def FinishFirstScreen(variab,E2,Lb3,s):
    project_name= ""
    if(variab.get() == "NP"):
        project_name = E2.get()
    else:
        pos = Lb3.curselection()[0]
        project_name = Lb3.get(pos)
        #tkMessageBox.showinfo("Project selected", project_name)
    s.withdraw()
    FileManipulationHelper.CreateFoderIfNotExist("Projects/"+project_name)
    FileManipulationHelper.CreateProjectCfgFileIfNotExist("Projects/"+project_name)
    LoadFirstCfGScreen(project_name)

def LoadConfigScreen():
    s = Toplevel()
    s.title("Table InfExtractor")
    s.geometry('{}x{}'.format(500, 500))
    topframe = Frame(s,height=10)
    topframe.pack()
    frame = Frame(s)
    frame.pack()
    newproject = Radiobutton(frame,text="Create New Project",variable=variab,value="NP",command=lambda: EnableLEntity(E2,Lb3))
    newproject.pack()
    newprojectFrame = Frame(frame,height=100)
    names = StringVar()
    label_projectName = Label(newprojectFrame,textvariable=names)
    names.set("Project Name")
    label_projectName.pack(side = LEFT)
    E2 = Entry(newprojectFrame, bd =5)
    E2.pack(side = LEFT)
    #E2.configure(state=DISABLED)
    #E2.configure(exportselection=False)
    newprojectFrame.pack()
    loadproject = Radiobutton(frame,text="Load Project",variable=variab,value="LP", command=lambda: EnableLB(Lb3,E2))
    loadproject.pack()
    loadprojectFrame = Frame(frame,height=100)
    loadprojectFrame.pack()
    Lb3 = Listbox(loadprojectFrame,width=80,height=20)
    projects = FileManipulationHelper.readProjects()
    i = 1
    for p in projects:
        Lb3.insert(i,p)
        i=i+1
    Lb3.pack()
    Lb3.configure(exportselection=False)
    Lb3.configure(state=DISABLED)
    variab.set("NP")
    newproject.select()
    BottomFrame = Frame(s,height=10)
    BottomFrame.pack()
    NextButtonFrame = Frame(s)
    NextButtonFrame.pack()
    NextButton = Button(NextButtonFrame, text="Next", fg="black",command=lambda: FinishFirstScreen(variab,E2,Lb3,s))
    NextButton.pack()
    
    
main = Tk()
variab = StringVar() 
FileManipulationHelper.CreateFolderStructure()
main.withdraw()
LoadConfigScreen()
main.mainloop()
#LoadFirstCfGScreen()
