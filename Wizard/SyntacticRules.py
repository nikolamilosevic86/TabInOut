'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import FileManipulationHelper
import Tkconstants, tkFileDialog
from tkFileDialog import askopenfile

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
    try:
        extracted = IntVar()
        extracted.set(0)
    except:
        print "Exception occured on that IntVAR in ProcessDataV method"
    Process_Data.ProcessDataBase(project_name,processing_rules)
    
    
########################################
#                                      #
#   Frames for setting up the rules    #
#                                      #
########################################
def LoadRulesCfGMainScreen(project_name,rule_name,variable_name):

    #SetLexRules.withdraw()
    #top.protocol("WM_DELETE_WINDOW", on_closing)
    processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name,True)
    #for rule in processing_rules:
        #if rule.RuleName == rule_name:
            #if(rule.RuleType == "Categorical"):
                #skip_val = IntVar()
                #skip_val.set(0)
                #return
    top = Toplevel()
    top.title("Set up rules")
    top.geometry('{}x{}'.format(500, 300))
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
    fname = StringVar()
    label_fname = Label(frame, textvariable=fname)
    fname.set("FileName")
    label_fname.grid(row=1, column=0, sticky='w')
    LoadFile = Button(frame, text='Open', command=lambda:askopenfilename(fname))
    LoadFile.grid(row=1,column=1,sticky='w')
    Next = Button(bottomframe, text="Next", bg="green",command = lambda:EditSintacticRules(project_name,rule_name, top,fname,variable_name))
    Next.pack( side = LEFT)
    pass

def askopenfilename(var):
    filename = tkFileDialog.askopenfilename(filetypes=[("Syntactic rules","")],initialdir=[('DefaultSintacticRules')])
    var.set(filename)
    return filename

def EditSintacticRules(project_name,rule_name, ChoseSintRulesWindow,fname,variable_name):
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

    if fname.get()=='':
        SaveSintacticRules(rulelist.get("1.0",END),top,project_name,variable_name)
        return
    else:
        fpaths.append(fname.get())
    rules = []
    for path in fpaths:
        rules = rules + FileManipulationHelper.LoadRules(path)

    i = 1
    for w in rules:
        rulelist.insert(str(i)+'.0',w)
        i=i+1
    saveButton = Button(frame,text="Next",bg="green",fg="black",command=lambda:SaveSintacticRules(rulelist.get("1.0",END),top,project_name,rule_name,variable_name)).grid(row=2,sticky='w')
    pass

def MakeChangesToSyntacticRules(project_name,rule_name,variable_name):
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
    rules = []
    path = 'Projects/'+project_name+'/'+variable_name+'/'+rule_name+'/'+'SyntacticRules.sin'
    rules = FileManipulationHelper.LoadRules(path)
        
    i = 1
    for w in rules:
        rulelist.insert(str(i)+'.0',w)
        i=i+1
    skip_val = IntVar()
    skip_val.set(0)
    saveButton = Button(frame,text="Next",bg="green",fg="black",command=lambda:SaveSintacticRules(rulelist.get("1.0",END),top,project_name,rule_name,variable_name)).grid(row=2,sticky='w')
    pass


# Syntactic rules
def SaveSintacticRules(rules, window,project_name,rule_name,variable_name):
    global lab2
    
    window.withdraw()
    #top = Toplevel()
    get_rules = FileManipulationHelper.loadRules(project_name,variable_name)
    rule_path = 'Projects/'+variable_name+'/'+project_name+'/'+rule_name
    FileManipulationHelper.SaveSyntacticRules(rules,project_name,rule_name,variable_name)
    #processing_rules = RuleClasses_LoadRulesForProcessingClass.LoadRulesForProcessing(project_name)
    #top.protocol("WM_DELETE_WINDOW", on_closing)

    