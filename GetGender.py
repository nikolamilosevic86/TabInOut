'''
Created on 11 Apr 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db" )
    queryclass.DeleteAttribute("BMI")
    queryclass.CreateAdditionalTables()
    results = queryclass.getArticles()
    articleIds = []
    for row in results:
        articleIds.append(row[0])
    del results
    for id in articleIds:
        results = queryclass.getArticleTables(id)
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
            resulta = queryclass.getCellsContainingInStubListOR(table.tableId, ['gender','Gender','male','female'])
            for res in resulta:
                m2 = re.search('(\d)+',res[9])
                if(m2==None):
                    continue
                totalNum = int(m2.group(0))
                if "range" in res[10].lower():
                    continue
                if(totalNum>12 and totalNum<50):
                    print 'Gender:'+str(totalNum) #add @male or @female to database
                    armid = queryclass.SaveArm(res[10], id,table.tableId) 
                    queryclass.SaveAttribute(armid, "BMI", totalNum)  
    print "Done"