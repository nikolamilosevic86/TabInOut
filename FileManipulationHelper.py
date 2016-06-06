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
        f.write('Pass:\n')
        f.write('Database:table_db')
        f.close() # you can omit in most cases as the destructor will call it

def SaveToConfigFile(project_name,hostname,port,user,pasword,database):
    f = open("Projects/"+project_name+"/Config.cfg",'w')
    f.write('Host:'+hostname+'\n') # python will convert \n to os.linesep
    f.write('Port:'+port+'\n')
    f.write('User:'+user+'\n')
    f.write('Pass:'+pasword+'\n')
    f.write('Database:'+database+'\n')
    f.close()

def SaveWhiteList(rule_path,whitelist):
    f = open(rule_path+'/WhiteList.lst','w')
    for item in whitelist:
        f.write(item+'\n')
    f.close
def SaveBlackList(rule_path,blakclist):
    f = open(rule_path+'/BlackList.lst','w')
    for item in blakclist:
        f.write(item+'\n')
    f.close
def MakeRuleCFGFile(rule_path,look_head,look_stub,look_super,look_data,look_all):
    f = open(rule_path+'/Rule.cfg','w')
    f.write('Header:'+str(look_head.get())+'\n')
    f.write('Stub:'+str(look_stub.get())+'\n')
    f.write('Super-row:'+str(look_super.get())+'\n')
    f.write('Data:'+str(look_data.get())+'\n')
    f.write('All:'+str(look_all.get())+'\n')
    f.close()

def loadRules(project_name):
    project_folder = 'Projects/'+project_name+'/'
    projects = [os.path.join("",o) for o in os.listdir(project_folder) if os.path.isdir(os.path.join(project_folder,o))]
    return projects
    
def loadWhiteList(project_name,rule_name):
    Rule_path = "Projects/"+project_name+'/'+rule_name+'/WhiteList.lst'
    f = open(Rule_path,'r')
    whitelist = f.readlines()
    return whitelist
def loadBlackList(project_name,rule_name):
    Rule_path = "Projects/"+project_name+'/'+rule_name+'/BlackList.lst'
    f = open(Rule_path,'r')
    blacklist = f.readlines()
    return blacklist
def loadRuleConfig(project_name,rule_name):
    Rule_path = "Projects/"+project_name+'/'+rule_name+'/Rule.cfg'
    f = open(Rule_path,'r')
    config = f.readlines()
    conf = {}
    for cfg in config:
        sp = cfg.split(':')
        if sp[0]=='Header':
            conf['Header']=sp[1]
        if sp[0]=='Stub':
            conf['Stub']=sp[1]
        if sp[0]=='Super-row':
            conf['Super-row']=sp[1]
        if sp[0]=='Data':
            conf['Data']=sp[1]
        if sp[0]=='All':
            conf['All']=sp[1]
    return conf

def LoadRules(path):
    f = open(path,'r')
    rules = f.readlines()
    return rules

            
    

        
#CreateFolderStructure()
#print readProjects()
