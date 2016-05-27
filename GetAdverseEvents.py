#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 7 Apr 2016

@author: mbaxknm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
from collections import Counter
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db" )
    queryclass.ClearCreatedTables()
    queryclass.CreateAdditionalTables()
    results = queryclass.getArticles()
    articleIds = []
    for row in results:
        articleIds.append(row[0])
    del results
    #articleIds = [2418]
    for id in articleIds:
        results = queryclass.getArticleTablesWithPragmatic(id,"AdverseEvent")
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
            #tables.append(table)
            resa = queryclass.getCellsAnnotated(table.tableId, ["%sosy%","%dsyn%"])
            lastColN = -999
            i = 0
            flagged = {}
            colum = []
            sameCol = True
            first = True
            for res in resa:
                if(first):
                    lastColN = res[5]
                    first = False
                colum.append(res[5])
                flagged[res[0]]=1
                if(lastColN!=res[5]):
                    sameCol=False
            if(not sameCol):
                counter = Counter(colum)
                maxC =0
                for el in counter.elements():
                    if counter[el]>maxC:
                        lastColN = el 
            resa = queryclass.getNonHeaderCellsInColumn(table.tableId,lastColN)
            processed = []
            for res in resa:
                if res[0] in processed:
                    continue
                event = res[9].replace("'","").replace("?","").lower().replace(".","")
                event = re.sub(r'[^\x00-\x7F]',' ',event)
                if(event=="" or "other" in event or "total" in event or "none" in event or "any" in event or "mg" in event or "p=" in event or "yes" in  event or "toxicity" in event or 
                   "variable" in  event or "event" in  event or "arm" in  event or "range" in  event or "month" in  event or "overall" in event or  'men' in event
                   or 'n'==event or 'baseline' in event or 'missing' in event or 'patient' in event):
                    continue
                if(res[4]==0):
                    continue
                
                m = re.search('^[(\d)%()/<>=\. *-g]+$',event)
                if(m<>None and m<>''):
                    continue
                isflagged = 0
                if(res[0] in flagged):
                    isflagged = 1
                
                print str(id)+"    "+table.tableOrder+"    "+str(table.tableId)+"    "+event+"    "+str(isflagged)
                queryclass.SaveAnnotation(id, table.tableOrder, table.tableId, event, isflagged)
                processed.append(res[0])
                
          #For rows  
            resa = queryclass.getCellsAnnotated(table.tableId, ["%sosy%","%dsyn%"])
            lastRowN = -999
            i = 0
            flagged = {}
            row = []
            sameRow = True
            first = True
            for res in resa:
                if(first):
                    lastRowN = res[4]
                row.append(res[4])
                flagged[res[0]]=1
                if(lastRowN!=res[4]):
                    sameRow=False
            if(not sameRow):
                counter = Counter(row)
                maxR =2
                for el in counter.elements():
                    if counter[el]>maxR:
                        lastRowN = el 
            resa = queryclass.getCellsInRow(table.tableId,lastRowN)
            processed = []
            for res in resa:
                if(res[0] in processed):
                    continue
                if(res[5]==0):
                    continue
                event = res[9].replace("'","").replace("?","").lower().replace(".","")
                event = re.sub(r'[^\x00-\x7F]',' ',event)
                if(res[9]=="" or "other" in res[9].lower() or "total" in res[9].lower() or "none" in res[9].lower() or "any" in res[9].lower() or "mg" in res[9].lower() or "p=" in res[9].lower() or "yes" in  res[9].lower() or "no" in res[9].lower() or 
                   "variable" in  res[9].lower() or "event" in  res[9].lower() or "arm" in  res[9].lower() or "range" in  res[9].lower() or "month" in  res[9].lower()or "overall" in  res[9].lower() or  'men' in res[9].lower()
                   or 'n'==res[9].lower()or 'baseline' in res[9].lower()or 'missing' in res[9].lower()or 'patient' in res[9].lower()):
                    continue

                m = re.search('^[(\d)%()/<>=\. *-g]+$',event)
                if(m<>None and m<>''):
                    continue
                isflagged = 0
                processed.append(res[0])
                if(res[0] in flagged):
                    isflagged = 1
                
                print str(id)+"    "+table.tableOrder+"    "+str(table.tableId)+"    "+event+"    "+str(isflagged)
                queryclass.SaveAnnotation(id, table.tableOrder, table.tableId, event, isflagged)
                
    print "Done!"
                
                
            
            