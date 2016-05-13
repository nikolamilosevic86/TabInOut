'''
Created on 29 Feb 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import MySQLdb

class QueryDBCalss:
    db = None
    def __init__(self,host,username,password,database):
        self.db = MySQLdb.connect(host,username,password,database,charset='utf8')
        
    def __del__(self):
        try:
            self.db.close()
        except:
            print "There was an error closing database"
    
    def getArticles(self):
        cursor = self.db.cursor()
        sql = "select * from article"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getArticleTables(self,articleID):
        cursor = self.db.cursor()
        sql = "select * from arttable where Article_idArticle='%d'" % articleID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    
    def getArticleTablesWithPragmatic(self,articleID,pragmaticType):
        cursor = self.db.cursor()
        sql = "select * from arttable where Article_idArticle='%d' and SpecPragmatic='%s'" % (articleID,pragmaticType)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getTableCells(self,tableID):
        cursor = self.db.cursor()
        sql = "select * from cell where Table_idTable='%d'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsInRow(self,tableID,RowN):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and RowN='%d'" % (tableID,RowN)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getNonHeaderCellsInColumn(self,tableID,columnN):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole<>'1' and ColumnN='%d'" % (tableID,columnN)
        cursor.execute(sql)
        results = cursor.fetchall()
        if(len(results)==0):
            sql = "SELECT * FROM cell where Table_idTable='%d' and ColumnN='%d'" % (tableID,columnN)
            cursor.execute(sql)
            results = cursor.fetchall()
        return results
    
    def getHeaderCells(self,tableID):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole='1'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getStubCells(self,tableID):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole='2'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getSuperRowCells(self,tableID):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole='4'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getDataCells(self,tableID):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole='3'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getNavigatinalCells(self,tableID):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='%d' and CellRole_idCellRole<>'3'" % tableID
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'" 
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or Content LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    
    
    
    
    def getHeaderCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='1' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getHeaderCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='1'"
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getHeaderCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='1' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '"+string+"'"
                first = False
            else:
                sql = sql+"or Content LIKE '"+string+"'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    
    def getStubCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='2' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getStubCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='2'"
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getStubCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='2' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or Content LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getSuperRowCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='4' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getSuperRowCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='4'"
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getSuperRowCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='4' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or Content LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getDataCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='3' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getDataCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='3'"
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getDataCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole='3' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or Content LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getNavigationalCellsContaining(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole<>'3' and Content LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getNavigationalCellsContainingListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole<>'3'"
        for string in stringList:
            sql = sql+" and Content LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getNavigationalCellsContainingListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join cellroles on idCell=Cell_idCell where Table_idTable='"+str(tableID)+"' and CellRole_idCellRole<>'3' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"Content LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or Content LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    
    def getCellsContainingInHeader(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and WholeHeader LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInHeaderListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'" 
        for string in stringList:
            sql = sql+" and WholeHeader LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInHeaderListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeHeader LIKE '"+string+"'"
                first = False
            else:
                sql = sql+"or WholeHeader LIKE '"+string+"'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInStub(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and WholeStub LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInStubListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'" 
        for string in stringList:
            sql = sql+" and WholeStub LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInStubListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeStub LIKE '"+string+"'"
                first = False
            else:
                sql = sql+"or WholeStub LIKE '"+string+"'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInSuperRow(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and WholeSuperRow LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInSuperRowListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'" 
        for string in stringList:
            sql = sql+" and WholeSuperRow LIKE '%"+string+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInSuperRowListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and (" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeSuperRow LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or WholeSuperRow LIKE '%"+string+"%'"
            
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    
    def getCellsContainingINavigational(self,tableID, string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"' and (WholeHeader LIKE '%"+string+"%' or WholeStub LIKE '%"+string+"%' or WholeSuperRow LIKE '%"+string+"%'" 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getDataForTrainingDataset(self,):
        cursor = self.db.cursor()
        sql = """ SELECT idArticle,article.PMCID,idTable,TableOrder,SpecPragmatic,idCell,CellType,RowN,ColumnN,Content,WholeHeader,WholeStub,WholeSuperRow FROM article inner join arttable on arttable.Article_idArticle=article.idArticle 
 inner join cell on cell.Table_idTable=arttable.idTable 
 where idArticle in (19,25,164,166,215,309,449,715,1118,1233,1273,1283,1287,1291,1359,1362,1376,1410,1423,1446,1504,1985,2165,2207,2230,
2246,2269,2370,2478,2486,2656,2688,2737,2809,2811,2834,2864,3023,3030,3044,3085,3088,3094,3097,3105,3162,3275,3276,
3291,3308,3324,3561,3652,3950,3974,4011,4024,4113,4185,4246,4305,4375,4428,4539,4585,4713,4733,4744,4861,4908,4914,
4958,5055,5162,5267,5330,5383,5469,5558,5561,5569,5578,5636,5637,5666,5696,5704,5758,5807,5842,5842,5937,6034,6191,
6195,6286,6311,6382,6405,6540) and SpecPragmatic='BaselineCharacteristic' """ 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def getDataForDevDataset(self,):
        cursor = self.db.cursor()
        sql = """ SELECT idArticle,article.PMCID,idTable,TableOrder,SpecPragmatic,idCell,CellType,RowN,ColumnN,Content,WholeHeader,WholeStub,WholeSuperRow FROM article inner join arttable on arttable.Article_idArticle=article.idArticle 
 inner join cell on cell.Table_idTable=arttable.idTable 
 where idArticle in (5505,2012,4000,2650,1988,2001,1443,1355,4275,1377,3417,1906,1976,2528,352,2536,1345,1437,3559,2748,4021,2866,3898,3448,6443,3566,1939,4680,2011,4593,1347,1348,1888,3424,3512,1388,3490,6042,1318,1911,2995,3950,3036,4321,5225,5859,4928,3781,4688,2787,2012,6342,1941,1134,1424,3787,1176,4295,2308,1345,3304,2602,5127,3596,3777,6425,3654,5228,3503,3713,1939,4689,6148,2472,5504,1351,3162,1386,5767,1762,6312,5937,1269,1769,1433,3496,2307,2011,5153,4156,5354,2529,3716,4282,4604,3424,2979,2062,2880,2848
) and SpecPragmatic='BaselineCharacteristic' """ 
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellRole(self,idCell):
        cursor = self.db.cursor()
        sql = "select CellRole_idCellRole from cell inner join cellroles on cell.idCell=cellroles.Cell_idCell where idCell='"+str(idCell)+"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        
        
        
    
    def getCellsAnnotated(self,tableID,stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell inner join annotation on cell.idCell = annotation.Cell_idCell where Table_idTable = '"+str(tableID)+"' and ("
        first = True
        for string in stringList:
            if(first):
                sql = sql+"AnnotationDescription LIKE '"+string+"'"
                first = False
            else:
                sql = sql+"or AnnotationDescription LIKE '"+string+"'"
        sql = sql+")"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInNavigationalListAND(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'and ((" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeHeader LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"and WholeHeader LIKE '%"+string+"%'"
        sql = sql+") or ("
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeStub LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"and WholeStub LIKE '%"+string+"%'"
        sql = sql+") or ("
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeSuperRow LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"and WholeSuperRow LIKE '%"+string+"%'"
        sql = sql+"))"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def getCellsContainingInNavigationalListOR(self,tableID, stringList):
        cursor = self.db.cursor()
        sql = "SELECT * FROM cell  where Table_idTable='"+str(tableID)+"'and ((" 
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeHeader LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or WholeHeader LIKE '%"+string+"%'"
        sql = sql+") or ("
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeStub LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or WholeStub LIKE '%"+string+"%'"
        sql = sql+") or ("
        first = True
        for string in stringList:
            if(first):
                sql = sql+"WholeSuperRow LIKE '%"+string+"%'"
                first = False
            else:
                sql = sql+"or WholeSuperRow LIKE '%"+string+"%'"
        sql = sql+"))"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def CreateAdditionalTables(self):
        cursor = self.db.cursor()
        sql = "Create table if not exists IEAttribute (id int NOT NULL AUTO_INCREMENT,documentId INT, PMC varchar(255),idTable int,TableName varchar(200),Class varchar(255),SubClass varchar(255),VOption varchar(255),Target varchar(255), StringValue varchar(255),IntValue DOUBLE, Unit varchar(255), PRIMARY KEY (id))"
        cursor.execute(sql)
        sql = "Create table if not exists AdverseEventNames (id int NOT NULL AUTO_INCREMENT,idArticle int, PMC varchar(255),TableName varchar(255), idTable int, EventName varchar(255), AnnotationFlag int, PRIMARY KEY (id))"
        cursor.execute(sql)
        
    
    def SaveAnnotation(self,idArticle,tableName, tableId,Event,AnnotationFlag):
        cursor = self.db.cursor()
        sql = "INSERT into AdverseEventNames (idArticle,tableName,idTable,EventName,AnnotationFlag) values (%d,'%s',%d,'%s',%d)" % (int(idArticle),tableName, int(tableId),Event,int(AnnotationFlag))
        cursor.execute(sql)
        self.db.commit()
        return cursor.lastrowid
    
    def SaveAttribute(self,documentID,Option,tableId,TableName,PMC,AttributeName,AttributeSubClass,AttributeValue,Unit,Target):
        cursor = self.db.cursor()
        intValue = -999
        try:
            intValue = float(AttributeValue)
        except:
            intValue = None
        sql = "INSERT into IEAttribute (documentId, PMC,idTable,TableName,Class,SubClass,VOption,Target, StringValue,IntValue, Unit) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(documentID,PMC,tableId,TableName,AttributeName,AttributeSubClass,Option,Target,AttributeValue,intValue,Unit))
        self.db.commit()
        return cursor.lastrowid
    
    def ClearCreatedTables(self):
        cursor = self.db.cursor()
        sql = "Drop table if exists patientgroupieattributes"
        cursor.execute(sql)
        self.db.commit()
        sql = "Drop table if exists patientgroup"
        cursor.execute(sql)
        self.db.commit()
        sql = "Drop table if exists IEAttribute"
        cursor.execute(sql)
        self.db.commit()
        sql = "Drop table if exists AdverseEventNames"
        cursor.execute(sql)
        self.db.commit()
        
    def DeleteAttribute(self,attributeName):
        cursor = self.db.cursor()
        sql = "Delete from IEAttribute where Class='"+attributeName+"'"
        cursor.execute(sql)
        self.db.commit()
