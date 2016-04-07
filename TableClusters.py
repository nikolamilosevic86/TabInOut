'''
Created on 9 Mar 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss

queryclass = QueryDBCalss("localhost","root","","table_db" )
cursor = queryclass.db.cursor()
sql = "select idTable, AnnotationDescription from arttable inner join cell on cell.Table_idTable=arttable.idTable inner join annotation on annotation.Cell_idCell=cell.idCell where AgentName='MetaMap' group by idTable, AnnotationDescription"
cursor.execute(sql)
results = cursor.fetchall()
tableclusters = {}
previd = -5
clustername = ''
newcluster = True
for row in results:
    if previd!=row[0]:
        previd = row[0]
        newcluster = True
        if  tableclusters.has_key(clustername):
            cnt = tableclusters[clustername]
            tableclusters[clustername] = cnt+1
        else:
            tableclusters[clustername] = 1
        clustername = row[1]
    else:
        clustername = clustername+';'+row[1]
print "Almost done"
f = open('clusters2.csv', 'w')
for key, value in tableclusters.iteritems():
    f.write('"'+key+'"\n') #+';'+str(value)+'\n')
f.close()
    
    