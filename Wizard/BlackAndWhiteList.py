'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import QueryDBClass
import FileManipulationHelper
def SaveBlackList(listAA,BlackListWindow):
    global currentBlackList
    currentBlackList = []
    currentBlackList = listAA.split('\n')
    BlackListWindow.withdraw()

def BlackListWindow(project_name,rule_name):
    BlackListWindow =Toplevel()
    BlackListWindow.title("Edit Black List")
    BlackListWindow.geometry('{}x{}'.format(450, 250))
    itemsFrame = Frame(BlackListWindow)
    itemsFrame.pack()
    namerule_label = Label(itemsFrame,text="List of terms in blacklist").grid(row=0,sticky='w')
    list = Text(itemsFrame,height=10,width=50)
    list.grid(row=1,sticky='w')
    saveButton = Button(itemsFrame,text="Save",fg="black",command=lambda:SaveBlackList(list.get("1.0",END),BlackListWindow)).grid(row=2,sticky='w')

def WhiteListWindow(project_name,rule_name):
    WhiteListWindow =Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Frame(WhiteListWindow)
    itemsFrame.pack(side=LEFT)
    choiseFrame = Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=RIGHT)
    type = ['WhiteList','BlackList']
    typeVar = StringVar()
    typeVar.set(type[0])
    TypeLabel = Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    drop = OptionMenu(choiseFrame,typeVar,*type)
    drop.grid(row=1,column=0,sticky='w')
    where_to_look = Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = IntVar()
    HeaderCB = Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = IntVar()
    StubCB = Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = IntVar()
    SuperRowCB = Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = IntVar()
    DataCB = Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = IntVar()
    EverywhereCB = Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    whitelist = Text(itemsFrame,height=10,width=50)
    whitelist.grid(row=1,sticky='w')
    saveButton = Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(whitelist.get("1.0",END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=2,sticky='w')

    
def WhiteListWindowEdit(project_name,rule_name):
    WhiteListWindow =Toplevel()
    WhiteListWindow.title("Edit White Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Frame(WhiteListWindow)
    itemsFrame.pack(side=LEFT)
    choiseFrame = Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=RIGHT)
    type = ['WhiteList','BlackList']
    typeVar = StringVar()
    typeVar.set(type[0])
    TypeLabel = Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    drop = OptionMenu(choiseFrame,typeVar,*type)
    drop.grid(row=1,column=0,sticky='w')
    where_to_look = Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = IntVar()
    HeaderCB = Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = IntVar()
    StubCB = Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = IntVar()
    SuperRowCB = Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = IntVar()
    DataCB = Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = IntVar()
    EverywhereCB = Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    list = Text(itemsFrame,height=10,width=50)
    list.grid(row=1,sticky='w')
    whitelist = FileManipulationHelper.loadWhiteList(project_name, rule_name)
    i = 1
    afterWordList = False
    for w in whitelist:
        w = w.replace('\n','')
        splitted = w.split(':')
        if splitted[0]=='Type':
            if splitted[1]=='WhiteList':
                typeVar.set(type[0])
            else:
                typeVar.set(type[1])
        if splitted[0]=='Header':
            look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            look_data.set(int(splitted[1]))
        if splitted[0]=='All':
            look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            list.insert(str(i)+'.0',w+'\n')
            i=i+1
    saveButton = Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(list.get("1.0",END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=2,sticky='w')



def BlackListWindowEdit(project_name,rule_name):
    WhiteListWindow =Toplevel()
    WhiteListWindow.title("Edit White Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Frame(WhiteListWindow)
    itemsFrame.pack(side=LEFT)
    choiseFrame = Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=RIGHT)
    type = ['WhiteList','BlackList']
    typeVar = StringVar()
    typeVar.set(type[0])
    TypeLabel = Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    drop = OptionMenu(choiseFrame,typeVar,*type)
    drop.grid(row=1,column=0,sticky='w')
    where_to_look = Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = IntVar()
    HeaderCB = Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = IntVar()
    StubCB = Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = IntVar()
    SuperRowCB = Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = IntVar()
    DataCB = Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = IntVar()
    EverywhereCB = Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    list = Text(itemsFrame,height=10,width=50)
    list.grid(row=1,sticky='w')
    whitelist = FileManipulationHelper.loadBlackList(project_name, rule_name)
    i = 1
    afterWordList = False
    for w in whitelist:
        w = w.replace('\n','')
        splitted = w.split(':')
        if splitted[0]=='Type':
            if splitted[1]=='WhiteList':
                typeVar.set(type[0])
            else:
                typeVar.set(type[1])
        if splitted[0]=='Header':
            look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            look_data.set(int(splitted[1]))
        if splitted[0]=='All':
            look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            list.insert(str(i)+'.0',w+'\n')
            i=i+1
    saveButton = Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(list.get("1.0",END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=2,sticky='w')



def SaveWhiteList(listAA,typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name):
    global currentWhiteList
    currentWhiteList = []
    currentWhiteList = listAA.split('\n')
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.SaveCueList(rule_path,rule_name, currentWhiteList,typeVar,look_head,look_stub,look_super,look_data,look_all)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()