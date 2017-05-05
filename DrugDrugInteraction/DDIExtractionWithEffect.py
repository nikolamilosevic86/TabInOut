'''
Created on 13 Sep 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import Cell
import Annotation
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
from AnalyzePattern import GetMean,GetRange
import re

def getCellsByTableID(TableID,db):
    rows = db.getTableCellsWithTableArticleData(TableID)
    cells = []
    for row in rows:
        cell = Cell.Cell()
        cell.idArticle = row[20]
        cell.idPMC = row[24]
        cell.idTable = row[13]
        cell.tableOrder = row[14]
        cell.pragmaticClass = row[22]
        cell.idCell = row[0]
        cell.cellID = row[1]
        cell.cellType = row[2]
        cell.rowN = row[4]
        cell.columnN = row[5]
        cell.Content = row[9]
        cell.Header = row[10]
        cell.Stub = row[11]
        cell.Super_row = row[12]
        cell.HeaderId = row[6]
        cell.StubId = row[7]
        cell.SuperRowId = row[8]
        roles = db.getCellRole(cell.idCell)
        for role in roles:
            if role[0]==1:
                cell.isHeader = True
            if role[0]==2:
                cell.isStub = True
            if role[0]==3:
                cell.isData = True
            if role[0]==4:
                cell.isSuperRow = True
        annotations = db.getCellAnnotation(cell.idCell)
        cell_annotations = []
        if(annotations!= None):
            for ann in annotations:
                Annot = Annotation.Annotation()
                Annot.annotationID = ann[0]
                Annot.Content = ann[1]
                Annot.Start = ann[2]
                Annot.End = ann[3]
                Annot.AnnotationCID = ann[4]
                Annot.AnnotationDesc =ann[5]
                Annot.AgentName = ann[6]
                Annot.AgentType = ann[7]
                Annot.AnnotationURL = ann[8]
                cell_annotations.append(Annot)
        cell.Annotations = cell_annotations
        cells.append(cell)
    return cells
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db_amia", )
    queryclass.CreateAdditionalDDITables()
    cursor = queryclass.db.cursor()
    #Get tables
    sql = """SELECT idArticle,Title,SpecId,idTable,TableOrder,TableCaption,Section FROM table_db_amia.article inner join
     arttable on idArticle=Article_idArticle where Section='34073-7'"""
    #Get cells and annotations that contain potential DDIs
    #sql = """select annotation.Content,AnnotationDescription,Table_idTable,RowN,ColumnN,TableOrder,idArticle,Title,SpecId,
    #AnnotationID from annotation inner join cell on cell.idCell=annotation.Cell_idCell inner join arttable on
    #arttable.idTable=cell.Table_idTable inner join article on article.idArticle = arttable.Article_idArticle
    #where Section='34073-7' and AnnotationDescription  IN ('Pharmacologic Substance (phsu)','Biologically Active Substance (bacs)',
    #'Organic Chemical (orch)','Hazardous or Poisonous Substance (hops)','Carbohydrate (carb)','Element, Ion, or Isotope (elii)',
    #'Nucleic Acid, Nucleoside, or Nucleotide (nnon)','Indicator, Reagent, or Diagnostic Aid (irda)',
    #'Biomedical or Dental Material (bodm)', 'Inorganic Chemical (inch)','Hormone (horm)')
    #"""
    cursor.execute(sql)
    results = cursor.fetchall()
    columnOfDrugs = -1
    isfirst = False
    #Get all drug annotated content
    for res in results:
        idArticle = res[0]
        Title = res[1]
        SpecId = res[2]
        idTable = res[3]
        TableOrder = res[4]
        TableCaption  = res [5]
        Section = res[6]
        PotentialDrugFromHeader = -1
        PotentialEffectFromHeader = -1
        PotentialDrugFromAnnotations = -1
        cells = getCellsByTableID(idTable,queryclass)
        most_annotated = {}
        annotated_cells=[]
        for cell in cells:
            if 'drug' in cell.Content.lower() and cell.rowN<3:
                PotentialDrugFromHeader = cell.rowN
            if 'effect' in cell.Content.lower() and cell.rowN < 3:
                PotentialEffectFromHeader = cell.rowN
            # Get annotations, find the most common column
            for annotation in cell.Annotations:
                if annotation.AnnotationDesc in ['Pharmacologic Substance (phsu)','Biologically Active Substance (bacs)',
                'Organic Chemical (orch)','Hazardous or Poisonous Substance (hops)','Carbohydrate (carb)','Element, Ion, or Isotope (elii)',
                'Nucleic Acid, Nucleoside, or Nucleotide (nnon)','Indicator, Reagent, or Diagnostic Aid (irda)',
                'Biomedical or Dental Material (bodm)', 'Inorganic Chemical (inch)','Hormone (horm)']:
                    annotated_cells.append(cell)
                    if(cell.columnN in most_annotated.keys()):
                        most_annotated[cell.columnN]=most_annotated[cell.columnN]+1
                    else:
                        most_annotated[cell.columnN]=1


        max_annotated_column = 0
        count = 0
        for key in most_annotated.keys():
            if most_annotated[key]>count:
                max_annotated_column=key
                count = most_annotated[key]
        #Get real column for drugs. 3 cases:
        # 1) Drug label+ max annotation same column ->all clear
        # 2) Drug label is not same as max annotations -> trust annotations
        # 3) Drug label not present -> trust annotations
        extract = ''
        effect = ''
        isGroup = -1
        for cell in cells:
            if cell.rowN==max_annotated_column and cell.isHeader==False:
                extract = cell.Content
                if extract=='' or extract==' ' or 'mg/day' in extract:
                    continue

                superRow = False
                for cell2 in cells:
                    if cell2.rowN==cell.rowN and cell2.columnN==cell.columnN+1 and (cell2.Content==cell.Content or cell2.Content==''):
                        superRow = True
                        break
                if superRow:
                    superRow = False
                    continue
                if PotentialEffectFromHeader!=-1:
                    for cell2 in cells:
                        if cell2.rowN==cell.rowN and cell2.columnN==PotentialEffectFromHeader:
                            effect = cell2.Content
                # Get drug name from the table based on SetID
                sql1 = """Select * from structuredproductlabelmetadata where SetId = '"""+SpecId+"'"
                cursor.execute(sql1)
                results2 = cursor.fetchall()
                for res1 in results2:
                    drugname = res1[3]
                    print drugname+' '+extract+' '+effect

                #QUERY UMLS for ATC codes
                umls_query = QueryDBCalss("localhost", "root", "", "umls", )
                umls_cursor = umls_query.db.cursor()
                for annotation in cell.Annotations:
                    if annotation.AnnotationDesc in ['Pharmacologic Substance (phsu)','Biologically Active Substance (bacs)',
                    'Organic Chemical (orch)','Hazardous or Poisonous Substance (hops)','Carbohydrate (carb)','Element, Ion, or Isotope (elii)',
                    'Nucleic Acid, Nucleoside, or Nucleotide (nnon)','Indicator, Reagent, or Diagnostic Aid (irda)',
                    'Biomedical or Dental Material (bodm)', 'Inorganic Chemical (inch)','Hormone (horm)']:

                        sql_umls = "SELECT CODE FROM umls.mrconso where SAB='ATC' and CUI='"+annotation.AnnotationCID+"'"
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
                sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,Effect,CueRule,isGroup) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(idArticle,SpecId,idTable,TableOrder,drugname,extract,effect,"DDI Method 2",isGroup))
                queryclass.db.commit()
                extract = ''
                effect = ''
                isGroup = -1
                   
    print "Done"