'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import Tix
import QueryDBClass
import FileManipulationHelper
def SaveBlackList(listAA,BlackListWindow):
    global currentBlackList
    currentBlackList = []
    currentBlackList = listAA.split('\n')
    BlackListWindow.withdraw()

def BlackListWindow(project_name,rule_name):
    BlackListWindow =Tix.Toplevel()
    BlackListWindow.title("Edit Black List")
    BlackListWindow.geometry('{}x{}'.format(450, 250))
    itemsFrame = Tix.Frame(BlackListWindow)
    itemsFrame.pack()
    namerule_label = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=0,sticky='w')
    list = Tix.Text(itemsFrame,height=10,width=50)
    list.grid(row=1,sticky='w')
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveBlackList(list.get("1.0",Tix.END),BlackListWindow)).grid(row=2,sticky='w')
    
def SemanticListWindow(project_name,rule_name):#
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Tix.Frame(WhiteListWindow)
    itemsFrame.pack(side=Tix.LEFT)
    choiseFrame = Tix.Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=Tix.RIGHT)
    #type = ['WhiteList','BlackList']
    typeVar = Tix.StringVar()
    #typeVar.set(type[0])
    #TypeLabel = Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    #drop = OptionMenu(choiseFrame,typeVar,*type)
    #drop.grid(row=1,column=0,sticky='w')
    where_to_look = Tix.Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = Tix.IntVar()
    HeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = Tix.IntVar()
    StubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = Tix.IntVar()
    SuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = Tix.IntVar()
    DataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = Tix.IntVar()
    EverywhereCB = Tix.Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    whitelist = Tix.CheckList(itemsFrame,width=350)
    whitelist.grid(row=1,sticky='w')
    createSemanticWhiteList(whitelist)
    whitelist.autosetmode()
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=2,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=5,width=50)
    blacklist.grid(row=3,sticky='w')
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(whitelist.get("1.0",Tix.END),blacklist.get("1.0",Tix.END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=4,sticky='w')

    pass

def createSemanticWhiteList(whitelist):
    list = []
    
    list.append("Physical Object")
    list.append("Physical Object.Organism")
    list.append("Physical Object.Organism.Plant")
    list.append("Physical Object.Organism.Fungus")
    list.append("Physical Object.Organism.Virus")
    list.append("Physical Object.Organism.Bacterium")
    
    list.append("Physical Object.Organism.Archaeon")
    list.append("Physical Object.Organism.Eukaryote")
    list.append("Physical Object.Organism.Eukaryote.Animal")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Amphibian")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Bird")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Fish")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Reptile")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Mammal")
    list.append("Physical Object.Organism.Eukaryote.Animal.Vertebrate.Mammal.Human")
    
    for item in list:
        print item
        whitelist.hlist.add(item,text = item.split('.')[-1])
        whitelist.setstatus(item,"off")

       

#def selectItem(whitelist,item):
#    print item, whitelist.getstatus(item)

def WhiteListWindow(project_name,rule_name):
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Tix.Frame(WhiteListWindow)
    itemsFrame.pack(side=Tix.LEFT)
    choiseFrame = Tix.Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=Tix.RIGHT)
    #type = ['WhiteList','BlackList']
    typeVar = Tix.StringVar()
    #typeVar.set(type[0])
    #TypeLabel = Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    #drop = OptionMenu(choiseFrame,typeVar,*type)
    #drop.grid(row=1,column=0,sticky='w')
    where_to_look = Tix.Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = Tix.IntVar()
    HeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = Tix.IntVar()
    StubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = Tix.IntVar()
    SuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = Tix.IntVar()
    DataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = Tix.IntVar()
    EverywhereCB = Tix.Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    whitelist = Tix.Text(itemsFrame,height=5,width=50)
    whitelist.grid(row=1,sticky='w')
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=2,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=5,width=50)
    blacklist.grid(row=3,sticky='w')
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(whitelist.get("1.0",Tix.END),blacklist.get("1.0",Tix.END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=4,sticky='w')

    
def WhiteListWindowEdit(project_name,rule_name):
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit White Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 250))
    itemsFrame = Tix.Frame(WhiteListWindow)
    itemsFrame.pack(side=Tix.LEFT)
    choiseFrame = Tix.Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=Tix.RIGHT)
    type = ['WhiteList','BlackList']
    typeVar = Tix.StringVar()
    typeVar.set(type[0])
    TypeLabel = Tix.Label(choiseFrame,text="ListType").grid(row=0,column=0,sticky='w')
    drop = Tix.OptionMenu(choiseFrame,typeVar,*type)
    drop.grid(row=1,column=0,sticky='w')
    where_to_look = Tix.Label(choiseFrame,text="Where to look?").grid(row=2,column=0,sticky='w')
    look_head = Tix.IntVar()
    HeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = look_head).grid(row=3,column=0,sticky='w')
    look_stub = Tix.IntVar()
    StubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = look_stub).grid(row=4,column=0,sticky='w')
    look_super = Tix.IntVar()
    SuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = look_super).grid(row=5,column=0,sticky='w')
    look_data = Tix.IntVar()
    DataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = look_data).grid(row=6,column=0,sticky='w')
    look_all = Tix.IntVar()
    EverywhereCB = Tix.Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=10,width=50)
    list = Tix.Text(itemsFrame,height=10,width=50)
    list.grid(row=1,sticky='w')
    whitelist = FileManipulationHelper.loadWhiteList(project_name, rule_name)
    i = 1
    afterWordList = False
    for w in whitelist:
        w = w.replace('\n','')
        splitted = w.split(':')
        if splitted[0]=='Type':
            if splitted[1]=='WhiteList':
                typeVar.set(type[0])
            else:
                typeVar.set(type[1])
        if splitted[0]=='Header':
            look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            look_data.set(int(splitted[1]))
        if splitted[0]=='All':
            look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            list.insert(str(i)+'.0',w+'\n')
            i=i+1
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(list.get("1.0",Tix.END),blacklist.get("1.0",Tix.END),typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name)).grid(row=2,sticky='w')



def SaveWhiteList(listWL,listBL,typeVar,look_head,look_stub,look_super,look_data,look_all,WhiteListWindow,project_name,rule_name):
    global currentWhiteList
    global currentBlackList
    currentWhiteList = []
    currentBlackList = []
    currentWhiteList = listWL.split('\n')
    currentBlackList = listBL.split('\n')
    rule_path = "Projects/"+project_name+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.SaveCueList(rule_path,rule_name, currentWhiteList,currentBlackList,typeVar,look_head,look_stub,look_super,look_data,look_all)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()