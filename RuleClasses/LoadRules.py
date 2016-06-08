'''
Created on Jun 8, 2016

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import FileManipulationHelper
import Rule
def LoadRulesForProcessing(project_name):
    rules = []
    projectpath = "Projects/"+project_name
    rules_names = FileManipulationHelper.loadRules(projectpath)
    for rule_name in rules_names:
        rule_datapath = projectpath+'/'+rule_name
        black_list = FileManipulationHelper.loadBlackList(project_name, rule_name)
        white_list = FileManipulationHelper.loadWhiteList(project_name, rule_name)
        cfg = FileManipulationHelper.loadRuleConfig(project_name, rule_name)
        rule = Rule.Rule()
        rule.RuleName = rule_name
        rule.WhiteList = white_list
        rule.BlackList = black_list
        if(cfg['Header']==1):
            rule.look_header = True
        if(cfg['Stub']==1):
            rule.look_stub = True
        if(cfg['Super-row']==1):
            rule.look_superrow = True
        if(cfg['Data']==1):
            rule.look_data = True
        if(cfg['All']==1):
            rule.look_anywhere = True
        
        #PatternList
        rules.append(rule)
        