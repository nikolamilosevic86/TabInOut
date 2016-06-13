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
    pass