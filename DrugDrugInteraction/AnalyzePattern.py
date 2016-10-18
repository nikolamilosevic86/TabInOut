#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26 Apr 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import re
def GetMean(value,res):
    #Mean can be mean +- sd or mean (min,max)
    #regex = (\d+\.\d+) [(](\d+\.*\d*)[ \-,]{1,}[ ]{0,}(\d+)[)]
    if res == None:
        res = {}
    m = re.search(ur'(\d+\.*\d*)[?  ]*[\-—–−––,]+(\d+\.*\d*)[ (]*(\d+\.*\d*)[?  ]*[±][?  ]*(\d+\.*\d*)[)]*',value)
    if(m!=None):

        range_min = m.group(1)
        range_max = m.group(2)
        mean = m.group(3)
        sd = m.group(4)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        res["sd"] = sd
        return res
    m = re.search(ur'(\d+\.*\d*)[?  ]*[±][?  ]*(\d+\.*\d*)[ (]*(\d+\.*\d*)[?  ]{0,}[\-—–−––,]+[ ]*(\d+\.*\d*)[)]*',value)
    if(m!=None):

        range_min = m.group(3)
        range_max = m.group(4)
        mean = m.group(1)
        sd = m.group(2)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        res["sd"] = sd
        return res
    m = re.search(ur'(\d+\.*\d*)[?  ]*[\(](\d+\.*\d*)[?  ]{0,}[\-—–−––,]+(\d+\.*\d*)[\)]',value)
    if(m!=None):
        mean = m.group(1)
        range_min = m.group(2)
        range_max = m.group(3)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        return res
    m = re.search(ur"[(](\d+\.*\d*)[?  ]{0,}[\-—–−,]{1,}[?  ]{0,}(\d+\.*\d*)[)][?  ]*(\d+\.*\d*)",value) 
    if(m!=None):
        range_min = m.group(1)
        range_max = m.group(2)
        mean = m.group(3)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        return res
    m = re.search(ur"(\d+\.*\d*)[?  ]{0,}[±]{1,}[?  ]{0,}(\d+\.*\d*)",value) 
    if(m!=None):
        mean = m.group(1)
        sd = m.group(2)
        res["mean"] = mean
        res["sd"] = sd
        return res
    m = re.search(ur"(\d+\.*\d*)[?  ]{0,}[(]{1,}[?  ]{0,}(\d+\.*\d*)[)]{1,}",value) 
    if(m!=None):
        mean = m.group(1)
        sd = m.group(2)
        res["mean"] = mean
        res["sd"] = sd
        return res
    m = re.search("(\d+\.*\d*)",value) 
    if(m!=None):
        mean = m.group(1)
        res["mean"] = mean
    return res

def GetRange(value,res):
    if res == None:
        res = {}
    m = re.search(ur"(\d+\.*\d*)[?  ]*[(](\d+\.*\d*)[?  ]{0,}[\-—–−,]{1,}[?  ]{0,}(\d+\.*\d*)[)]",value)
    if(m!=None):
        mean = m.group(1)
        range_min = m.group(2)
        range_max = m.group(3)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        return res
    m = re.search(ur"[(](\d+\.*\d*)[?  ]{0,}[\-—–−,;]{1,}[?  ]{0,}(\d+)[)][?  ]*(\d+\.*\d*)",value) 
    if(m!=None):
        range_min = m.group(1)
        range_max = m.group(2)
        mean = m.group(3)
        res["mean"] = mean
        res["min"] = range_min
        res["max"] = range_max
        return res
    m = re.search(ur"(\d+\.*\d*)[?  ]{0,1}[\-—–−,;]{1,}[?  ]{0,}(\d+\.*\d*)",value) 
    if(m!=None):
        range_min = m.group(1)
        range_max = m.group(2)
        res["min"] = range_min
        res["max"] = range_max
        return res
    return res
