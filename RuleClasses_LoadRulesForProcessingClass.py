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
    pattern = RuleClasses_Pattern.Pattern()
    i = 0
    for line in lines:
        if line == '\n':
            continue
        if(line[0]=='+'):
            i = 0
            semanticVals = []
            if pattern.name != '':
                pattern.SemanticValues = semanticVals
                patterns.append(pattern)
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
        rule.WhiteList = white_list
        rule.BlackList = black_list
        if(int(cfg['Header'])==1):
            rule.look_header = True
        if(int(cfg['Stub'])==1):
            rule.look_stub = True
        if(int(cfg['Super-row'])==1):
            rule.look_superrow = True
        if(int(cfg['Data'])==1):
            rule.look_data = True
        if(int(cfg['All'])==1):
            rule.look_anywhere = True
        rule.DefaultUnit = cfg['DefUnit']
        rule.PossibleUnits = cfg['PosUnit'].split(',')
        patterns = LoadSyntacticRoles(project_name,rule_name)
        rule.PatternList = patterns
        
        
        #PatternList
        rules.append(rule)
        