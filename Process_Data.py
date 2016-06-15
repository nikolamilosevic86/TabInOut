'''
Created on 13 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import FileManipulationHelper
import QueryDBClass

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
            
            
            
            break
    pass

