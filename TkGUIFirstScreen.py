'''
Created on 1 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import FileManipulationHelper
import QueryDBClass
import shutil 
import RuleClasses_LoadRulesForProcessingClass
import Process_Data
from threading import Thread
from time import sleep
Lb1 = None
Lb3 = None   
currentWhiteList = []
currentBlackList = []

def RemoveRule(Lb1,project_name):
    try:
        # get selected line index
        index = Lb1.curselection()[0]
        rule = Lb1.get(index)
        shutil.rmtree('Projects/'+project_name+'/'+rule)
        Lb1.delete(index)
    except IndexError:
        pass

def MoveRuleUp(Lb1):
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

def MoveRuleDown(Lb1):
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

def AddEditRule(project_name,vRuleName,RuleNameView,RulesListBox):
    global currentWhiteList
    global currentBlackList
    currentWhiteList = []
    currentBlackList = []
    
    RuleNameView.withdraw()
    add = Toplevel()
    #add.protocol("WM_DELETE_WINDOW", on_closing)
    add.title("Add Rule")
    add.geometry('{}x{}'.format(400, 300))
    itemsFrame = Frame(add,height=130)
    itemsFrame.pack()
    namerule_label = Label(itemsFrame,text="Name of the rule").grid(row=0,column=0,sticky='w')
    rulename_entry = Entry(itemsFrame,textvariable=vRuleName,state=DISABLED).grid(row=0,column=1,sticky='w')
    rule_name = vRuleName.get()
    editCueList = Button(itemsFrame,text="Edit Cue List",command=lambda:WhiteListWindow(project_name,rule_name)).grid(row=1,column=0,sticky='w')
    ClassLabel = Label(itemsFrame,text="Class name of result").grid(row=3,column=0,sticky='w')
    vClsIn = StringVar()
    ClassInput = Entry(itemsFrame,textvariable=vClsIn).grid(row=4,sticky='w')
    DefUnitLabel = Label(itemsFrame,text="Default unit").grid(row=5,column=0,sticky='w')
    vDefUnit = StringVar()
    DefUnInput = Entry(itemsFrame,textvariable=vDefUnit).grid(row=6,sticky='w')
    PosUnitLabel = Label(itemsFrame,text="Possible units (comma separated)").grid(row=7,column=0,sticky='w')
    vPosUnit = StringVar()
    PosUnInput = Entry(itemsFrame,textvariable=vPosUnit).grid(row=8,sticky='w')
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    prags = db.GetPragmaticClasses()
    pragVar = StringVar()
    pragVar.set(prags[0])
    PragLabel = Label(itemsFrame,text="Pragmatic class").grid(row=7,column=1,sticky='w')
    drop = OptionMenu(itemsFrame,pragVar,*prags)
    drop.grid(row=8,column=1,sticky='w')
    save = Button(itemsFrame, text="Save", fg="black",command=lambda:SaveRule(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox)).grid(row=9,column=1,sticky='w')

def SaveRule(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    #FileManipulationHelper.SaveWhiteList(rule_path, currentWhiteList)
    #FileManipulationHelper.SaveBlackList(rule_path, currentBlackList)
    FileManipulationHelper.MakeRuleCFGFile(rule_path,vClsIn,vDefUnit,vPosUnit,pragVar) 
    RulesListBox.insert(RulesListBox.size(),rule_name)
    add.withdraw()   
    
def SaveRuleEdit(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    #FileManipulationHelper.SaveWhiteList(rule_path, currentWhiteList)
    #FileManipulationHelper.SaveBlackList(rule_path, currentBlackList)
    FileManipulationHelper.MakeRuleCFGFile(rule_path, vClsIn,vDefUnit,vPosUnit,pragVar) 
    add.withdraw()  
    
  
def SetRuleName(project_name,RulesListBox):
    RuleNameView = Toplevel()
    RuleNameView.title("Set rule name") 
    RuleNameLabel = Label(RuleNameView,text="Name of the rule").grid(row=0,sticky='w')
    vRuleName = StringVar()
    RuleNameEntry = Entry(RuleNameView,textvariable=vRuleName).grid(row=1,sticky='w')
    RuleNameButton = Button(RuleNameView,text="Next ->>",command=lambda:AddEditRule(project_name,vRuleName,RuleNameView,RulesListBox)).grid(row=2,sticky='w')

def EditRule(project_name,Lb1):
    global currentWhiteList
    global currentBlackList
    currentWhiteList = []
    currentBlackList = []
    
    add = Toplevel()
    add.title("Edit Rule")
    add.geometry('{}x{}'.format(400, 300))
    itemsFrame = Frame(add,height=130)
    itemsFrame.pack()
    vRuleName = StringVar()
    pos = Lb1.curselection()[0]
    vRuleName.set(Lb1.get(pos))
    namerule_label = Label(itemsFrame,text="Name of the rule").grid(row=0,column=0,sticky='w')
    rulename_entry = Entry(itemsFrame,textvariable=vRuleName,state=DISABLED).grid(row=0,column=1,sticky='w')
    
    rule_name = vRuleName.get()
    ClassLabel = Label(itemsFrame,text="Class name of result").grid(row=3,column=0,sticky='w')
    vClsIn = StringVar()
    ClassInput = Entry(itemsFrame,textvariable=vClsIn)
    ClassInput.grid(row=4,sticky='w')
    DefUnitLabel = Label(itemsFrame,text="Default unit")
    DefUnitLabel.grid(row=5,column=0,sticky='w')
    vDefUnit = StringVar()
    DefUnInput = Entry(itemsFrame,textvariable=vDefUnit)
    DefUnInput.grid(row=6,sticky='w')
    PosUnitLabel = Label(itemsFrame,text="Possible units (comma separated)")
    PosUnitLabel.grid(row=7,column=0,sticky='w')
    vPosUnit = StringVar()
    PosUnInput = Entry(itemsFrame,textvariable=vPosUnit)
    PosUnInput.grid(row=8,sticky='w')
    
    editWhiteList = Button(itemsFrame,text="Edit White Cue List",command=lambda:WhiteListWindowEdit(project_name,rule_name)).grid(row=1,column=0,sticky='w')
    editBlackList = Button(itemsFrame,text="Edit Black Cue List",command=lambda:BlackListWindowEdit(project_name,rule_name)).grid(row=2,column=0,sticky='w')
    text_of_where_to_look = StringVar()
    cfg = FileManipulationHelper.loadRuleConfig(project_name, rule_name)
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    prags = db.GetPragmaticClasses()
    pragVar = StringVar()
    pragVar.set(cfg['PragClass'])
    vDefUnit.set(cfg['DefUnit'])
    vPosUnit.set(cfg['PosUnit'])
    vClsIn.set(cfg['Class'])
    PragLabel = Label(itemsFrame,text="Pragmatic class").grid(row=7,column=1,sticky='w')
    drop = OptionMenu(itemsFrame,pragVar,*prags)
    drop.grid(row=8,column=1,sticky='w')
    save = Button(itemsFrame, text="Save", fg="black",command=lambda:SaveRuleEdit(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar)).grid(row=9,column=1,sticky='w')
    

def AddRule(project_name,RulesListBox):
    SetRuleName(project_name,RulesListBox)
    
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



def SaveWhiteList(listAA,typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name):
    global currentWhiteList
    currentWhiteList = []
    currentWhiteList = listAA.split('\n')
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.SaveCueList(rule_path,rule_name, currentWhiteList,typeVar,look_head,look_stub,look_super,look_data,look_all)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    
    WhiteListWindow.withdraw()
    
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

    

#def EditRule():
#    AddEditRule()
#    pass

def ConfigureDatabaseScreen(project_name):
    DataConfig = Toplevel()
    db_host = ""
    db_port = ""
    db_user = ""
    db_pass = ""
    db_database = ""
    with open("Projects/"+project_name+"/"+"Config.cfg") as f:
        content = f.readlines()
    for line in content:
        split = line.split(":")
        split[0] = split[0].replace('\n','')
        split[1] = split[1].replace('\n','')
        if(split[0]=="Host"):
            db_host = split[1]
        if(split[0]=="Port"):
            db_port = split[1]
        if(split[0]=="User"):
            db_user = split[1]
        if(split[0]=="Pass"):
            db_pass = split[1]
        if(split[0]=="Database"):
            db_database = split[1]
    DataConfig.title("Database configuration")
    Host = Label(DataConfig,text="Host Name").grid(row=0,column=0,sticky='w')
    vHost = StringVar()
    HostName = Entry(DataConfig,textvariable=vHost).grid(row=0,column=1,sticky='w')
    vHost.set(db_host)
    
    Port = Label(DataConfig,text="Port Name").grid(row=1,column=0,sticky='w')
    vPort = StringVar()
    PortName = Entry(DataConfig,textvariable=vPort).grid(row=1,column=1,sticky='w')
    vPort.set(db_port)
    User = Label(DataConfig,text="User Name").grid(row=2,column=0,sticky='w')
    vUser = StringVar()
    UserName = Entry(DataConfig,textvariable=vUser).grid(row=2,column=1,sticky='w')
    vUser.set(db_user)
    Pass = Label(DataConfig,text="Password").grid(row=3,column=0,sticky='w')
    vPass = StringVar()
    PassName = Entry(DataConfig,show="*",textvariable=vPass).grid(row=3,column=1,sticky='w')
    vPass.set(db_pass)
    Database = Label(DataConfig,text="Database Name").grid(row=4,column=0,sticky='w')
    vDatabase = StringVar()
    DatabaseName = Entry(DataConfig,textvariable=vDatabase).grid(row=4,column=1,sticky='w')
    vDatabase.set(db_database)
    Save = Button(DataConfig, text="Save", bg="green",command=lambda: SaveDBSettings(vHost,vPort,vUser,vPass,vDatabase,DataConfig,project_name)).grid(row=5,column=1,sticky='w')
    
def SaveDBSettings(HostName,PortName,UserName,PassName,DatabaseName,DataConfig,project_name):
    
    hostname = HostName.get()
    portname = PortName.get()
    username = UserName.get()
    passname = PassName.get()
    database = DatabaseName.get()
    DataConfig.withdraw()
    FileManipulationHelper.SaveToConfigFile(project_name,hostname,portname,username,passname,database)
    pass


def LoadFirstCfGScreen(project_name):
    top = Toplevel()
    top.protocol("WM_DELETE_WINDOW", on_closing)
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
    name2 = StringVar()
    label_name2 = Label(frame,textvariable=name2)
    name2.set(project_name)
    label_name2.pack(side = LEFT)
    ConfigureDB = Button(frame, text="Configure Database", fg="black",command=lambda: ConfigureDatabaseScreen(project_name))
    ConfigureDB.pack( side = LEFT)
    clearTable = Button(frame, text="Clear DB Table", fg="black",command = lambda: ClearDBTables(project_name))
    clearTable.pack( side = LEFT)
    rules = FileManipulationHelper.loadRules(project_name)
    Lb1 = Listbox(middleframe,width=80,height=20)
    Lb1.pack()
    size = Lb1.size()
    for rule in rules:
        Lb1.insert(size,rule)
        size = Lb1.size()
    AddRules = Button(bottomframe, text="Add Rule", fg="black",command=lambda:AddRule(project_name,Lb1))
    AddRules.pack( side = LEFT)
    DeleteRule = Button(bottomframe, text="Delete Rule", fg="black",command=lambda:RemoveRule(Lb1,project_name))
    DeleteRule.pack( side = LEFT)
    EditRuleA = Button(bottomframe, text="Edit Rule", fg="black",command=lambda:EditRule(project_name,Lb1))
    EditRuleA.pack( side = LEFT)
    MoveUpRule = Button(bottomframe, text="Move Up Rule", fg="black",command=lambda:MoveRuleUp(Lb1))
    MoveUpRule.pack( side = LEFT)
    MoveDownRule = Button(bottomframe, text="Move Down Rule", fg="black",command=lambda:MoveRuleDown(Lb1))
    MoveDownRule.pack( side = LEFT)
    Next = Button(bottomframe, text="Next", bg="green", command=lambda:LoadRulesCfGMainScreen(project_name,top))
    Next.pack( side = LEFT)
    
def ClearDBTables(project_name):
    dbSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    query = QueryDBClass.QueryDBCalss(dbSettings['Host'],dbSettings['User'],dbSettings['Pass'],dbSettings['Database'])
    query.ClearCreatedTables()
    query.CreateAdditionalTables()
    

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
    s.protocol("WM_DELETE_WINDOW", on_closing)
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
    
def on_closing():
    main.destroy()
    
########################################
#                                      #
#   Frames for setting up the rules    #
#                                      #
########################################
def LoadRulesCfGMainScreen(project_name,SetLexRules):
    top = Toplevel()
    SetLexRules.withdraw()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Set up rules")
    top.geometry('{}x{}'.format(300, 400))
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
    name.set("Choose from default set of rules:")
    label_name.grid(row=0,column=0,sticky='w')
    int_val = IntVar()
    IntCB = Checkbutton(frame,text="Single integer",variable = int_val)
    IntCB.grid(row=1,column=0,sticky='w')
    float_val = IntVar()
    FloatCB = Checkbutton(frame,text="Single Float",variable = float_val)
    FloatCB.grid(row=2,column=0,sticky='w')
    stats_val = IntVar()
    StatsCB = Checkbutton(frame,text="Statistical value (Mean,SD,Ranges)",variable = stats_val)
    StatsCB.grid(row=3,column=0,sticky='w')
    alt_val = IntVar()
    AltCB = Checkbutton(frame,text="Two alternative values",variable = alt_val)
    AltCB.grid(row=4,column=0,sticky='w')
    none_val = IntVar()
    NoneCB = Checkbutton(frame,text="None (Write your own rules)",variable = none_val)
    NoneCB.grid(row=5,column=0,sticky='w')
    skip_val = IntVar()
    skip_val.set(1)
    SkipCB = Checkbutton(frame,text="Skip this step (Will not overwrite old rules)",variable = skip_val)
    SkipCB.grid(row=5,column=0,sticky='w')
    Next = Button(bottomframe, text="Next", bg="green",command = lambda:EditSintacticRules(project_name, top,int_val,float_val,stats_val,alt_val,none_val,skip_val))
    Next.pack( side = LEFT)
    pass

def EditSintacticRules(project_name, ChoseSintRulesWindow,int_val,float_val,stats_val,alt_val,none_val,skip_val):
    ChoseSintRulesWindow.withdraw()
    top = Toplevel()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Modify selected rules")
    top.geometry('{}x{}'.format(400, 300))
    topframe = Frame(top,height=10)
    topframe.pack()
    frame = Frame(top)
    frame.pack()
    topframe2 = Frame(top,height=10)
    topframe2.pack()
    rules = StringVar()
    rulelist = Text(frame,height=15,width=40)
    rulelist.grid(row=1,sticky='w')
    fpaths = []
    if(int_val.get()==1):
        fpaths.append('DefaultSintacticRules/SingleInteger')
    if(float_val.get()==1):
        fpaths.append('DefaultSintacticRules/SingleFloat')
    if(stats_val.get()==1):
        fpaths.append('DefaultSintacticRules/StatisticalValues')
    if(alt_val.get()==1):
        fpaths.append('DefaultSintacticRules/Alternatives')
    if skip_val.get()==1:
        SaveSintacticRules(rulelist.get("1.0",END),top,project_name,skip_val)
        return
    rules = []
    for path in fpaths:
        rules = rules + FileManipulationHelper.LoadRules(path)
        
    i = 1
    for w in rules:
        rulelist.insert(str(i)+'.0',w)
        i=i+1
    
    saveButton = Button(frame,text="Next",bg="green",fg="black",command=lambda:SaveSintacticRules(rulelist.get("1.0",END),top,project_name,skip_val)).grid(row=2,sticky='w')
    pass

def MakeWorkingScreen(rules, window,project_name,skip_val):
    window.withdraw()
    top = Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name)
    for rule in get_rules:
        rule_path = 'Projects/'+project_name+'/'+rule
        if(skip_val.get()!=1):
            FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule)
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Working...")
    top.geometry('{}x{}'.format(400, 300))
    lab = Label(top,text="Please be patient...")
    lab.pack()
    rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    


def ProcessDataV(project_name,processing_rules,window,extracted):
    extracted = IntVar()
    extracted.set(0)
    Process_Data.ProcessDataBase(project_name,processing_rules)
    

def SaveSintacticRules(rules, window,project_name,skip_val):
    global lab2
    
    window.withdraw()
    top = Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name)
    for rule in get_rules:
        rule_path = 'Projects/'+project_name+'/'+rule
        if(skip_val.get()!=1):
            FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule)
    processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Working...")
    top.geometry('{}x{}'.format(400, 300))
    extracted = IntVar()
    lab = Label(top,text="Please be patient... Processing...")
    lab.pack()
    lab2 = Label(top,text=extracted)
    lab2.pack()
    thread = Thread(target = ProcessDataV, args = (project_name,processing_rules,top,extracted))
    thread.start()
    print "thread finished...exiting"
    #Process_Data.ProcessDataBase(project_name,processing_rules)
    pass
   
    
##################################################################
lab2 = None
main = Tk()
variab = StringVar() 
FileManipulationHelper.CreateFolderStructure()
main.withdraw()
LoadConfigScreen()
main.protocol("WM_DELETE_WINDOW", on_closing)
main.mainloop()
#LoadFirstCfGScreen()
