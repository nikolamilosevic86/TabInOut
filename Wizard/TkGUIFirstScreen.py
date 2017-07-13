'''
Created on 1 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import Tix
from threading import Thread
import Tkinter
import ttk

import FileManipulationHelper
from DatabaseSettings import ConfigureDatabaseScreen,ClearDBTables
from EditRule import EditRule, AddEditRule
from  RuleClasses_LoadRulesForProcessingClass import LoadRulesForProcessing
from SimpleRuleOps import MoveRuleDown,MoveRuleUp,RemoveRule,EnableLEntity,EnableLB, AddVariable
from SyntacticRules import ProcessDataV,RefreshDatabaseData

Lb1 = None
Lb3 = None   
currentWhiteList = []
currentBlackList = []


def LoadFirstCfGScreen(project_name):
    top = Tix.Toplevel()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Table InfExtractor")
    top.geometry('{}x{}'.format(500, 500))
    topframe = Tix.Frame(top,height=10)
    topframe.pack()
    frame = Tix.Frame(top)
    frame.pack()
    topframe2 = Tix.Frame(top,height=10)
    topframe2.pack()
    middleframe = Tix.Frame(top)
    middleframe.pack()
    bottomframe2 = Tix.Frame(top,height=10)
    bottomframe2.pack( side = Tix.BOTTOM )
    bottomframe = Tix.Frame(top)
    bottomframe.pack( side = Tix.BOTTOM )

    name = Tix.StringVar()
    label_name = Tix.Label(frame,textvariable=name)
    name.set("Name of task:")
    label_name.pack(side = Tix.LEFT)
    name2 = Tix.StringVar()
    label_name2 = Tix.Label(frame,textvariable=name2)
    name2.set(project_name)
    label_name2.pack(side = Tix.LEFT)
    ConfigureDB = Tix.Button(frame, text="Configure Database", fg="black",command=lambda: ConfigureDatabaseScreen(project_name))
    ConfigureDB.pack( side = Tix.LEFT)
    clearTable = Tix.Button(frame, text="Clear DB Table", fg="black",command = lambda: ClearDBTables(project_name))
    clearTable.pack( side = Tix.LEFT)
    vars = FileManipulationHelper.loadVariables(project_name)
    Lb1 = ttk.Treeview(middleframe,columns=40,height=19)

    Lb1.pack()
    size = Lb1.size()
    for var in vars:
        Lb1.insert('', 'end', var, text=var)
        rules = FileManipulationHelper.loadRules(project_name,var)
        for rule in rules:
            Lb1.insert(var, 'end', text=rule)
        #Lb1.insert(size,rule)
        size = Lb1.size()
    AddVariables = Tix.Button(bottomframe, text="Add Variable", fg="black", command=lambda:AddVariable(project_name, Lb1))
    AddVariables.pack(side=Tix.LEFT)

    AddRules = Tix.Button(bottomframe, text="Add Rule", fg="black",command=lambda:AddEditRule(project_name,Lb1))
    AddRules.pack( side = Tix.LEFT)
    DeleteRule = Tix.Button(bottomframe, text="Delete Rule", fg="black",command=lambda:RemoveRule(Lb1,project_name))
    DeleteRule.pack( side = Tix.LEFT)
    EditRuleA = Tix.Button(bottomframe, text="Edit Rule", fg="black",command=lambda:EditRule(project_name,Lb1))
    EditRuleA.pack( side = Tix.LEFT)
    #MoveUpRule = Tix.Button(bottomframe, text="Move Up Rule", fg="black",command=lambda:MoveRuleUp(Lb1))
    #MoveUpRule.pack( side = Tix.LEFT)
    #MoveDownRule =Tix.Button(bottomframe, text="Move Down Rule", fg="black",command=lambda:MoveRuleDown(Lb1))
    #MoveDownRule.pack( side = Tix.LEFT)
    skip_val = 0
    Next = Tix.Button(bottomframe, text="Next", bg="green", command=lambda:MakeWorkingScreen(rules, top,project_name,skip_val))
    Next.pack( side = Tix.LEFT)

def ShowChoice():
    print variab.get()
    
def FinishFirstScreen(variab,E2,Lb3,s):
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
    s = Tix.Toplevel()
    s.protocol("WM_DELETE_WINDOW", on_closing)
    s.title("Table InfExtractor")
    s.geometry('{}x{}'.format(500, 500))
    topframe = Tix.Frame(s,height=10)
    topframe.pack()
    frame = Tix.Frame(s)
    frame.pack()
    newproject = Tix.Radiobutton(frame,text="Create New Project",variable=variab,value="NP",command=lambda: EnableLEntity(E2,Lb3))
    newproject.pack()
    newprojectFrame = Tix.Frame(frame,height=100)
    names = Tix.StringVar()
    label_projectName = Tix.Label(newprojectFrame,textvariable=names)
    names.set("Project Name")
    label_projectName.pack(side = Tix.LEFT)
    E2 = Tix.Entry(newprojectFrame, bd =5)
    E2.pack(side = Tix.LEFT)
    newprojectFrame.pack()
    loadproject = Tix.Radiobutton(frame,text="Load Project",variable=variab,value="LP", command=lambda: EnableLB(Lb3,E2))
    loadproject.pack()
    loadprojectFrame = Tix.Frame(frame,height=100)
    loadprojectFrame.pack()
    Lb3 = Tix.Listbox(loadprojectFrame,width=80,height=20)
    projects = FileManipulationHelper.readProjects()
    i = 1
    for p in projects:
        Lb3.insert(i,p)
        i=i+1
    Lb3.pack()
    Lb3.configure(exportselection=False)
    Lb3.configure(state=Tix.DISABLED)
    variab.set("NP")
    newproject.select()
    BottomFrame = Tix.Frame(s,height=10)
    BottomFrame.pack()
    NextButtonFrame = Tix.Frame(s)
    NextButtonFrame.pack()
    NextButton = Tix.Button(NextButtonFrame, text="Next", fg="black",command=lambda: FinishFirstScreen(variab,E2,Lb3,s))
    NextButton.pack()



def MakeWorkingScreen(rules, window,project_name,skip_val):
    window.withdraw()
    top = Tix.Toplevel()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Working...")
    top.geometry('{}x{}'.format(400, 400))
    extracted = Tix.IntVar()
    lab = Tix.Label(top,text="Please be patient... Processing...")
    lab.pack()
    Lb1 = Tix.Listbox(top,width=60,height=20)
    Lb1.pack()
    size = Lb1.size()
    refreshButton = Tix.Button(top,text="Refresh",fg="black",command=lambda:RefreshDatabaseData(Lb1,project_name))
    refreshButton.pack()
    processing_rules = LoadRulesForProcessing(project_name)
    thread = Thread(target = ProcessDataV, args = (project_name,processing_rules,top,extracted))
    thread.start()
    print "thread finished...exiting"
    pass

def on_closing():
    global main
    main.destroy()
    
##################################################################
lab2 = None
main = Tix.Tk()
variab = Tix.StringVar() 
FileManipulationHelper.CreateFolderStructure()
main.withdraw()
LoadConfigScreen()
main.protocol("WM_DELETE_WINDOW", on_closing)
main.mainloop()
