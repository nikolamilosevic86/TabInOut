'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import QueryDBClass
import FileManipulationHelper
from BlackAndWhiteList import WhiteListWindow,WhiteListWindowEdit,SemanticListWindow,SemanticListWindowEdit
from SyntacticRules import LoadRulesCfGMainScreen,MakeChangesToSyntacticRules
from SimpleRuleOps import loadVariableConfig


def AddEditRule(project_name,RulesListBox):
    global currentWhiteList
    global currentBlackList
    currentWhiteList = []
    currentBlackList = []
    rule = RulesListBox.selection()[0]


    add = Toplevel()
    #add.protocol("WM_DELETE_WINDOW", on_closing)
    add.title("Add Rule")
    add.geometry('{}x{}'.format(400, 350))
    itemsFrame = Frame(add,height=130)
    itemsFrame.pack()
    namerule_label = Label(itemsFrame,text="Name of the rule").grid(row=0,column=0,sticky='w')
    vRule = StringVar()

    rulename_entry = Entry(itemsFrame,textvariable=vRule).grid(row=0,column=1,sticky='w')
    #editCueList = Button(itemsFrame,text="Edit Cue List",command=lambda:WhiteListWindow(project_name,rule_name)).grid(row=1,column=0,sticky='w')
    ClassLabel = Label(itemsFrame,text="Variable name (Information class)").grid(row=3,column=0,sticky='w')
    vClsIn = StringVar()
    vClsIn.set(rule)
    ClassInput = Entry(itemsFrame,textvariable=vClsIn,state=DISABLED).grid(row=4,sticky='w')
    vDefUnit = StringVar()
    vPosUnit = StringVar()
    cfg = loadVariableConfig(project_name,rule)
    vRuleType = StringVar()
    vRuleType.set(cfg["VariableType"])
    if(cfg["VariableType"] == "Numeric" or cfg["VariableType"]=="Categorical"):
        DefUnitLabel = Label(itemsFrame,text="Default unit").grid(row=5,column=0,sticky='w')
        DefUnInput = Entry(itemsFrame,textvariable=vDefUnit).grid(row=6,sticky='w')
        PosUnitLabel = Label(itemsFrame,text="Possible units (comma separated)").grid(row=7,column=0,sticky='w')    
        PosUnInput = Entry(itemsFrame,textvariable=vPosUnit).grid(row=8,sticky='w')
    #if(vRuleType.get() == "Categorical"):
    #    PosUnitLabel = Label(itemsFrame,text="Possible categories (comma separated)").grid(row=7,column=0,sticky='w')
    #    vPosUnit = StringVar()
    #    PosUnInput = Entry(itemsFrame,textvariable=vPosUnit).grid(row=8,sticky='w')
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    prags = db.GetPragmaticClasses()
    prags.insert(0,"Any")
    pragVar = StringVar()
    pragVar.set(prags[0])
    PragLabel = Label(itemsFrame,text="Table type (pragmatics)").grid(row=9,column=0,sticky='w')
    drop = OptionMenu(itemsFrame,pragVar,*prags)
    drop.grid(row=10,column=0,sticky='w')
    vLexSemRule = StringVar()
    vLexSemRule.set("Lexical")
    #PosUnitLabel = Label(itemsFrame,text="Select rule creation mechanism").grid(row=11,column=0,sticky='w')
    #Radiobutton(itemsFrame, text="Lexical (White List+Black list)", variable=vLexSemRule, value="Lexical").grid(row=12,sticky='w')
    #Radiobutton(itemsFrame, text="Semantic (UMLS Sem. type+Black list)", variable=vLexSemRule, value="Semantic").grid(row=13,sticky='w')
    where_to_look = Label(itemsFrame,text="Where to look for data?").grid(row=2,column=1,sticky='w')
    wl_look_head = IntVar()
    WLHeaderCB = Checkbutton(itemsFrame,text="Header",variable = wl_look_head).grid(row=3,column=1,sticky='w')
    wl_look_stub = IntVar()
    WLStubCB = Checkbutton(itemsFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=1,sticky='w')
    wl_look_super = IntVar()
    WLSuperRowCB = Checkbutton(itemsFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=1,sticky='w')
    wl_look_data = IntVar()
    WLDataCB = Checkbutton(itemsFrame,text="Data",variable = wl_look_data).grid(row=6,column=1,sticky='w')
    save = Button(itemsFrame, text="Save", fg="black",command=lambda:SaveRule(project_name,vRule.get(),add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox,vRuleType,vLexSemRule,wl_look_head,wl_look_stub,wl_look_super,wl_look_data)).grid(row=14,column=1,sticky='w')
    

def SaveRuleEdit(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,ruleType,ruleMech,wl_look_head,wl_look_stub,wl_look_super,wl_look_data):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    vRuleType = StringVar()
    vLexSemRule = StringVar()
    vRuleType.set(ruleType)
    vLexSemRule.set(ruleMech)
    FileManipulationHelper.MakeRuleCFGFile(rule_path, vClsIn,vDefUnit,vPosUnit,pragVar,vRuleType,vLexSemRule,wl_look_head,wl_look_stub,wl_look_super,wl_look_data) 
    add.withdraw()  

def SaveRule(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox,vRuleType,vLexSemRule,wl_look_head,wl_look_stub,wl_look_super,wl_look_data):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+vClsIn.get()+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    #FileManipulationHelper.SaveWhiteList(rule_path, currentWhiteList)
    #FileManipulationHelper.SaveBlackList(rule_path, currentBlackList)
    FileManipulationHelper.MakeRuleCFGFile(rule_path,vClsIn,vDefUnit,vPosUnit,pragVar,vRuleType,vLexSemRule,wl_look_head,wl_look_stub,wl_look_super,wl_look_data) 
    RulesListBox.insert(vClsIn.get(), 'end',text=rule_name)
    add.withdraw() 
    if(vLexSemRule.get()=="Lexical"):
        WhiteListWindow(project_name,rule_name,vClsIn)
    if(vLexSemRule.get()=="Semantic"):
        SemanticListWindow(project_name,rule_name,vClsIn)


    
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
    # Obtain rule/vaiable properly. The following won't work
    pos = Lb1.curselection()[0]
    vRuleName.set(Lb1.get(pos))
    namerule_label = Label(itemsFrame,text="Name of the rule").grid(row=0,column=0,sticky='w')
    rulename_entry = Entry(itemsFrame,textvariable=vRuleName,state=DISABLED).grid(row=0,column=1,sticky='w')
    rule_name = vRuleName.get()
    cfg = FileManipulationHelper.loadRuleConfig(project_name, rule_name)
    ruleType = cfg['RuleType'].replace('\n','')
    ClassLabel = Label(itemsFrame,text="Class name of result").grid(row=2,column=0,sticky='w')
    vClsIn = StringVar()
    ClassInput = Entry(itemsFrame,textvariable=vClsIn)
    ClassInput.grid(row=3,sticky='w')
    vDefUnit = StringVar()
    vPosUnit = StringVar()
    if ruleType =='Numeric' or ruleType=="Categorical":
        DefUnitLabel = Label(itemsFrame,text="Default unit")
        DefUnitLabel.grid(row=4,column=0,sticky='w')
        vDefUnit = StringVar()
        DefUnInput = Entry(itemsFrame,textvariable=vDefUnit)
        DefUnInput.grid(row=5,sticky='w')
        PosUnitLabel = Label(itemsFrame,text="Possible units (comma separated)")
        PosUnitLabel.grid(row=6,column=0,sticky='w')
        PosUnInput = Entry(itemsFrame,textvariable=vPosUnit)
        PosUnInput.grid(row=7,sticky='w')
    ruleMech = cfg['RuleCreationMech'].replace('\n','')
    where_to_look = Label(itemsFrame,text="Where to look for data?").grid(row=2,column=1,sticky='w')
    wl_look_head = IntVar()
    if('DataInHeader' in cfg.keys() and cfg['DataInHeader']!=None and cfg['DataInHeader']=='1'):
        wl_look_head.set(1)
    else:
        wl_look_head.set(0)
    WLHeaderCB = Checkbutton(itemsFrame,text="Header",variable = wl_look_head).grid(row=3,column=1,sticky='w')
    wl_look_stub = IntVar()
    if('DataInStub' in cfg.keys() and cfg['DataInStub']!=None and cfg['DataInStub']=='1'):
        wl_look_stub.set(1)
    else:
        wl_look_stub.set(0)
    WLStubCB = Checkbutton(itemsFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=1,sticky='w')
    wl_look_super = IntVar()
    if('DataInSuperRow' in cfg.keys() and cfg['DataInSuperRow']!=None and cfg['DataInSuperRow']=='1'):
        wl_look_super.set(1)
    else:
        wl_look_super.set(0)
    WLSuperRowCB = Checkbutton(itemsFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=1,sticky='w')
    wl_look_data = IntVar()
    if('DataInData' in cfg.keys() and cfg['DataInData']!=None and cfg['DataInData']=='1'):
        wl_look_data.set(1)
    else:
        wl_look_data.set(0)
    WLDataCB = Checkbutton(itemsFrame,text="Data",variable = wl_look_data).grid(row=6,column=1,sticky='w')
    if ruleMech == 'Lexical':
        editWhiteList = Button(itemsFrame,text="Edit Sem/Lexical Cue List",command=lambda:WhiteListWindowEdit(project_name,rule_name)).grid(row=8,column=0,sticky='w')
    else:
        editWhiteList = Button(itemsFrame,text="Edit Semantic Cue List",command=lambda:SemanticListWindowEdit(project_name,rule_name)).grid(row=8,column=0,sticky='w')
    if ruleType != "String":
        SyntacticRules = Button(itemsFrame,text="Edit Syntactic rules",command=lambda:MakeChangesToSyntacticRules(project_name,rule_name)).grid(row=9,column=0,sticky='w')
    #editBlackList = Button(itemsFrame,text="Edit Black Cue List",command=lambda:BlackListWindowEdit(project_name,rule_name)).grid(row=2,column=0,sticky='w')
    text_of_where_to_look = StringVar()
    
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    prags = db.GetPragmaticClasses()
    prags.insert(0,"Any")
    pragVar = StringVar()
    pragVar.set(cfg['PragClass'])
    
    if ruleType == 'Numeric' or ruleType == 'Categorical':
        vDefUnit.set(cfg['DefUnit'])
        vPosUnit.set(cfg['PosUnit'])
    vClsIn.set(cfg['Class'])
    PragLabel = Label(itemsFrame,text="Table type (pragmatics)").grid(row=7,column=1,sticky='w')
    drop = OptionMenu(itemsFrame,pragVar,*prags)
    drop.grid(row=8,column=1,sticky='w')
    save = Button(itemsFrame, text="Save", fg="black",command=lambda:SaveRuleEdit(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,ruleType,ruleMech,wl_look_head,wl_look_stub,wl_look_super,wl_look_data)).grid(row=9,column=1,sticky='w')