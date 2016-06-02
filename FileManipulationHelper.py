'''
Created on 2 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import os
from os import listdir
from os.path import isfile, join
def CreateFoderIfNotExist(FolderName):
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)

def CreateFolderStructure():
    CreateFoderIfNotExist("Projects")
    

def readProjects():
    projects = [os.path.join("",o) for o in os.listdir("Projects") if os.path.isdir(os.path.join("Projects",o))]
    return projects

def CreateProjectCfgFileIfNotExist(Folder):
    if not os.path.exists(Folder+"/Config.cfg"):
        f = open(Folder+"/Config.cfg",'w')
        f.write('Host:127.0.0.1\n') # python will convert \n to os.linesep
        f.write('Port:3306\n')
        f.write('User:root\n')
        f.write('Pass:')
        f.close() # you can omit in most cases as the destructor will call it
        
#CreateFolderStructure()
#print readProjects()
