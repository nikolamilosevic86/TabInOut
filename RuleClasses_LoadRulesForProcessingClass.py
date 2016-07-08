'''
Created on Jun 8, 2016

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''

import FileManipulationHelper
import RuleClasses_Rule
import RuleClasses_Pattern
import RuleClasses_PatternValueSem

def LoadSyntacticRoles(project_name,rule_name):
    patterns = []
    path = "Projects/"+project_name+"/"+rule_name+"/SyntacticRules.sin"
    f = open(path,'r')
    lines = f.readlines()
    i = 0
    pattern = RuleClasses_Pattern.Pattern()
    semanticVals = []
    for line in lines:
        if line == '\n':
            continue
        if(line[0]=='+'):
            i = 0
            if pattern.name != '':
                pattern.SemanticValues = semanticVals
                patterns.append(pattern)
            semanticVals = []
            pattern = RuleClasses_Pattern.Pattern()
            pattern.name = line[1:]
            i = i+1
        elif(i==1):
            pattern.regex = line
            i = i+1
        else:
            sem = line.split('->')
            pvs = RuleClasses_PatternValueSem.PatternValueSem()
            i= i+1
            pvs.Semantics = sem[1]
            val  = sem[0].split(':')
            if (len(val)>1):
                pvs.SemTermList = val[1].split(',')
            pvs.position = int(val[0])
            semanticVals.append(pvs)
    pattern.SemanticValues = semanticVals
    patterns.append(pattern)
    return patterns
        

def LoadRulesForProcessing(project_name):
    rules = []
    projectpath = "Projects/"+project_name
    rules_names = FileManipulationHelper.loadRules(project_name)
    for rule_name in rules_names:
        rule_datapath = projectpath+'/'+rule_name
        black_list = FileManipulationHelper.loadBlackList(project_name, rule_name)
        white_list = FileManipulationHelper.loadWhiteList(project_name, rule_name)
        cfg = FileManipulationHelper.loadRuleConfig(project_name, rule_name)
        rule = RuleClasses_Rule.Rule()
        rule.RuleName = rule_name
        #rule.WhiteList = white_list
        #rule.BlackList = black_list
        afterWordList= False
        for w in white_list:
            w = w.replace('\n','')
            splitted = w.split(':')
            if splitted[0]=='Type':
                if splitted[1]=='WhiteList':
                    continue
            if splitted[0]=='Header':
                if int(splitted[1]) ==1:
                    rule.wl_look_head=True
                else:
                    rule.wl_look_head=False
            if splitted[0]=='Stub':
                if int(splitted[1]) ==1:
                    rule.wl_look_stub=True
                else:
                    rule.wl_look_stub=False
            if splitted[0]=='Super-row':
                if int(splitted[1]) ==1:
                    rule.wl_look_super=True
                else:
                    rule.wl_look_super=False
            if splitted[0]=='Data':
                if int(splitted[1]) ==1:
                    rule.wl_look_data=True
                else:
                    rule.wl_look_data=False
            if splitted[0]=='All':
                if int(splitted[1]) ==1:
                    rule.wl_look_all=True
                else:
                    rule.wl_look_all=False
            if w == "WordList:":
                afterWordList = True
                continue
            if afterWordList == True:
                rule.WhiteList.append(w)
        afterWordList= False
        for w in black_list:
            w = w.replace('\n','')
            splitted = w.split(':')
            if splitted[0]=='Type':
                if splitted[1]=='BlackList':
                    continue
            if splitted[0]=='Header':
                if int(splitted[1]) ==1:
                    rule.bl_look_head=True
                else:
                    rule.bl_look_head=False
            if splitted[0]=='Stub':
                if int(splitted[1]) ==1:
                    rule.bl_look_stub=True
                else:
                    rule.bl_look_stub=False
            if splitted[0]=='Super-row':
                if int(splitted[1]) ==1:
                    rule.bl_look_super=True
                else:
                    rule.bl_look_super=False
            if splitted[0]=='Data':
                if int(splitted[1]) ==1:
                    rule.bl_look_data=True
                else:
                    rule.bl_look_data=False
            if splitted[0]=='All':
                if int(splitted[1]) ==1:
                    rule.bl_look_all=True
                else:
                    rule.bl_look_all=False
            if w == "WordList:":
                afterWordList = True
                continue
            if afterWordList == True:
                rule.BlackList.append(w)
        
        rule.DefaultUnit = cfg['DefUnit']
        rule.PossibleUnits = cfg['PosUnit'].split(',')
        rule.PragmaticClass = cfg['PragClass']
        rule.ClassName = cfg['Class']
        patterns = LoadSyntacticRoles(project_name,rule_name)
        rule.PatternList = patterns
        
        
        #PatternList
        rules.append(rule)

    return rules
        