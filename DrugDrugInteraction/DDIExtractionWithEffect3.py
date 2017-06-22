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
    queryclass = QueryDBCalss("localhost","root","","ddi_data", )
    queryclass.CreateAdditionalDDITables()
    cursor = queryclass.db.cursor()
    #Get tables
    sql = """SELECT idArticle,Title,SpecId,idTable,TableOrder,TableCaption,Section FROM ddi_data.article inner join
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
        drugcolumns = []
        effectcolums = []
        spanningRows = []
        pastCell = ''
        numOfColumns = 0
        NotCalcNumOfColumns = True
        cellid = 0
        drugset = -1
        hasHeader = False
        if cells[0].isHeader:
            hasHeader = True

        DrugColumnsSet = False
        for cell in cells:
            if drugset>-1 and cell.rowN>0:
                DrugColumnsSet = True
            if(cell.rowN==0 and NotCalcNumOfColumns):
                numOfColumns = numOfColumns+1
            if cell.rowN==1:
                NotCalcNumOfColumns = False
            if hasHeader:
                if ("drug" in cell.Content.lower() or "interacting agent" in cell.Content.lower() or'coadministered' in  cell.Content.lower() or 'co-administered' in  cell.Content.lower()) and ('effect' not in cell.Content.lower() and 'dose' not in cell.Content.lower() and 'exposure' not in cell.Content.lower() and 'recommendation' not in cell.Content.lower()) and cell.isHeader and DrugColumnsSet==False:
                    drugcolumns.append(cell.columnN)
                    drugset = cell.rowN
                if "effect" in cell.Content.lower() and cell.isHeader and DrugColumnsSet==False:
                    effectcolums.append(cell.columnN)
            else:
                if ("drug" in cell.Content.lower() or 'coadministered' in  cell.Content.lower() or 'co-administered' in  cell.Content.lower()) and ('effect' not in cell.Content.lower() and 'dose' not in cell.Content.lower() and 'exposure'  not in cell.Content.lower() and 'recommendation' not in cell.Content.lower()) and cell.rowN<3 and DrugColumnsSet==False:
                    drugcolumns.append(cell.columnN)
                    drugeffectset = cell.rowN
                if "effect" in cell.Content.lower() and cell.rowN<3 and DrugColumnsSet==False:
                    effectcolums.append(cell.columnN)
            if cell.columnN==0 and NotCalcNumOfColumns==False:
                isSpanning = True
                for i in range(0,numOfColumns-1):
                    if(cellid+i+1<len(cells) and cells[cellid+i].Content.lower()!=cells[cellid+i+1].Content.lower()):
                        j=cellid
                        numCellsInRow=0
                        numCellsZero = 0
                        while(cellid+i+1<len(cells) and j<len(cells) and cells[j].rowN==cells[cellid+i].rowN):
                            if cells[j]=='':
                                numCellsZero=numCellsZero+1
                            numCellsInRow = numCellsInRow+1
                            j=j+1
                        if numCellsInRow>0 and (numCellsZero*1.0)/(numCellsInRow*1.0)<0.5:
                            isSpanning = False
                if isSpanning:
                    spanningRows.append(cell.rowN)
            cellid = cellid+1

        drugcolumns = set(drugcolumns)
        effectcolums = set(effectcolums)
        spanningRows = set(spanningRows)
        isGroup = -1
        for i in range(0,len(cells)):
            extract = ''
            effect = ''
            if cells[i].rowN in spanningRows or cells[i].rowN==0 or cells[i].rowN==drugset:
                continue
            if cells[i].columnN in drugcolumns:
                extract = cells[i].Content
                if extract=='':
                    continue
                for k in range(0,5):
                    if i+k<len(cells) and cells[i+k].columnN in effectcolums:
                        if cells[k+i].Content == "":
                            continue
                        effect = cells[k+i].Content
            # Get drug name from the table based on SetID
                sql1 = """Select * from structuredproductlabelmetadata where SetId = '"""+SpecId+"'"
                cursor.execute(sql1)
                results2 = cursor.fetchall()
                for res1 in results2:
                    drugname = res1[3]
                    if extract.strip() =="" or extract.strip()==" ":
                        continue
                    print drugname+' '+extract+' '+effect
                drugs = extract.split(":")
                if len(drugs)>1:
                    ex1 = drugs[0]
                    ex2 = drugs[1]
                    cursor = queryclass.db.cursor()
                    sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,Effect,CueRule,isGroup) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (
                    idArticle, SpecId, idTable, TableOrder, drugname, ex1, effect, "DDI Method 3", 1))
                    queryclass.db.commit()
                    extract = ''
                    isGroup = -1
                    onedrugs = re.split(";|,|\n",ex2)
                    for onedrug in onedrugs:
                        cursor = queryclass.db.cursor()
                        sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,Effect,CueRule,isGroup) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql, (
                            idArticle, SpecId, idTable, TableOrder, drugname, onedrug, effect, "DDI Method 3", -1))
                        queryclass.db.commit()
                        isGroup = -1
                else:
                    onedrugs = re.split(";|,|\n", extract)
                    for onedrug in onedrugs:
                        cursor = queryclass.db.cursor()
                        sql = "INSERT into ddiinfo (documentId, SpecId,idTable,TableName,Drug1,Drug2,Effect,CueRule,isGroup) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql, (
                            idArticle, SpecId, idTable, TableOrder, drugname, onedrug, effect, "DDI Method 3", -1))
                        queryclass.db.commit()
                        isGroup = -1
                effect=''
                extract = ''
                   
    print "Done"