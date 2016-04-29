#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 2 Mar 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
from AnalyzePattern import GetMean,GetRange
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db", )
    queryclass.DeleteAttribute("Age")
    queryclass.CreateAdditionalTables()
    results = queryclass.getArticles()
    articleIds = []
    PMCs = []
    for row in results:
        articleIds.append(row[0])
        PMCs.append(row[1])
    del results
    #articleIds = [6311]
    l = 0
    for id in articleIds:
        results = queryclass.getArticleTablesWithPragmatic(id,"BaselineCharacteristic")
        tables = []
        for t in results:
            table = Table()
            table.tableId = t[0]
            table.tableOrder = t[1]
            table.tableCaption = t[2]
            table.tableFooter = t[3]
            table.StructureType = t[4]
            table.PrgamaticType = t[5]
            table.hasXML = t[6]
            table.articleId = t[7]
            tables.append(table)
            resulta = queryclass.getCellsContainingInStubListOR(table.tableId, ['%Age%','%age%'])
            for res in resulta:
                m2 = {}
                #m2 = re.search('[\d\.]+',res[9])
                m2 = GetMean(res[9],m2)
                m2 = GetRange(res[9],m2)
                if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and m2["mean"]==m2["min"]):
                    del m2["mean"]
                if(m2==None):
                    continue
                m3 = re.search('\\b(age)\\b',res[11].lower())
                if m3==None:
                    continue
                if(m2==None or ("mean" in m2.keys() and (m2["mean"]=='.'or m2["mean"]=='..'))):
                    continue
                content = re.sub(r'[^\x00-\x7F]','[spec]',res[9])
                content = content.replace('?','[spec]')
                if "range" in res[10].lower():
                    m2 = GetRange(res[9],m2)
                
                if("sd" in res[10].lower() and 'mean' not in res[10].lower()) or "p-value" in res[10].lower() or "p" ==res[10].lower():
                    continue
                m3 = re.search('\\b(p)\\b',res[10].lower())
                m4 = re.search('\\b[\/](p)\\b',res[10].lower())
                if m3!=None and m4==None:
                    continue
                if("onset" in res[11].lower()):
                    continue
                if('%' in content or 'day' in content or 'min' in content or '<' in content or '>' in content or '=' in content or '?' in content or '<' in res[11] or '>' in res[11] or '=' in res[11]or '?' in res[11] or 'min' in res[11].lower() or 'max' in res[11].lower()):
                    continue
                unit = 'years'
                if("months" in res[11].lower() or "months" in res[9].lower()):
                    unit = 'months'
                    #totalNum = totalNum/12
                if("weeks" in res[11].lower() or "weeks" in res[9].lower()):
                     unit = 'weeks'
                    #totalNum = totalNum/52
                totalNum = 0.0
                if(m2!= None and "mean" in m2.keys() and m2["mean"]!=None):
                    totalNum = float(m2["mean"])
                if(m2== None):
                    continue
                print 'Age:'+str(totalNum)+" "+unit
                
                if("mean" in m2.keys()):
                    queryclass.SaveAttribute(id,"Mean",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["mean"]),unit,res[10]) 
                if("sd" in m2.keys()):
                    queryclass.SaveAttribute(id,"SD",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["sd"]),unit,res[10]) 
                if("min" in m2.keys()):
                    queryclass.SaveAttribute(id,"Range:Minimum",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["min"]),unit,res[10]) 
                if("max" in m2.keys()):
                    queryclass.SaveAttribute(id,"Range:Maximum",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["max"]),unit,res[10])  
                    
                    
                    
            resulta = queryclass.getCellsContainingInSuperRowListOR(table.tableId, ['Age','age'])
            
            for res in resulta:
                m2 = {}
                m2 = GetMean(res[9],m2)
                m2 = GetRange(res[9],m2)
                if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and m2["mean"]==m2["min"]):
                    del m2["mean"]
                if(m2==None or ("mean" in m2.keys() and m2["mean"]=='.')):
                    continue
                m3 = re.search('\\b(age)\\b',res[12].lower())
                if m3==None:
                    continue
                if("sd" in res[11].lower() and "mean" not in  res[11].lower() ) or "%" in res[11].lower() or "onset" in res[11].lower():
                    continue
                if("sd" in res[10].lower() and 'mean' not in res[10].lower()) or "p-value" in res[10].lower() or "p" ==res[10].lower():
                    continue
                content = re.sub(r'[^\x00-\x7F]','[spec]',res[9])
                content = content.replace('?','[spec]')
                if('<' in content or '>' in content or '=' in content or '?' in content or '<' in res[11] or '>' in res[11] or '=' in res[11] or '<' in res[12] or '>' in res[12] or '=' in res[12]):
                    continue
                unit = 'years'
                if("months" in res[11].lower() or "months" in res[9].lower()):
                    #totalNum = totalNum/12
                    unit = 'months'
                if("weeks" in res[11].lower() or "weeks" in res[9].lower()):
                    #totalNum = totalNum/52
                    unit = 'weeks'
                if "range" in res[10].lower():
                    m2 = GetRange(res[9],m2)
                if "sd" in res[10].lower() or "p-value" in res[10].lower() or "p" ==res[10].lower():
                    continue
                totalNum = 0.0
                if(m2!= None and "mean" in m2.keys() and m2["mean"]!=None):
                    totalNum = float(m2["mean"])
                if("mean" in m2.keys()):
                    queryclass.SaveAttribute(id,"Mean",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["mean"]),unit,res[10]) 
                if("sd" in m2.keys()):
                    queryclass.SaveAttribute(id,"SD",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["sd"]),unit,res[10]) 
                if("min" in m2.keys()):
                    queryclass.SaveAttribute(id,"Range:Minimum",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["min"]),unit,res[10]) 
                if("max" in m2.keys()):
                    queryclass.SaveAttribute(id,"Range:Maximum",table.tableId,table.tableOrder,PMCs[l],"Age","",float(m2["max"]),unit,res[10]) 
        l = l+1        
    print "Done"