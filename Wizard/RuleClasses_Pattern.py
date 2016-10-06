'''
Created on Jun 8, 2016

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
class Pattern:
    name = ""
    regex = ""
    SemanticValues = []
    
    def addSemanticVal(self,PatternValueSem):
        self.SemanticValues.append(PatternValueSem)