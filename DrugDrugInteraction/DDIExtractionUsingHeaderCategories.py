'''
Created on 18 Oct 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db_amia", )
    queryclass.CreateAdditionalDDITables()
    cursor = queryclass.db.cursor()
    d = {}
    with open("Categories.txt") as f:
        for line in f:
            spl = line.split('\t')
            print spl[0]
            d[spl[0].lower()] = spl[1].replace('\n','').lower()
    print d
    sql = """select Content,Table_idTable,RowN,ColumnN,TableOrder,idArticle,Title,SpecId,CellRole_idCellRole from cell inner join arttable on arttable.idTable=cell.Table_idTable inner join article on 
    article.idArticle = arttable.Article_idArticle inner join cellroles on cellroles.Cell_idCell=cell.idCell where Section='34073-7'"""
    cursor.execute(sql)
    results = cursor.fetchall()
    columnOfDrugs = -1
    isfirst = False
    for res in results:
        Conent = res[0]
        TableId = res[1]
        RowN = res[2]
        ColumnN = res[3]
        TableOrder  = res [4]
        idArticle = res[5]
        Title = res[6]
        SetId = res[7]
        sql1 = """Select * from structuredproductlabelmetadata where SetId = '"""+SetId+"'"
        cursor.execute(sql1)
        results2 = cursor.fetchall()
        for res1 in results2:
            drugname = res1[3]
        ContainsKey = False
        ContainsTheKey = ''
        for keyA in d.keys() :
            if keyA in Conent.lower() :
                if (d[keyA] == 'Drug Name or Drug Class'):
                    ContainsKey = True
                    ContainsTheKey = keyA
        if ContainsKey:        
            columnRes = queryclass.getCellsInColumn(TableId,ColumnN)
            for r in columnRes:
                r_id = r[0]
                r_idTable = r[3]
                r_row = r[4]
                r_column=r[5]
                r_content=r[9]
                r_header = r[10]
                r_stub = r[11]
                r_super_row = r[12]
                if(ContainsTheKey in r_content):
                    continue
                if(['drug','drugs'] in r_content):
                    continue
                cursor = queryclass.db.cursor()
                sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,CueRule) values (%s,%s,%s,%s,%s,%s,%s)"
                print drugname,r_content
                cursor.execute(sql,(idArticle,SetId,TableId,TableOrder,drugname,r_content,"DDI Method 2"))
                queryclass.db.commit()
            ContainsKey = False
            ContainsTheKey = ''
    
    