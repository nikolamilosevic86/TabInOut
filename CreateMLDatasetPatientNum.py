'''
Created on Apr 14, 2016

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db" )
    results = queryclass.getDataForTrainingDataset()
    target = open("learnngCellDataset.csv", 'w')                                                                                          
    target.write("ArticleId,PMCid,TableName,SpecPragmatics,CellContent,Header,Stub,SuperRow,rowN,columnN,function\n")
    for res in results:
        idArticle = res[0]
        PMCid = res[1]
        idTable = res[2]
        TableOrder = res[3]
        SpecPragmatic = res[4]
        idCell = res[5]
        CellType = res[6]
        RowN = res[7]
        ColumnN =res[8]
        Content = res[9]
        Header = res[10]
        Stub = res[11]
        SuperRow = res[12]
        result2 = queryclass.getCellRole(idCell)
        CellRole = ""
        for role in result2:
            CellRole = CellRole+str(role[0])
        if(Content!=None):
            Content = Content.replace("'","\'").replace("\n"," ")
            Content = re.sub(r'\d','x',Content)
        if(Header!=None):
            Header = Header.replace("'","\'").replace("\n"," ")
            Header = re.sub(r'\d','x',Header)
        if(Stub!=None):
            Stub = Stub.replace("'","\'").replace("\n"," ")
            Stub = re.sub(r'\d','x',Stub)
        if(SuperRow!=None):
            SuperRow = SuperRow.replace("'","\'").replace("\n"," ")
            SuperRow = re.sub(r'\d','x',SuperRow)
        target.write(str(idArticle)+","+str(PMCid)+","+str(TableOrder)+","+str(SpecPragmatic)+",\""+str(Content)+
                     "\",\""+str(Header)+"\",\""+str(Stub)+"\",\""+str(SuperRow)+"\","+str(RowN)+","+str(ColumnN)
                     +","+str(CellRole)+"\n")
        
    target.close()
    print "Done"