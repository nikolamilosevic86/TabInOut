'''
Created on 1 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import Tix
import FileManipulationHelper
import RuleClasses_LoadRulesForProcessingClass
from threading import Thread
from EditRule import EditRule
from SimpleRuleOps import MoveRuleDown,MoveRuleUp,RemoveRule,AddRule,EnableLEntity,EnableLB
from DatabaseSettings import ConfigureDatabaseScreen,ClearDBTables
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
    rules = FileManipulationHelper.loadRules(project_name)
    Lb1 = Tix.Listbox(middleframe,width=80,height=20)
    Lb1.pack()
    size = Lb1.size()
    for rule in rules:
        Lb1.insert(size,rule)
        size = Lb1.size()
    AddRules = Tix.Button(bottomframe, text="Add Rule", fg="black",command=lambda:AddRule(project_name,Lb1))
    AddRules.pack( side = Tix.LEFT)
    DeleteRule = Tix.Button(bottomframe, text="Delete Rule", fg="black",command=lambda:RemoveRule(Lb1,project_name))
    DeleteRule.pack( side = Tix.LEFT)
    EditRuleA = Tix.Button(bottomframe, text="Edit Rule", fg="black",command=lambda:EditRule(project_name,Lb1))
    EditRuleA.pack( side = Tix.LEFT)
    MoveUpRule = Tix.Button(bottomframe, text="Move Up Rule", fg="black",command=lambda:MoveRuleUp(Lb1))
    MoveUpRule.pack( side = Tix.LEFT)
    MoveDownRule =Tix.Button(bottomframe, text="Move Down Rule", fg="black",command=lambda:MoveRuleDown(Lb1))
    MoveDownRule.pack( side = Tix.LEFT)
    Next = Tix.Button(bottomframe, text="Next", bg="green", command=lambda:LoadRulesCfGMainScreen(project_name,top))
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
    #E2.configure(state=DISABLED)
    #E2.configure(exportselection=False)
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
    
def on_closing():
    global main
    main.destroy()
    
########################################
#                                      #
#   Frames for setting up the rules    #
#                                      #
########################################
def LoadRulesCfGMainScreen(project_name,SetLexRules):
    top = Tix.Toplevel()
    SetLexRules.withdraw()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Set up rules")
    top.geometry('{}x{}'.format(300, 400))
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
    name.set("Choose from default set of rules:")
    label_name.grid(row=0,column=0,sticky='w')
    int_val = Tix.IntVar()
    IntCB = Tix.Checkbutton(frame,text="Single integer",variable = int_val)
    IntCB.grid(row=1,column=0,sticky='w')
    float_val = Tix.IntVar()
    FloatCB = Tix.Checkbutton(frame,text="Single Float",variable = float_val)
    FloatCB.grid(row=2,column=0,sticky='w')
    stats_val = Tix.IntVar()
    StatsCB = Tix.Checkbutton(frame,text="Statistical value (Mean,SD,Ranges)",variable = stats_val)
    StatsCB.grid(row=3,column=0,sticky='w')
    alt_val = Tix.IntVar()
    AltCB = Tix.Checkbutton(frame,text="Two alternative values",variable = alt_val)
    AltCB.grid(row=4,column=0,sticky='w')
    none_val = Tix.IntVar()
    NoneCB = Tix.Checkbutton(frame,text="None (Write your own rules)",variable = none_val)
    NoneCB.grid(row=5,column=0,sticky='w')
    skip_val = Tix.IntVar()
    skip_val.set(1)
    SkipCB = Tix.Checkbutton(frame,text="Skip this step (Will not overwrite old rules)",variable = skip_val)
    SkipCB.grid(row=5,column=0,sticky='w')
    Next = Tix.Button(bottomframe, text="Next", bg="green",command = lambda:EditSintacticRules(project_name, top,int_val,float_val,stats_val,alt_val,none_val,skip_val))
    Next.pack( side = Tix.LEFT)
    pass

def EditSintacticRules(project_name, ChoseSintRulesWindow,int_val,float_val,stats_val,alt_val,none_val,skip_val):
    ChoseSintRulesWindow.withdraw()
    top = Tix.Toplevel()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Modify selected rules")
    top.geometry('{}x{}'.format(400, 300))
    topframe = Tix.Frame(top,height=10)
    topframe.pack()
    frame = Tix.Frame(top)
    frame.pack()
    topframe2 = Tix.Frame(top,height=10)
    topframe2.pack()
    rules = Tix.StringVar()
    rulelist = Tix.Text(frame,height=15,width=40)
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
        SaveSintacticRules(rulelist.get("1.0",Tix.END),top,project_name,skip_val)
        return
    rules = []
    for path in fpaths:
        rules = rules + FileManipulationHelper.LoadRules(path)
        
    i = 1
    for w in rules:
        rulelist.insert(str(i)+'.0',w)
        i=i+1
    
    saveButton = Tix.Button(frame,text="Next",bg="green",fg="black",command=lambda:SaveSintacticRules(rulelist.get("1.0",Tix.END),top,project_name,skip_val)).grid(row=2,sticky='w')
    pass


# Syntactic rules
def SaveSintacticRules(rules, window,project_name,skip_val):
    global lab2
    
    window.withdraw()
    top = Tix.Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name)
    for rule in get_rules:
        rule_path = 'Projects/'+project_name+'/'+rule
        if(skip_val.get()!=1):
            FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule)
    processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
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
    pass
    thread = Thread(target = ProcessDataV, args = (project_name,processing_rules,top,extracted))
    thread.start()
    print "thread finished...exiting"
    pass

def MakeWorkingScreen(rules, window,project_name,skip_val):
    window.withdraw()
    top = Tix.Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name)
    for rule in get_rules:
        rule_path = 'Projects/'+project_name+'/'+rule
        if(skip_val.get()!=1):
            FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule)
    top.protocol("WM_DELETE_WINDOW", on_closing)
    top.title("Working...")
    top.geometry('{}x{}'.format(400, 300))
    lab = Tix.Label(top,text="Please be patient...")
    lab.pack()
    rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    
##################################################################
lab2 = None
main = Tix.Tk()
variab = Tix.StringVar() 
FileManipulationHelper.CreateFolderStructure()
main.withdraw()
LoadConfigScreen()
main.protocol("WM_DELETE_WINDOW", on_closing)
main.mainloop()
