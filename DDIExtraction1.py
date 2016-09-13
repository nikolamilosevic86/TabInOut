'''
Created on 13 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
from AnalyzePattern import GetMean,GetRange
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db_amia", )
    queryclass.CreateAdditionalDDITables()
    cursor = queryclass.db.cursor()
    sql = "select annotation.Content,AnnotationDescription,Table_idTable,RowN,ColumnN,TableOrder,idArticle,Title,SpecId from annotation inner join cell on cell.idCell=annotation.Cell_idCell inner join arttable on arttable.idTable=cell.Table_idTable inner join article on article.idArticle = arttable.Article_idArticle where Section='34073-7' and (AnnotationDescription like '%Antibiotic%' or AnnotationDescription like '%Biomedical or Dental Material%' or AnnotationDescription like '%Biologically Active Substance%'or AnnotationDescription like '%Indicator, Reagent, or Diagnostic Acid%' or AnnotationDescription like '%Organic Chemical%' or AnnotationDescription like '%Hormone%'   or AnnotationDescription like '%Lipid%')"
    cursor.execute(sql)
    results = cursor.fetchall()
    columnOfDrugs = -1
    isfirst = False
    for res in results:
        AnnotationConent = res[0]
        AnnotationDescription = res[1]
        TableId = res[2]
        RowN = res[3]
        ColumnN = res[4]
        TableOrder  = res [5]
        idArticle = res[6]
        Title = res[7]
        SetId = res[8]
        if(not isfirst or ColumnN<columnOfDrugs):
            isfirst = True
            columnOfDrugs = ColumnN
        if(ColumnN!=columnOfDrugs):
            continue  
        
        if ("These highlights do not include" in Title):
            startindex = Title.index("use")+4
            endindex = Title.index("safely")-1
            drugname = Title[startindex:endindex]
        else:
            drugname = Title
        print drugname
        if(AnnotationConent in drugname.lower()):
            continue
        cursor = queryclass.db.cursor()
        sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,CueRule) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(idArticle,SetId,TableId,TableOrder,drugname,AnnotationConent,"DDI Method 1"))
        queryclass.db.commit()

        
            
        #        if("mean" in m2.keys()):
        #            queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"mean",float(m2["mean"]),unit,res[10],"MetaMap","MetaMap") 
        #        if("sd" in m2.keys()):
        #            queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"sd",float(m2["sd"]),unit,res[10],"MetaMap","MetaMap") 
        #        if("min" in m2.keys()):
        #            queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:minimum",float(m2["min"]),unit,res[10],"MetaMap","MetaMap") 
        #        if("max" in m2.keys()):
        #            queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:maximum",float(m2["max"]),unit,res[10],"MetaMap","MetaMap")                
        #    row = row+1
                   
    print "Done"