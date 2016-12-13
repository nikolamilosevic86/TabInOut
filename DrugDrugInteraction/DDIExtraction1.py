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
    #Get cells and annotations that contain potential DDIs
    sql = """select annotation.Content,AnnotationDescription,Table_idTable,RowN,ColumnN,TableOrder,idArticle,Title,SpecId,
    AnnotationID from annotation inner join cell on cell.idCell=annotation.Cell_idCell inner join arttable on
    arttable.idTable=cell.Table_idTable inner join article on article.idArticle = arttable.Article_idArticle
    where Section='34073-7' and AnnotationDescription  IN ('Pharmacologic Substance (phsu)','Biologically Active Substance (bacs)',
    'Organic Chemical (orch)','Hazardous or Poisonous Substance (hops)','Carbohydrate (carb)','Element, Ion, or Isotope (elii)',
    'Nucleic Acid, Nucleoside, or Nucleotide (nnon)','Indicator, Reagent, or Diagnostic Aid (irda)',
    'Biomedical or Dental Material (bodm)', 'Inorganic Chemical (inch)','Hormone (horm)')
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    columnOfDrugs = -1
    isfirst = False
    #Get all drug annotated content
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
        AnnotationID = res[9]
        #Make sure it extracts drugs from only one column
        if(not isfirst or ColumnN<columnOfDrugs):
            isfirst = True
            columnOfDrugs = ColumnN
        if(ColumnN!=columnOfDrugs):
            continue  
        # Get drug name from the table based on SetID
        sql1 = """Select * from structuredproductlabelmetadata where SetId = '"""+SetId+"'"
        cursor.execute(sql1)
        results2 = cursor.fetchall()
        for res1 in results2:
            drugname = res1[3]
        print drugname
        if(AnnotationConent in drugname.lower()):
            continue
        if(AnnotationConent in ["drug","drugs"]):
            continue

        #QUERY UMLS for ATC codes
        umls_query = QueryDBCalss("localhost", "root", "", "umls", )
        umls_cursor = umls_query.db.cursor()
        sql_umls = "SELECT CODE FROM umls.mrconso where SAB='ATC' and CUI='"+AnnotationID+"'"
        umls_cursor.execute(sql_umls)
        umls_results = umls_cursor.fetchall()
        # Set flag based on ATC:
        #-1: The name was not found in ATC
        # 0: It is a drug/ingrediant name
        # 1: It is a group name
        isGroup = -1
        print "size:"+str(umls_cursor.rowcount)
        for umls_res in umls_results:
            print "res:"+umls_res[0]
            #print umls_res[1]
            if len(umls_res[0])<7:
                isGroup = 1
            if len(umls_res[0])==7:
                isGroup = 0

        #Save output to database
        cursor = queryclass.db.cursor()
        sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,CueRule,isGroup) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(idArticle,SetId,TableId,TableOrder,drugname,AnnotationConent,"DDI Method 1",isGroup))
        queryclass.db.commit()
                   
    print "Done"