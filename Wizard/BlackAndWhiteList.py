'''
Created on 28 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import Tix
import QueryDBClass
import FileManipulationHelper
from SyntacticRules import LoadRulesCfGMainScreen

global semanticTypes
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
    
def SemanticListWindow(project_name,rule_name,vClsIn):#

    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 400))
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
    where_to_look = Tix.Label(choiseFrame,text="Where to look for white list variables?").grid(row=2,column=0,sticky='w')
    wl_look_head = Tix.IntVar()
    WLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = wl_look_head).grid(row=3,column=0,sticky='w')
    wl_look_stub = Tix.IntVar()
    WLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=0,sticky='w')
    wl_look_super = Tix.IntVar()
    WLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=0,sticky='w')
    wl_look_data = Tix.IntVar()
    WLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = wl_look_data).grid(row=6,column=0,sticky='w')
    
    where_to_look2 = Tix.Label(choiseFrame,text="Where to look for black list variables?").grid(row=7,column=0,sticky='w')
    bl_look_head = Tix.IntVar()
    BLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = bl_look_head).grid(row=8,column=0,sticky='w')
    bl_look_stub = Tix.IntVar()
    BLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = bl_look_stub).grid(row=9,column=0,sticky='w')
    bl_look_super = Tix.IntVar()
    BLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = bl_look_super).grid(row=10,column=0,sticky='w')
    bl_look_data = Tix.IntVar()
    BLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = bl_look_data).grid(row=11,column=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    whitelist = Tix.CheckList(itemsFrame,width=350)
    whitelist.grid(row=1,sticky='w')
    createSemanticWhiteList(whitelist)
    whitelist.autosetmode()
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=2,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=5,width=50)
    blacklist.grid(row=3,sticky='w')
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteListSemantic(whitelist,blacklist.get("1.0",Tix.END),typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn)).grid(row=4,sticky='w')

    pass

def createSemanticWhiteList(whitelist):
    global semanticTypes
    list = ["Physical Object","Physical Object.Organism","Physical Object.Organism.Plant","Physical Object.Organism.Fungus","Physical Object.Organism.Virus","Physical Object.Organism.Bacterium",
    "Physical Object.Organism.Archaeon","Physical Object.Organism.Eukaryote","Physical Object.Organism.Eukaryote.Animal","Physical Object.Organism.Eukaryote.Animal.Vertebrate","Physical Object.Organism.Eukaryote.Animal.Vertebrate.Amphibian",
    "Physical Object.Organism.Eukaryote.Animal.Vertebrate.Bird","Physical Object.Organism.Eukaryote.Animal.Vertebrate.Fish","Physical Object.Organism.Eukaryote.Animal.Vertebrate.Reptile",
    "Physical Object.Organism.Eukaryote.Animal.Vertebrate.Mammal","Physical Object.Organism.Eukaryote.Animal.Vertebrate.Mammal.Human","Physical Object.Anatomical Structure",
    "Physical Object.Anatomical Structure.Embryonic Structure","Physical Object.Anatomical Structure.Anatomical Abnormality","Physical Object.Anatomical Structure.Anatomical Abnormality.Congenital Abnormality",
    "Physical Object.Anatomical Structure.Anatomical Abnormality.Acquired Abnormality","Physical Object.Anatomical Structure.Fully Formed Anatomical Structure","Physical Object.Anatomical Structure.Fully Formed Anatomical Structure.Body Part, Organ, or Organ Component",
    "Physical Object.Anatomical Structure.Fully Formed Anatomical Structure.Tissue","Physical Object.Anatomical Structure.Fully Formed Anatomical Structure.Cell","Physical Object.Anatomical Structure.Fully Formed Anatomical Structure.Cell Component",
    "Physical Object.Anatomical Structure.Fully Formed Anatomical Structure.Gene or Genome","Physical Object.Manufactured Object","Physical Object.Manufactured Object.Medical Device",
    "Physical Object.Manufactured Object.Medical Device.Drug Delivery Device","Physical Object.Manufactured Object.Research Device","Physical Object.Manufactured Object.Clinical Drug",
    "Physical Object.Substance","Physical Object.Substance.Chemical","Physical Object.Substance.Chemical.Chemical Viewed Functionally","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Pharmacologic Substance",
    "Physical Object.Substance.Chemical.Chemical Viewed Functionally.Pharmacologic Substance.Antibiotic","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biomedical or Dental Material",
    "Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance.Hormone",
    "Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance.Enzyme","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance.Vitamin",
    "Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance.Immunologic Factor","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Biologically Active Substance.Receptor",
    "Physical Object.Substance.Chemical.Chemical Viewed Functionally.Indicator, Reagent, or Diagnostic Acid","Physical Object.Substance.Chemical.Chemical Viewed Functionally.Hazardous or Poisonous Substance",
    "Physical Object.Substance.Chemical.Chemical Viewed Structurally","Physical Object.Substance.Chemical.Chemical Viewed Structurally.Organic Chemical","Physical Object.Substance.Chemical.Chemical Viewed Structurally.Organic Chemical.Nucleic Acid, Nucleoside, or Nucleotide",
    "Physical Object.Substance.Chemical.Chemical Viewed Structurally.Organic Chemical.Amino Acid, Peptide, or Protein","Physical Object.Substance.Chemical.Chemical Viewed Structurally.Inorganic Chemical",
    "Physical Object.Substance.Chemical.Chemical Viewed Structurally.Element, Ion, or Isotope","Physical Object.Substance.Body Substance","Physical Object.Substance.Food","Conceptual Entity","Conceptual Entity.Idea or Concept",
    "Conceptual Entity.Idea or Concept.Temporal Concept","Conceptual Entity.Idea or Concept.Qualitative Concept","Conceptual Entity.Idea or Concept.Quantitative Concept","Conceptual Entity.Idea or Concept.Functional Concept",
    "Conceptual Entity.Idea or Concept.Functional Concept.Body System","Conceptual Entity.Idea or Concept.Spatial Concept","Conceptual Entity.Idea or Concept.Spatial Concept.Body Space or Junction",
    "Conceptual Entity.Idea or Concept.Spatial Concept.Body Location or Region","Conceptual Entity.Idea or Concept.Spatial Concept.Molecular Sequence","Conceptual Entity.Idea or Concept.Spatial Concept.Molecular Sequence.Nucleotide Sequence",
    "Conceptual Entity.Idea or Concept.Spatial Concept.Molecular Sequence.Amino Acid Sequence","Conceptual Entity.Idea or Concept.Spatial Concept.Molecular Sequence.Carbohydrate Sequence",
    "Conceptual Entity.Idea or Concept.Spatial Concept.Geographic Area","Conceptual Entity.Finding","Conceptual Entity.Finding.Laboratory or Test Result","Conceptual Entity.Finding.Sign or Symptom",
    "Conceptual Entity.Organism Attribute","Conceptual Entity.Organism Attribute.Clinical Attribute","Conceptual Entity.Intellectual Product","Conceptual Entity.Intellectual Product.Classification",
    "Conceptual Entity.Intellectual Product.Regulation or Law","Conceptual Entity.Language","Conceptual Entity.Occupation or Discipline","Conceptual Entity.Occupation or Discipline.Biomedical Occupation or Discipline",
    "Conceptual Entity.Organization","Conceptual Entity.Organization.Health Care Related Organization","Conceptual Entity.Organization.Professional Society","Conceptual Entity.Organization.Self-help or Relief Organization",
    "Conceptual Entity.Group Attribute","Conceptual Entity.Group","Conceptual Entity.Group.Professional or Occupational Group","Conceptual Entity.Group.Population Group","Conceptual Entity.Group.Family Group",
    "Conceptual Entity.Group.Age Group","Conceptual Entity.Group.Patient or Disabled Group","Activity","Activity.Behavior","Activity.Behavior.Social Behavior","Activity.Behavior.Individual Behavior",
    "Activity.Daily or Recreational Activity","Activity.Occupational Activity","Activity.Occupational Activity.Health Care Activity","Activity.Occupational Activity.Health Care Activity.Laboratory Procedure",
    "Activity.Occupational Activity.Health Care Activity.Diagnostic Procedure","Activity.Occupational Activity.Health Care Activity.Therapeutic or Preventive Procedure","Activity.Occupational Activity.Research Activity",
    "Activity.Occupational Activity.Research Activity.Molecular Biology Research Technique","Activity.Occupational Activity.Governmental or Regulatory Activity","Activity.Occupational Activity.Educational Activity",
    "Activity.Machine Activity","Phenomenon or Process","Phenomenon or Process.Human-caused Phenomenon or Process","Phenomenon or Process.Human-caused Phenomenon or Process.Environmental Effect of Humans",
    "Phenomenon or Process.Natural Phenomenon or Process","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Organism Function","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Organism Function.Mental Process",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Organ or Tissue Function","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Cell Function",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Molecular Function",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Physiologic Function.Molecular Function.Genetic Function","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function.Disease or Syndrome","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function.Disease or Syndrome.Mental or Behavioral Dysfunction",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function.Disease or Syndrome.Neoplastic Process","Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function.Cell or Molecular Dysfunction",
    "Phenomenon or Process.Natural Phenomenon or Process.Biologic Function.Pathologic Function.Experimental Model of Disease","Phenomenon or Process. Injury or Poisoning"
    ]
    semanticTypes = list
    for item in list:
        print item
        whitelist.hlist.add(item,text = item.split('.')[-1])
        whitelist.setstatus(item,"off")

def SemanticListWindowEdit(project_name,rule_name,variable_name):#
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 400))
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
    where_to_look = Tix.Label(choiseFrame,text="Where to look for white list variables?").grid(row=2,column=0,sticky='w')
    wl_look_head = Tix.IntVar()
    WLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = wl_look_head).grid(row=3,column=0,sticky='w')
    wl_look_stub = Tix.IntVar()
    WLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=0,sticky='w')
    wl_look_super = Tix.IntVar()
    WLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=0,sticky='w')
    wl_look_data = Tix.IntVar()
    WLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = wl_look_data).grid(row=6,column=0,sticky='w')
    
    where_to_look2 = Tix.Label(choiseFrame,text="Where to look for black list variables?").grid(row=7,column=0,sticky='w')
    bl_look_head = Tix.IntVar()
    BLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = bl_look_head).grid(row=8,column=0,sticky='w')
    bl_look_stub = Tix.IntVar()
    BLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = bl_look_stub).grid(row=9,column=0,sticky='w')
    bl_look_super = Tix.IntVar()
    BLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = bl_look_super).grid(row=10,column=0,sticky='w')
    bl_look_data = Tix.IntVar()
    BLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = bl_look_data).grid(row=11,column=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=0,sticky='w')
    whitelist = Tix.CheckList(itemsFrame,width=350)
    whitelist.grid(row=1,sticky='w')
    createSemanticWhiteList(whitelist)
    whitelist.autosetmode()
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=2,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=5,width=50)
    blacklist.grid(row=3,sticky='w')
    
    
    whitelist_list = FileManipulationHelper.loadWhiteList(project_name, rule_name,variable_name)
    blacklist_list = FileManipulationHelper.loadBlackList(project_name, rule_name,variable_name)
    
    
    i = 1
    afterWordList = False
    for w in whitelist_list:
        w = w.replace('\n','')
        splitted = w.split(':')
        #if splitted[0]=='Type':
        #    if splitted[1]=='WhiteList':
        #        typeVar.set(type[0])
        #    else:
        #        typeVar.set(type[1])
        if splitted[0]=='Header':
            wl_look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            wl_look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            wl_look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            wl_look_data.set(int(splitted[1]))
        #if splitted[0]=='All':
        #    look_all.set(int(splitted[1]))
        if w == "SemanticTypes:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            cur = 0
            for item in semanticTypes:
                if(w == item.split('.')[-1]):
                    whitelist.setstatus(item,"on")
                cur = cur + 1
            i=i+1
                    
        
    afterWordList = False
    for w in blacklist_list:
        w = w.replace('\n','')
        splitted = w.split(':')
        #if splitted[0]=='Type':
        #    if splitted[1]=='WhiteList':
        #        typeVar.set(type[0])
        #    else:
        #        typeVar.set(type[1])
        if splitted[0]=='Header':
            bl_look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            bl_look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            bl_look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            bl_look_data.set(int(splitted[1]))
        #if splitted[0]=='All':
        #    look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            blacklist.insert(str(i)+'.0',w+'\n')
            i=i+1
    
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteListSemanticEdit(whitelist,blacklist.get("1.0",Tix.END),typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name)).grid(row=4,sticky='w')

    pass    

#def selectItem(whitelist,item):
#    print item, whitelist.getstatus(item)

def WhiteListWindow(project_name,rule_name,vClsIn):
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 550))
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
    where_to_look = Tix.Label(choiseFrame,text="Where to look for white list cues?").grid(row=2,column=0,sticky='w')
    wl_look_head = Tix.IntVar()
    WLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = wl_look_head).grid(row=3,column=0,sticky='w')
    wl_look_stub = Tix.IntVar()
    WLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=0,sticky='w')
    wl_look_super = Tix.IntVar()
    WLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=0,sticky='w')
    wl_look_data = Tix.IntVar()
    WLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = wl_look_data).grid(row=6,column=0,sticky='w')
    
    where_to_look2 = Tix.Label(choiseFrame,text="Where to look for black list cues?").grid(row=7,column=0,sticky='w')
    bl_look_head = Tix.IntVar()
    BLHeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = bl_look_head).grid(row=8,column=0,sticky='w')
    bl_look_stub = Tix.IntVar()
    BLStubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = bl_look_stub).grid(row=9,column=0,sticky='w')
    bl_look_super = Tix.IntVar()
    BLSuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = bl_look_super).grid(row=10,column=0,sticky='w')
    bl_look_data = Tix.IntVar()
    BLDataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = bl_look_data).grid(row=11,column=0,sticky='w')
    namerule_label2 = Tix.Label(itemsFrame,text="To look for annotations ids (such as CUI from UMLS)\nwrite [annID]: (eg. '[annID]:C1696465'). To look\nfor annotation types (such as Semantic Type\nin UMLS) write [annType]: in front of cue (e.g.\n'[annType]:Biomedical or Dental Materia' or\n'[annType]:(bodm)'). To write just lexical cue,\njust write word, without prefixes, or [word]:\n(e.g. 'age' or '[word]:age')", justify=Tix.LEFT).grid(row=0,sticky='w')
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelist").grid(row=1,sticky='w')
    whitelist = Tix.Text(itemsFrame,height=5,width=50)
    whitelist.grid(row=2,sticky='w')
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklist").grid(row=3,sticky='w')
    blacklist = Tix.Text(itemsFrame,height=5,width=50)
    blacklist.grid(row=4,sticky='w')
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteList(whitelist.get("1.0",Tix.END),blacklist.get("1.0",Tix.END),typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn)).grid(row=5,sticky='w')

    
def WhiteListWindowEdit(project_name,rule_name):
    typeVar =Tix.StringVar() 
    WhiteListWindow =Tix.Toplevel()
    WhiteListWindow.title("Edit White Cue List")
    WhiteListWindow.geometry('{}x{}'.format(550, 550))
    itemsFrame = Tix.Frame(WhiteListWindow)
    itemsFrame.pack(side=Tix.LEFT)
    choiseFrame = Tix.Frame(WhiteListWindow,width=130)
    choiseFrame.pack(side=Tix.RIGHT)
    wl_where_to_look = Tix.Label(choiseFrame,text="Where to look in whitelist?").grid(row=2,column=0,sticky='w')
    wl_look_head = Tix.IntVar()
    wl_HeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = wl_look_head).grid(row=3,column=0,sticky='w')
    wl_look_stub = Tix.IntVar()
    wl_StubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = wl_look_stub).grid(row=4,column=0,sticky='w')
    wl_look_super = Tix.IntVar()
    wl_SuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = wl_look_super).grid(row=5,column=0,sticky='w')
    wl_look_data = Tix.IntVar()
    wl_DataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = wl_look_data).grid(row=6,column=0,sticky='w')
    
    
    bl_where_to_look = Tix.Label(choiseFrame,text="Where to look in blacklist?").grid(row=7,column=0,sticky='w')
    bl_look_head = Tix.IntVar()
    bl_HeaderCB = Tix.Checkbutton(choiseFrame,text="Header",variable = bl_look_head).grid(row=8,column=0,sticky='w')
    bl_look_stub = Tix.IntVar()
    bl_StubCB = Tix.Checkbutton(choiseFrame,text="Stub",variable = bl_look_stub).grid(row=9,column=0,sticky='w')
    bl_look_super = Tix.IntVar()
    bl_SuperRowCB = Tix.Checkbutton(choiseFrame,text="Super-row",variable = bl_look_super).grid(row=10,column=0,sticky='w')
    bl_look_data = Tix.IntVar()
    bl_DataCB = Tix.Checkbutton(choiseFrame,text="Data",variable = bl_look_data).grid(row=11,column=0,sticky='w')
    #look_all = Tix.IntVar()
    #EverywhereCB = Tix.Checkbutton(choiseFrame,text="Everywhere",variable=look_all).grid(row=7,column=0,sticky='w')
    
    namerule_label2 = Tix.Label(itemsFrame,text="To look for annotations ids (such as CUI from UMLS)\nwrite [annID]: (eg. '[annID]:C1696465'). To look\nfor annotation types (such as Semantic Type\nin UMLS) write [annType]: in front of cue (e.g.\n'[annType]:Biomedical or Dental Materia' or\n'[annType]:(bodm)'). To write just lexical cue,\njust write word, without prefixes, or [word]:\n(e.g. 'age' or '[word]:age')", justify=Tix.LEFT).grid(row=0,sticky='w')
    
    namerule_label = Tix.Label(itemsFrame,text="List of terms in whitelsit").grid(row=1,sticky='w')
    WhiteListText = Tix.Text(itemsFrame,height=10,width=50)
    WhiteListText.grid(row=2,sticky='w')
    whitelist = FileManipulationHelper.loadWhiteList(project_name, rule_name)
    
    namerule_label2 = Tix.Label(itemsFrame,text="List of terms in blacklsit").grid(row=3,sticky='w')
    BlackListText = Tix.Text(itemsFrame,height=10,width=50)
    BlackListText.grid(row=4,sticky='w')
    blacklist = FileManipulationHelper.loadBlackList(project_name, rule_name)
    i = 1
    afterWordList = False
    for w in whitelist:
        w = w.replace('\n','')
        splitted = w.split(':')
        #if splitted[0]=='Type':
        #    if splitted[1]=='WhiteList':
        #        typeVar.set(type[0])
        #    else:
        #        typeVar.set(type[1])
        if splitted[0]=='Header':
            wl_look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            wl_look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            wl_look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            wl_look_data.set(int(splitted[1]))
        #if splitted[0]=='All':
        #    look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            WhiteListText.insert(str(i)+'.0',w+'\n')
            i=i+1
            
    afterWordList = False
    for w in blacklist:
        w = w.replace('\n','')
        splitted = w.split(':')
        #if splitted[0]=='Type':
        #    if splitted[1]=='WhiteList':
        #        typeVar.set(type[0])
        #    else:
        #        typeVar.set(type[1])
        if splitted[0]=='Header':
            bl_look_head.set(int(splitted[1]))
        if splitted[0]=='Stub':
            bl_look_stub.set(int(splitted[1]))
        if splitted[0]=='Super-row':
            bl_look_super.set(int(splitted[1]))
        if splitted[0]=='Data':
            bl_look_data.set(int(splitted[1]))
        #if splitted[0]=='All':
        #    look_all.set(int(splitted[1]))
        if w == "WordList:":
            afterWordList = True
            continue
        
        if afterWordList == True:
            BlackListText.insert(str(i)+'.0',w+'\n')
            i=i+1
    saveButton = Tix.Button(itemsFrame,text="Save",fg="black",command=lambda:SaveWhiteListEdit(WhiteListText.get("1.0",Tix.END),BlackListText.get("1.0",Tix.END),typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name)).grid(row=12,column=0,sticky='w')
                            
                                                                                                                       

def SaveWhiteListSemantic(listWL,listBL,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn):
    global currentWhiteList
    global currentBlackList
    global semanticTypes
    selected = []
    for item in semanticTypes:
        if(listWL.getstatus(item)=="on"):
            selected.append(item.split(".")[-1])
    
    currentWhiteList = selected
    currentBlackList = []
    currentBlackList = listBL.split('\n')
    rule_path = "Projects/"+project_name+"/"+vClsIn.get()+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    semType = True
    FileManipulationHelper.SaveCueListSem(rule_path,rule_name, currentWhiteList,currentBlackList,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()
    LoadRulesCfGMainScreen(project_name,rule_name,vClsIn.get())

def SaveWhiteListSemanticEdit(listWL,listBL,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn):
    global currentWhiteList
    global currentBlackList
    global semanticTypes
    selected = []
    for item in semanticTypes:
        if(listWL.getstatus(item)=="on"):
            selected.append(item.split(".")[-1])
    
    currentWhiteList = selected
    currentBlackList = []
    currentBlackList = listBL.split('\n')
    rule_path = "Projects/"+project_name+"/"+vClsIn.get()+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    semType = True
    FileManipulationHelper.SaveCueListSem(rule_path,rule_name, currentWhiteList,currentBlackList,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()

def SaveWhiteList(listWL,listBL,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn):
    global currentWhiteList
    global currentBlackList
    listWL
    currentWhiteList = []
    currentBlackList = []
    currentWhiteList = listWL.split('\n')
    currentBlackList = listBL.split('\n')
    rule_path = "Projects/"+project_name+"/"+vClsIn.get()+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.SaveCueList(rule_path,rule_name, currentWhiteList,currentBlackList,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()
    LoadRulesCfGMainScreen(project_name,rule_name,vClsIn.get())
    
def SaveWhiteListEdit(listWL,listBL,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data,WhiteListWindow,project_name,rule_name,vClsIn):
    global currentWhiteList
    global currentBlackList
    listWL
    currentWhiteList = []
    currentBlackList = []
    currentWhiteList = listWL.split('\n')
    currentBlackList = listBL.split('\n')
    rule_path = "Projects/"+project_name+"/"+vClsIn.get()+"/"+rule_name
    FileManipulationHelper.CreateFoderIfNotExist(rule_path)
    FileManipulationHelper.SaveCueList(rule_path,rule_name, currentWhiteList,currentBlackList,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data)
    #FileManipulationHelper.MakeRuleCFGFile(rule_path, look_head, look_stub, look_super, look_data, look_all,vClsIn,vDefUnit,vPosUnit,pragVar) 
    WhiteListWindow.withdraw()