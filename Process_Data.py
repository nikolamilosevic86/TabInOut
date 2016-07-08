'''
Created on 13 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import FileManipulationHelper
import QueryDBClass
import re

Source = ''

def CheckWListUsingRegex(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    global Source
    ContainsValue = False
    if(look_header):
        for item in List:
            if Header == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Header)
            if(m1!=None):
                ContainsValue = True
                Source = Stub
    if(look_stub):
        for item in List:
            if(Stub == None or item.replace('\n','') ==''):
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Stub)
            if(m1!=None):
                ContainsValue = True
                Source = Header
    if(look_superrow):
        for item in List:
            if Super_row == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Super_row)
            if(m1!=None):
                ContainsValue = True
                Source = "h:"+Header+"; s:"+Stub
    if(look_data):
        for item in List:
            if Data == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Data)
            if(m1!=None):
                ContainsValue = True
                Source = "h:"+Header+"; s:"+Stub
    return ContainsValue

def CheckBListUsingRegex(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    ValidCandidate = True
    if(look_header):
        for item in List:
            if Header == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Header)
            if(m1!=None):
                ValidCandidate = False
    if(look_stub):
        for item in List:
            if Stub == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Stub)
            if(m1!=None):
                ValidCandidate = False
    if(look_superrow):
        for item in List:
            if Super_row == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Super_row)
            if(m1!=None):
                ValidCandidate = False
    if(look_data):
        for item in List:
            if Data == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Data)
            if(m1!=None):
                ValidCandidate = False
    
    return ValidCandidate

def CheckUnits(Header,Stub,SuperRow,Data,defaultUnit,PossibleUnits):
    UnitSelected = defaultUnit
    for unit in PossibleUnits:
        unit = unit.replace('\n','')
        if Header != None:
            m1 = re.search('\\b('+unit+")\\b",Header)
            if(m1!=None):
                UnitSelected = unit
                break
        if Stub !=None:
            m1 = re.search('\\b('+unit+")\\b",Stub)
            if(m1!=None):
                UnitSelected = unit
                break
        if SuperRow != None:
            m1 = re.search('\\b('+unit+")\\b",SuperRow)
            if(m1!=None):
                UnitSelected = unit
                break
        if Data != None:
            m1 = re.search('\\b('+unit+")\\b",Data)
            if(m1!=None):
                UnitSelected = unit
                break
    return UnitSelected
            

def ProcessDataBase(project_name,rules):
    global Source
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    for rule in rules:
        rows = db.getCellsGeneric(rule.PragmaticClass,rule.wl_look_header,rule.wl_look_stub,rule.wl_look_superrow,rule.wl_look_data,rule.WhiteList)
        gen_rule_name = rule.RuleName
        for row in rows:
            id_article = row[0]
            pmc_id = row[1]
            id_table = row[2]
            tableOrder = row[3]
            SpecPragmatic =  row[4]
            idCell = row[5]
            cellType = row[6]
            rowN = row[7]
            columnN = row[8]
            Content = row[9]
            Header = row[10]
            Stub = row[11]
            Super_row = row[12]

            ContainsLooked = CheckWListUsingRegex(rule.wl_look_header,rule.wl_look_stub,rule.wl_look_superrow,rule.wl_look_data,rule.WhiteList,Header,Stub,Super_row,Content)
            if(ContainsLooked):
                ValidCandidate = CheckBListUsingRegex(rule.bl_look_header,rule.bl_look_stub,rule.bl_look_superrow,rule.bl_look_data,rule.BlackList,Header,Stub,Super_row,Content)
                if ValidCandidate:
                    FoundSemantics = False
                    AllSemSaved = False
                    for syn_rule in rule.PatternList:
                        if(AllSemSaved ==True):
                                break
                        m = re.search(syn_rule.regex.replace('\n',''),Content)
                        if m == None:
                            continue
                        c = 0
                        for sem in syn_rule.SemanticValues:
                            if(AllSemSaved ==True):
                                break
                            value = m.group(sem.position)
                            if len(sem.SemTermList)>0:
                                contains_term =  CheckWListUsingRegex(True,True,True,False,sem.SemTermList,Header,Stub,Super_row,Content)
                                if(contains_term):
                                    semValue  = sem.Semantics
                                    FoundSemantics = True
                            if len(sem.SemTermList)==0:
                                semValue  = sem.Semantics
                                FoundSemantics = True
                            c = c+1
                            if FoundSemantics:    
                                syn_rule_name = syn_rule.name
                                Unit = CheckUnits(Header, Stub, Super_row, Content, rule.DefaultUnit, rule.PossibleUnits)
                        #Save the value to the database
                                db.SaveExtracted(id_article,id_table,tableOrder,pmc_id,rule.ClassName,semValue,value,Unit,Source,gen_rule_name,syn_rule_name)
                                
                                FoundSemantics = False
                                if(c == len(syn_rule.SemanticValues)):
                                    AllSemSaved = True
                            
                        
                    
            
    print "Done!!!!"
    #FinishScreen()
    
    pass

