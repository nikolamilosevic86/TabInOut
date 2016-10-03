'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import QueryDBClass
import FileManipulationHelper
from BlackAndWhiteList import WhiteListWindow,WhiteListWindowEdit,SemanticListWindow

def AddEditRule(project_name,vRuleName,vRuleType,RuleNameView,RulesListBox):
    global currentWhiteList
    global currentBlackList
    currentWhiteList = []
    currentBlackList = []
    
    RuleNameView.withdraw()
    add = Toplevel()
    #add.protocol("WM_DELETE_WINDOW", on_closing)
    add.title("Add Rule")
    add.geometry('{}x{}'.format(400, 350))
    itemsFrame = Frame(add,height=130)
    itemsFrame.pack()
    namerule_label = Label(itemsFrame,text="Name of the rule").grid(row=0,column=0,sticky='w')
    rulename_entry = Entry(itemsFrame,textvariable=vRuleName,state=DISABLED).grid(row=0,column=1,sticky='w')
    rule_name = vRuleName.get()
    #editCueList = Button(itemsFrame,text="Edit Cue List",command=lambda:WhiteListWindow(project_name,rule_name)).grid(row=1,column=0,sticky='w')
    ClassLabel = Label(itemsFrame,text="Class name of result").grid(row=3,column=0,sticky='w')
    vClsIn = StringVar()
    ClassInput = Entry(itemsFrame,textvariable=vClsIn).grid(row=4,sticky='w')
    vDefUnit = StringVar()
    vPosUnit = StringVar()
    if(vRuleType.get() == "Numeric"):
        DefUnitLabel = Label(itemsFrame,text="Default unit").grid(row=5,column=0,sticky='w')
        DefUnInput = Entry(itemsFrame,textvariable=vDefUnit).grid(row=6,sticky='w')
        PosUnitLabel = Label(itemsFrame,text="Possible units (comma separated)").grid(row=7,column=0,sticky='w')    
        PosUnInput = Entry(itemsFrame,textvariable=vPosUnit).grid(row=8,sticky='w')
    if(vRuleType.get() == "Categorical"):
        PosUnitLabel = Label(itemsFrame,text="Possible categories (comma separated)").grid(row=7,column=0,sticky='w')
        vPosUnit = StringVar()
        PosUnInput = Entry(itemsFrame,textvariable=vPosUnit).grid(row=8,sticky='w')
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    prags = db.GetPragmaticClasses()
    pragVar = StringVar()
    pragVar.set(prags[0])
    PragLabel = Label(itemsFrame,text="Pragmatic class").grid(row=9,column=0,sticky='w')
    drop = OptionMenu(itemsFrame,pragVar,*prags)
    drop.grid(row=10,column=0,sticky='w')
    vLexSemRule = StringVar()
    vLexSemRule.set("Lexical")
    PosUnitLabel = Label(itemsFrame,text="Select rule creation mechanism").grid(row=11,column=0,sticky='w')
    Radiobutton(itemsFrame, text="Lexical (White List+Black list)", variable=vLexSemRule, value="Lexical").grid(row=12,sticky='w')
    Radiobutton(itemsFrame, text="Semantic (UMLS Sem. type+Black list)", variable=vLexSemRule, value="Semantic").grid(row=13,sticky='w')
    save = Button(itemsFrame, text="Save", fg="black",command=lambda:SaveRule(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox,vRuleType,vLexSemRule)).grid(row=14,column=1,sticky='w')
    

def SaveRuleEdit(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.MakeRuleCFGFile(rule_path, vClsIn,vDefUnit,vPosUnit,pragVar) 
    add.withdraw()  

def SaveRule(project_name,rule_name,add,vClsIn,vDefUnit,vPosUnit,pragVar,RulesListBox,vRuleType,vLexSemRule):
    global currentWhiteList
    global currentBlackList
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    #FileManipulationHelper.SaveWhiteList(rule_path, currentWhiteList)
    #FileManipulationHelper.SaveBlackList(rule_path, currentBlackList)
    FileManipulationHelper.MakeRuleCFGFile(rule_path,vClsIn,vDefUnit,vPosUnit,pragVar,vRuleType,vLexSemRule) 
    RulesListBox.insert(RulesListBox.size(),rule_name)
    add.withdraw() 
    if(vLexSemRule.get()=="Lexical"):
        WhiteListWindow(project_name,rule_name)  
    if(vLexSemRule.get()=="Semantic"):
        SemanticListWindow(project_name,rule_name)


    
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
    #editBlackList = Button(itemsFrame,text="Edit Black Cue List",command=lambda:BlackListWindowEdit(project_name,rule_name)).grid(row=2,column=0,sticky='w')
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