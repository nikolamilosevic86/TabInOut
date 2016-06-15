'''
Created on 13 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import FileManipulationHelper
import QueryDBClass
import re

def CheckWListUsingRegex(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    ContainsValue = False
    if(look_header):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Header)
            if(m1!=None):
                ContainsValue = True
    if(look_stub):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Stub)
            if(m1!=None):
                ContainsValue = True
    if(look_superrow):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Super_row)
            if(m1!=None):
                ContainsValue = True
    if(look_data):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Data)
            if(m1!=None):
                ContainsValue = True
    return ContainsValue

def CheckBListUsingRegex(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    ValidCandidate = True
    if(look_header):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Header)
            if(m1!=None):
                ValidCandidate = False
    if(look_stub):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Stub)
            if(m1!=None):
                ValidCandidate = False
    if(look_superrow):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Super_row)
            if(m1!=None):
                ValidCandidate = False
    if(look_data):
        for item in List:
            m1 = re.search('\\b('+item+")\\b",Data)
            if(m1!=None):
                ValidCandidate = False
    
    return ValidCandidate

def ProcessDataBase(project_name,rules):
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    for rule in rules:
        rows = db.getCellsGeneric(rule.PragmaticClass,rule.look_header,rule.look_stub,rule.look_superrow,rule.look_data,rule.WhiteList)
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
            print id_article
            print pmc_id
            print id_table
            print tableOrder
            print SpecPragmatic
            print idCell
            print cellType
            print rowN
            print columnN
            print Content
            print Header
            print Stub
            print Super_row
            ContainsLooked = CheckWListUsingRegex(rule.look_header,rule.look_stub,rule.look_superrow,rule.look_data,rule.WhiteList,Header,Stub,Super_row,Content)
            if(ContainsLooked):
                ValidCandidate = CheckBListUsingRegex(rule.look_header,rule.look_stub,rule.look_superrow,rule.look_data,rule.WhiteList,Header,Stub,Super_row,Content)
                if ValidCandidate:
                    FoundSemantics = False
                    for syn_rule in rule.PatternList:
                        m = re.search(syn_rule.regex,Content)
                        c = 0
                        for sem in syn_rule.SemanticValues:
                            value = m.group(sem.position)
                            if len(sem.SemTermList)>0:
                                contains_term =  CheckWListUsingRegex(True,True,True,False,sem.SemTermList,Header,Stub,Super_row,Content)
                                if(contains_term):
                                    semValue  = sem.Semantics
                                    FoundSemantics = True
                            if len(sem.SemTermList)==0:
                                semValue  = sem.Semantics
                                FoundSemantics = True
                                    
            
    pass

