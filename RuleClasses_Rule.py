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
    wl_look_header = False
    wl_look_stub = False
    wl_look_superrow = False
    wl_look_data = False
    wl_look_anywhere = False
    bl_look_header = False
    bl_look_stub = False
    bl_look_superrow = False
    bl_look_data = False
    bl_look_anywhere = False
    PragmaticClass = ''
    PatternList = []
    DefaultUnit = ''
    PossibleUnits = []
    PossibleCategories = []
    is_semantic = False
    RuleType = ''