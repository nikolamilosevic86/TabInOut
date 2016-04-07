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
  #  articleIds = [1334]
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
            for res in resa:
                event = res[9].replace("'","").replace("?","").lower().replace(".","")
                if(res[9]=="" or "other" in res[9].lower() or "total" in res[9].lower() or "none" in res[9].lower() or "any" in res[9].lower() or "mg" in res[9].lower() or "p=" in res[9].lower() or "yes" in  res[9].lower() or "no" in res[9].lower() or 
                   "variable" in  res[9].lower() or "event" in  res[9].lower() or "arm" in  res[9].lower() or "range" in  res[9].lower() or "month" in  res[9].lower()or "overall" in  res[9].lower() or '\xe2' in res[9].lower() or 'men' in res[9].lower()
                   or 'n'==res[9].lower()or 'baseline' in res[9].lower()or 'missing' in res[9].lower()):
                    continue
                if(res[4]==0):
                    continue
                if('\xb5g' in res[9]):
                    continue

                m = re.search('^[(\d)%()/<>=\. *-]+$',event)
                if(m<>None and m<>''):
                    continue
                isflagged = 0
                if(res[0] in flagged):
                    isflagged = 1
                
                print str(id)+"    "+table.tableOrder+"    "+str(table.tableId)+"    "+event+"    "+str(isflagged)
                queryclass.SaveAnnotation(id, table.tableOrder, table.tableId, event, isflagged)
    print "Done!"
                
                
            
            