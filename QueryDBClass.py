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
        self.db = MySQLdb.connect(host,username,password,database)
        
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
        sql = "Create table if not exists PatientGroup (id int NOT NULL AUTO_INCREMENT,GroupName varchar(255), tableID int, articleID int, PRIMARY KEY (id), Foreign key (articleID) REFERENCES  article(idArticle))"
        cursor.execute(sql)
        sql = "Create table if not exists PatientGroupIEAttributes (id int NOT NULL AUTO_INCREMENT,AttributeName varchar(255), StringValue varchar(255),IntValue DOUBLE, GroupID int, PRIMARY KEY (id), Foreign key (GroupID) REFERENCES  PatientGroup(id))"
        cursor.execute(sql)
        sql = "Create table if not exists AdverseEventNames (id int NOT NULL AUTO_INCREMENT,idArticle int, PMC varchar(255),TableName varchar(255), idTable int, EventName varchar(255), AnnotationFlag int, PRIMARY KEY (id))"
        cursor.execute(sql)
        
    def SaveArm(self,groupName,articleId, tableId):
        cursor = self.db.cursor()
        sql = "INSERT into PatientGroup (GroupName,ArticleID,tableID) values (%s,%s,%s)" 
        cursor.execute(sql,(groupName,articleId,tableId))
        self.db.commit()
        return cursor.lastrowid
    
    def SaveAnnotation(self,idArticle,tableName, tableId,Event,AnnotationFlag):
        cursor = self.db.cursor()
        sql = "INSERT into AdverseEventNames (idArticle,tableName,idTable,EventName,AnnotationFlag) values (%d,'%s',%d,'%s',%d)" % (int(idArticle),tableName, int(tableId),Event,int(AnnotationFlag))
        cursor.execute(sql)
        self.db.commit()
        return cursor.lastrowid
    
    def SaveAttribute(self,groupId,AttributeName,AttributeValue):
        cursor = self.db.cursor()
        intValue = -999
        try:
            intValue = int(AttributeValue)
        except:
            intValue = None
        sql = "INSERT into patientgroupieattributes (groupID,AttributeName,StringValue,IntValue) values (%s,%s,%s,%s)"
        cursor.execute(sql,(groupId,AttributeName,AttributeValue,intValue))
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
        sql = "Drop table if exists AdverseEventNames"
        cursor.execute(sql)
        self.db.commit()
        
    def DeleteAttribute(self,attributeName):
        cursor = self.db.cursor()
        sql = "Delete from patientgroupieattributes where AttributeName='"+attributeName+"'"
        cursor.execute(sql)
        self.db.commit()