'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import FileManipulationHelper
from threading import Thread
import RuleClasses_LoadRulesForProcessingClass
import Process_Data



def RefreshDatabaseData(ListBox,project_name):
    extracted = Process_Data.GetExtractedData(project_name)
    size = 0
    for ex in extracted:
        row = str(ex[0])+','+str(ex[1])+','+str(ex[2])+','+str(ex[3])+','+str(ex[4])+','+str(ex[5])+','+str(ex[6])+','+str(ex[7])+','+str(ex[8])+','+str(ex[9])+','+str(ex[10])+','+str(ex[11])+','+str(ex[12])
        ListBox.insert(size,row)
        size = ListBox.size()
    pass


def ProcessDataV(project_name,processing_rules,window,extracted):
    extracted = IntVar()
    extracted.set(0)
    Process_Data.ProcessDataBase(project_name,processing_rules)
    
    
########################################
#                                      #
#   Frames for setting up the rules    #
#                                      #
########################################
def LoadRulesCfGMainScreen(project_name,rule_name):

    #SetLexRules.withdraw()
    #top.protocol("WM_DELETE_WINDOW", on_closing)
    processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name,True)
    for rule in processing_rules:
        if rule.RuleName == rule_name:
            if(rule.RuleType == "Categorical"):
                skip_val = IntVar()
                skip_val.set(0)
                return
    top = Toplevel()
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
    #top.protocol("WM_DELETE_WINDOW", on_closing)
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


# Syntactic rules
def SaveSintacticRules(rules, window,project_name,skip_val):
    global lab2
    
    window.withdraw()
    #top = Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name)
    for rule in get_rules:
        rule_path = 'Projects/'+project_name+'/'+rule
        if(skip_val.get()!=1):
            FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule)
    #processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    #top.protocol("WM_DELETE_WINDOW", on_closing)
    

def MakeWorkingScreen(rules, window,project_name,skip_val):
    window.withdraw()
    top = Toplevel()
    top.title("Working...")
    top.geometry('{}x{}'.format(400, 400))
    extracted = IntVar()
    lab = Label(top,text="Please be patient... Processing...")
    lab.pack()
    Lb1 = Listbox(top,width=60,height=20)
    Lb1.pack()
    size = Lb1.size()
    refreshButton = Button(top,text="Refresh",fg="black",command=lambda:RefreshDatabaseData(Lb1,project_name))
    refreshButton.pack()
    processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    thread = Thread(target = ProcessDataV, args = (project_name,processing_rules,top,extracted))
    thread.start()
    print "thread finished...exiting"
    pass
    