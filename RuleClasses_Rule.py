'''
Created on Jun 8, 2016

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
class Rule:
    RuleName = ""
    ClassName = ""
    WhiteList = []
    BlackList = []
    look_header = False
    look_stub = False
    look_superrow = False
    look_data = False
    look_anywhere = False
    PragmaticClass = ''
    PatternList = []
    DefaultUnit = ''
    PossibleUnits = []