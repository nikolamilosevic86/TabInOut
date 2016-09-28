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