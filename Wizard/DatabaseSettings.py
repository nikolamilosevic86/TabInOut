'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from Tkinter import *
import FileManipulationHelper
import QueryDBClass


def ClearDBTables(project_name):
    dbSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    query = QueryDBClass.QueryDBCalss(dbSettings['Host'],dbSettings['User'],dbSettings['Pass'],dbSettings['Database'])
    query.ClearCreatedTables()
    query.CreateAdditionalTables()

def ConfigureDatabaseScreen(project_name):
    DataConfig = Toplevel()
    db_host = ""
    db_port = ""
    db_user = ""
    db_pass = ""
    db_database = ""
    with open("Projects/"+project_name+"/"+"Config.cfg") as f:
        content = f.readlines()
    for line in content:
        split = line.split(":")
        split[0] = split[0].replace('\n','')
        split[1] = split[1].replace('\n','')
        if(split[0]=="Host"):
            db_host = split[1]
        if(split[0]=="Port"):
            db_port = split[1]
        if(split[0]=="User"):
            db_user = split[1]
        if(split[0]=="Pass"):
            db_pass = split[1]
        if(split[0]=="Database"):
            db_database = split[1]
    DataConfig.title("Database configuration")
    Host = Label(DataConfig,text="Host Name").grid(row=0,column=0,sticky='w')
    vHost = StringVar()
    HostName = Entry(DataConfig,textvariable=vHost).grid(row=0,column=1,sticky='w')
    vHost.set(db_host)
    
    Port = Label(DataConfig,text="Port Name").grid(row=1,column=0,sticky='w')
    vPort = StringVar()
    PortName = Entry(DataConfig,textvariable=vPort).grid(row=1,column=1,sticky='w')
    vPort.set(db_port)
    User = Label(DataConfig,text="User Name").grid(row=2,column=0,sticky='w')
    vUser = StringVar()
    UserName = Entry(DataConfig,textvariable=vUser).grid(row=2,column=1,sticky='w')
    vUser.set(db_user)
    Pass = Label(DataConfig,text="Password").grid(row=3,column=0,sticky='w')
    vPass = StringVar()
    PassName = Entry(DataConfig,show="*",textvariable=vPass).grid(row=3,column=1,sticky='w')
    vPass.set(db_pass)
    Database = Label(DataConfig,text="Database Name").grid(row=4,column=0,sticky='w')
    vDatabase = StringVar()
    DatabaseName = Entry(DataConfig,textvariable=vDatabase).grid(row=4,column=1,sticky='w')
    vDatabase.set(db_database)
    Save = Button(DataConfig, text="Save", bg="green",command=lambda: SaveDBSettings(vHost,vPort,vUser,vPass,vDatabase,DataConfig,project_name)).grid(row=5,column=1,sticky='w')
    
def SaveDBSettings(HostName,PortName,UserName,PassName,DatabaseName,DataConfig,project_name):
    
    hostname = HostName.get()
    portname = PortName.get()
    username = UserName.get()
    passname = PassName.get()
    database = DatabaseName.get()
    DataConfig.withdraw()
    FileManipulationHelper.SaveToConfigFile(project_name,hostname,portname,username,passname,database)
    pass
