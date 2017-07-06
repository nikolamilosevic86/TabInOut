'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import shutil 
from Tkinter import *
import FileManipulationHelper

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

def RemoveRule(Lb1,project_name):
    try:
        # get selected line index
        index = Lb1.selection()[0]
        rule = Lb1.item(index)
        variable = Lb1.parent(index)
        shutil.rmtree('Projects/'+project_name+'/'+variable+'/'+rule['text'])
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
    
def SetRuleName(project_name,RulesListBox):
    RuleNameView = Toplevel()
    RuleNameView.title("Set variable name")
    RuleNameLabel = Label(RuleNameView,text="Name of the variable").grid(row=0,sticky='w')
    vRuleName = StringVar()
    RuleNameEntry = Entry(RuleNameView,textvariable=vRuleName).grid(row=1,sticky='w')
    vRuleType = StringVar()
    RuleNameLabel = Label(RuleNameView,text="Value type of the variable").grid(row=2,sticky='w')
    vRuleType.set("Numeric")
    Radiobutton(RuleNameView, text="Numeric", variable=vRuleType, value="Numeric").grid(row=3,sticky='w')
    Radiobutton(RuleNameView, text="Categorical", variable=vRuleType, value="Categorical").grid(row=4,sticky='w')
    Radiobutton(RuleNameView, text="String", variable=vRuleType, value="String").grid(row=5,sticky='w')
    RuleNameButton = Button(RuleNameView,text="Next ->>",command=lambda:AddEditVariable(project_name,vRuleName,vRuleType,RuleNameView,RulesListBox)).grid(row=6,sticky='w')

def AddEditVariable(project_name,vRuleName,vRuleType,RuleNameView,RulesListBox):
    RuleNameView.withdraw()
    rule_path = "Projects/" + project_name + "/" + vRuleName.get().replace('\n', '')
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    f = open(rule_path +'/var_config.cfg', 'w')
    f.write("VariableName:" + str(vRuleName.get().replace('\n', '')) + '\n')
    f.write("VariableType:" + str(vRuleType.get().replace('\n', '')) + '\n')
    f.close()
    RulesListBox.insert('', 'end', vRuleName.get(), text=vRuleName.get())

def loadVariableConfig(project_name,variable_name):
    Rule_path = "Projects/"+project_name+'/'+variable_name+'/var_config.cfg'
    f = open(Rule_path,'r')
    config = f.readlines()
    conf = {}
    for cfg in config:
        sp = cfg.split(':')
        if sp[0]=='VariableName':
            conf['VariableName']=sp[1].replace('\n','')
        if sp[0]=='VariableType':
            conf['VariableType']=sp[1].replace('\n','')
    return conf

    

def AddVariable(project_name,RulesListBox):
    SetRuleName(project_name,RulesListBox)



