'''
Created on 14 Mar 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import MySQLdb
content = []
with open("InclusionExclusions") as f:
    content = f.readlines()
db = MySQLdb.connect("localhost","root","","table_db")

for i in content:
    cursor = db.cursor()
    sql = "select idTable,SpecPragmatic from arttable where idTable="+str(i)
    cursor.execute(sql)
    results = cursor.fetchall()
    for res in results:
        print str(res[0])+"  "+res[1]
db.close()