'''
Created on 22 Aug 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
from AnalyzePattern import GetMean,GetRange
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db", )
    queryclass.DeleteAttribute("Age")
    queryclass.CreateAdditionalTables()
    results = queryclass.getCellsWithMetaMapAnnotation("BaselineCharacteristic","orga")
    lastCellID = -1
    for res in results:
        CellID = res[0]
        if(CellID==lastCellID):
            continue
        TableID = res[3]
        RowN = res[4]
        ColumtnN = res[5]
        Content = res[9]
        Header  = res [10]
        Stub = res[11]
        SuperRow = res[12]
        AnnotationContent = res[14]
        AnnotationDesc = res[19]
        TableOrder = res[28]
        idArt = res[34]
        PMC = res[38]
        if PMC=='1090597':#'1488867':
            print 'right PMC'
        #CellRole = res[51]
        lastCellID = CellID
        rowRes = queryclass.getCellsFromTableRowRow(TableID,RowN)
        
       # l = 0

        for res in rowRes:
            m2 = {}
                #m2 = re.search('[\d\.]+',res[9])
            m2 = GetMean(res[9],m2)
            if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and "max" in m2.keys() and m2["mean"]!=None and m2["min"]!=None and m2["max"]!=None):
                print "has all"
            else:
                m2 = GetRange(res[9],m2)
            if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and m2["mean"]==m2["min"]):
                del m2["mean"]
            if(m2==None):
                continue
            if(m2==None or ("mean" in m2.keys() and (m2["mean"]=='.'or m2["mean"]=='..'))):
                continue
            content = re.sub(r'[^\x00-\x7F]','[spec]',res[9])
            content = content.replace('?','[spec]')
            if "range" in res[10].lower():
                m2 = GetRange(res[9],m2)
                
            if("sd" in res[10].lower() and 'mean' not in res[10].lower()) or "p-value" in res[10].lower() or "p" ==res[10].lower():
                continue
            m3 = re.search('\\b(p)\\b',res[10].lower())
            m4 = re.search('\\b[\/](p)\\b',res[10].lower())
            if m3!=None and m4==None:
                continue
            
            if(res[11]!=None and "onset" in res[11].lower()):
                continue
            if(content!=None and res[11]!=None and ('%' in content or 'day' in content or 'min' in content or '<' in content or '>' in content or '=' in content or '?' in content or '<' in res[11] or '>' in res[11] or '=' in res[11]or 'min' in res[11].lower() or 'max' in res[11].lower())):
                continue
            unit = 'years'
            if(res[11]!=None and ("months" in res[11].lower() or "months" in res[9].lower())):
                unit = 'months'
                    #totalNum = totalNum/12
            if(res[11]!=None and ("weeks" in res[11].lower() or "weeks" in res[9].lower())):
                unit = 'weeks'
                    #totalNum = totalNum/52
            totalNum = 0.0
            if(m2!= None and "mean" in m2.keys() and m2["mean"]!=None):
                totalNum = float(m2["mean"])
            if(m2== None):
                continue
            print AnnotationContent+':'+str(totalNum)+" "+unit
                
            
            if("mean" in m2.keys()):
                queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"mean",float(m2["mean"]),unit,res[10],"MetaMap","MetaMap") 
            if("sd" in m2.keys()):
                queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"sd",float(m2["sd"]),unit,res[10],"MetaMap","MetaMap") 
            if("min" in m2.keys()):
                queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:minimum",float(m2["min"]),unit,res[10],"MetaMap","MetaMap") 
            if("max" in m2.keys()):
                queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:maximum",float(m2["max"]),unit,res[10],"MetaMap","MetaMap")  
           # l = l+1 
    print "Done normal, going super-row"
        # if row super-row - take the rows bellow   
    results = queryclass.getCellsWithMetaMapAnnotationWithRole("BaselineCharacteristic","orga",4)
    lastCellID = -1
    for res in results:
        CellID = res[0]
        if(CellID==lastCellID):
            continue
        TableID = res[3]
        RowN = res[4]
        ColumtnN = res[5]
        Content = res[9]
        Header  = res [10]
        Stub = res[11]
        SuperRow = res[12]
        AnnotationContent = res[14]
        AnnotationDesc = res[19]
        TableOrder = res[28]
        idArt = res[34]
        PMC = res[38]
        if PMC=='1488867':#'1488867':
            print 'right PMC'
        CellRole = res[51]
        lastCellID = CellID
        row = RowN+1
        CellRole = 3
        SuperRowOfInterest = Content
        SuperRow = SuperRowOfInterest
        while CellRole!=4 and SuperRowOfInterest in SuperRow and row<50:
            rowRes = queryclass.getCellsFromTableRowRow(TableID,row)
            for res in rowRes:
                SuperRow = res[12]
                CellRole = res[14]
                m2 = {}
                m2 = GetMean(res[9],m2)
                if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and "max" in m2.keys() and m2["mean"]!=None and m2["min"]!=None and m2["max"]!=None):
                    print "has all"
                else:
                    m2 = GetRange(res[9],m2)
                if(m2!=None and "mean" in m2.keys() and "min" in m2.keys() and m2["mean"]==m2["min"]):
                    del m2["mean"]
                if(m2==None):
                    continue
                if(m2==None or ("mean" in m2.keys() and (m2["mean"]=='.'or m2["mean"]=='..'))):
                    continue
                content = re.sub(r'[^\x00-\x7F]','[spec]',res[9])
                content = content.replace('?','[spec]')
                if "range" in res[10].lower():
                    m2 = GetRange(res[9],m2)
                
                if("sd" in res[10].lower() and 'mean' not in res[10].lower()) or "p-value" in res[10].lower() or "p" ==res[10].lower():
                    continue
                m3 = re.search('\\b(p)\\b',res[10].lower())
                m4 = re.search('\\b[\/](p)\\b',res[10].lower())
                if m3!=None and m4==None:
                    continue
                if(res[11]!=None and "onset" in res[11].lower()):
                    continue
                if(content!=None and res[11]!=None and ('%' in content or 'day' in content or 'min' in content or '<' in content or '>' in content or '=' in content or '?' in content or '<' in res[11] or '>' in res[11] or '=' in res[11]or 'min' in res[11].lower() or 'max' in res[11].lower())):
                    continue
                unit = 'years'
                if(res[11]!=None and ("months" in res[11].lower() or "months" in res[9].lower())):
                    unit = 'months'
                    #totalNum = totalNum/12
                if(res[11]!=None and ("weeks" in res[11].lower() or "weeks" in res[9].lower())):
                    unit = 'weeks'
                    #totalNum = totalNum/52
                totalNum = 0.0
                if(m2!= None and "mean" in m2.keys() and m2["mean"]!=None):
                    totalNum = float(m2["mean"])
                if(m2== None):
                    continue
                print AnnotationContent+':'+str(totalNum)+" "+unit
                
            
                if("mean" in m2.keys()):
                    queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"mean",float(m2["mean"]),unit,res[10],"MetaMap","MetaMap") 
                if("sd" in m2.keys()):
                    queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"sd",float(m2["sd"]),unit,res[10],"MetaMap","MetaMap") 
                if("min" in m2.keys()):
                    queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:minimum",float(m2["min"]),unit,res[10],"MetaMap","MetaMap") 
                if("max" in m2.keys()):
                    queryclass.SaveExtracted(idArt,TableID,TableOrder,PMC,AnnotationContent,"Range:maximum",float(m2["max"]),unit,res[10],"MetaMap","MetaMap")                
            row = row+1
                   
    print "Done"