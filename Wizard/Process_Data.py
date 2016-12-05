'''
Created on 13 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import FileManipulationHelper
import QueryDBClass
import re
import Cell
import Annotation

Source = ''


def CheckSemTermListUsingRegex2(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    global Source
    ContainsValue = False
    string_pos = 0
    if(look_header):
        for item in List:
            if Header == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Header)
            if(m1!=None):
                if string_pos<=m1.start():
                    string_pos = m1.start()
                    ContainsValue = True
                    Source = Stub
    if(look_stub):
        for item in List:
            if(Stub == None or item.replace('\n','') ==''):
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Stub)
            if(m1!=None):
                if string_pos<=m1.start():
                    string_pos = m1.start()
                    ContainsValue = True
                    Source = Header
    if(look_superrow):
        for item in List:
            if Super_row == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Super_row)
            if(m1!=None):
                if string_pos<=m1.start():
                    string_pos = m1.start()
                    ContainsValue = True
                    Source = "h:"+Header+"; s:"+Stub
    if(look_data):
        for item in List:
            if Data == None or item.replace('\n','') =='':
                continue
            regex = '\\b('+item.replace('\n','')+')\\b'
            m1 = re.search(regex,Data)
            if(m1!=None):
                if string_pos<=m1.start():
                    string_pos = m1.start()
                    ContainsValue = True
                    Source = "h:"+Header+"; s:"+Stub
    return ContainsValue

def CheckSemTermListUsingRegex(look_header,look_stub,look_superrow,look_data,BigList,Header,Stub,Super_row,Data):
    global Source
    ContainsValue = False
    string_pos = 0
    for List in BigList:
        if(look_header):
            for item in List:
                if Header == None or item.replace('\n','') =='':
                    continue
                regex = '\\b('+item.replace('\n','')+')\\b'
                m1 = re.search(regex,Header)
                if(m1!=None):
                    if string_pos<=m1.start():
                        string_pos = m1.start()
                        ContainsValue = True
                        Source = Stub
        if(look_stub):
            for item in List:
                if(Stub == None or item.replace('\n','') ==''):
                    continue
                regex = '\\b('+item.replace('\n','')+')\\b'
                m1 = re.search(regex,Stub)
                if(m1!=None):
                    if string_pos<=m1.start():
                        string_pos = m1.start()
                        ContainsValue = True
                        Source = Header
        if(look_superrow):
            for item in List:
                if Super_row == None or item.replace('\n','') =='':
                    continue
                regex = '\\b('+item.replace('\n','')+')\\b'
                m1 = re.search(regex,Super_row)
                if(m1!=None):
                    if string_pos<=m1.start():
                        string_pos = m1.start()
                        ContainsValue = True
                        Source = "h:"+Header+"; s:"+Stub
        if(look_data):
            for item in List:
                if Data == None or item.replace('\n','') =='':
                    continue
                regex = '\\b('+item.replace('\n','')+')\\b'
                m1 = re.search(regex,Data)
                if(m1!=None):
                    if string_pos<=m1.start():
                        string_pos = m1.start()
                        ContainsValue = True
                        Source = "h:"+Header+"; s:"+Stub
    return ContainsValue

def CheckBListUsingRegex(look_header,look_stub,look_superrow,look_data,List,Header,Stub,Super_row,Data):
    ValidCandidate = True
    if(look_header):
        for item in List:
            if Header == None or item.replace('\n','') =='':
                continue
            item = item.replace('\n','')
            regex = ''+item+''
            m1 = re.search(regex,Header)
            if(m1!=None):
                ValidCandidate = False
    if(look_stub):
        for item in List:
            if Stub == None or item.replace('\n','') =='':
                continue
            regex = ''+item.replace('\n','')+''
            m1 = re.search(regex,Stub)
            if(m1!=None):
                ValidCandidate = False
    if(look_superrow):
        for item in List:
            if Super_row == None or item.replace('\n','') =='':
                continue
            regex = ''+item.replace('\n','')+''
            m1 = re.search(regex,Super_row)
            if(m1!=None):
                ValidCandidate = False
    if(look_data):
        for item in List:
            if Data == None or item.replace('\n','') =='':
                continue
            regex = ''+item.replace('\n','')+''
            m1 = re.search(regex,Data)
            if(m1!=None):
                ValidCandidate = False
    
    return ValidCandidate

def CheckUnits(Header,Stub,SuperRow,Data,defaultUnit,PossibleUnits):
    UnitSelected = defaultUnit
    for unit in PossibleUnits:
        unit = unit.replace('\n','')
        if Header != None:
            m1 = re.search('\\b('+unit+")\\b",Header)
            if(m1!=None):
                UnitSelected = unit
                break
        if Stub !=None:
            m1 = re.search('\\b('+unit+")\\b",Stub)
            if(m1!=None):
                UnitSelected = unit
                break
        if SuperRow != None:
            m1 = re.search('\\b('+unit+")\\b",SuperRow)
            if(m1!=None):
                UnitSelected = unit
                break
        if Data != None:
            m1 = re.search('\\b('+unit+")\\b",Data)
            if(m1!=None):
                UnitSelected = unit
                break
    return UnitSelected

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
        
def getHeaderCells(HeaderId,Cells,heads):
    if HeaderId == None:
        return heads
    for cell in Cells:
        if cell.cellID==HeaderId:
            heads.append(cell)
            heads = getHeaderCells(cell.HeaderId,Cells,heads)
    return heads

def getStubCells(StubId,Cells,stubs):
    if StubId == None:
        return stubs
    for cell in Cells:
        if cell.cellID==StubId:
            stubs.append(cell)
            stubs = getHeaderCells(cell.StubId,Cells,stubs)
    return stubs

def getSuperRowCells(SuperRowId,Cells,superrows):
    if SuperRowId == None:
        return superrows
    for cell in Cells:
        if cell.cellID==SuperRowId:
            superrows.append(cell)
            superrows = getHeaderCells(cell.SuperRowId,Cells,superrows)
    return superrows

def ProcessDataBase(project_name,rules):
    global Source
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    for rule in rules:
        WhiteWordList = []
        WhiteIDList = []
        WhiteDescList = []
        BlackWordList = []
        BlackIDList = []
        BlackDescList = []
        # Get different cue lists from one big list containing annotations and lexical cues
        for word in rule.WhiteList:
            if('[annID]:' in word):
                if(word[8:]!=''):
                    WhiteIDList.append(word[8:])
            elif('[annType]:'in word):
                if(word[10:]!=''):
                    WhiteDescList.append(word[10:])
            elif('[word]:'in word):
                if(word[7:]!=''):
                    WhiteWordList.append(word[7:])
            else:
                if(word!=''):
                    WhiteWordList.append(word)
                
        for word in rule.BlackList:
            if('[annID]:' in word):
                if (word[8:] != ''):
                    BlackIDList.append(word[8:])
            elif('[annType]:'in word):
                if (word[10:] != ''):
                    BlackDescList.append(word[10:])
            elif('[word]:'in word):
                if (word[7:] != ''):
                    BlackWordList.append(word[7:])
            else:
                if (word != ''):
                    BlackWordList.append(word)
            # Get tables that contain something from white list in it
        tabres = db.getRelevantTables(WhiteWordList,WhiteIDList,WhiteDescList,rule.PragmaticClass)
        tables = []
        for res in tabres:
            tables.append(res[0])
        for table in tables:
        #Get Table cells with all the annotations
            cells = getCellsByTableID(table,db)
            #Now the data should be filtered
            for cell in cells:
                extractData = True
                extracted = False
                selectCell = False
                CueFoundInHeader = False
                CueFoundInStub = False
                CueFoundInSuperRow = False
                CueFoundInData = False

                #Check white list against data cells
                if rule.wl_look_data:
                    for word in WhiteWordList:
                        if cell.Content != None:
                            if(word in cell.Content):
                                selectCell = True
                                CueFoundInData = True
                    for word in WhiteDescList:
                        for ann in cell.Annotations:
                            if ann.AnnotationDesc == word:
                                selectCell = True
                                CueFoundInData = True
                    for word in WhiteIDList:
                        for ann in cell.Annotations:
                            if ann.AnnotationCID == word:
                                selectCell = True
                                CueFoundInData = True

                # Check white list against heades
                if rule.wl_look_header:
                    for word in WhiteWordList:
                        if cell.Header != None:
                            if (word in cell.Header):
                                selectCell = True
                                CueFoundInHeader = True
                    idHeader = cell.HeaderId
                    heads = []
                    heads = getHeaderCells(cell.HeaderId,cells,heads)
                    for head in heads:
                        for word in WhiteDescList:
                            for ann in head.Annotations:
                                if ann.AnnotationDesc==word:
                                    selectCell = True
                                    CueFoundInHeader = True
                        for word in WhiteIDList:
                            for ann in head.Annotations:
                                if ann.AnnotationCID == word:
                                    selectCell = True
                                    CueFoundInHeader = True

                # Check white list against stub
                if rule.wl_look_stub:
                    for word in WhiteWordList:
                        if cell.Stub != None:
                            if (word in cell.Stub):
                                selectCell = True
                                CueFoundInStub = True
                    idStub = cell.StubId
                    stubs = []
                    stubs = getStubCells(cell.StubId, cells, stubs)
                    for stub in stubs:
                        for word in WhiteDescList:
                            for ann in stub.Annotations:
                                if ann.AnnotationDesc == word:
                                    selectCell = True
                                    CueFoundInStub = True
                        for word in WhiteIDList:
                            for ann in stub.Annotations:
                                if ann.AnnotationCID == word:
                                    selectCell = True
                                    CueFoundInStub = True

                # Check white list against super-row
                if rule.wl_look_superrow:
                    for word in WhiteWordList:
                        if cell.Super_row != None:
                            if (word in cell.Super_row):
                                selectCell = True
                                CueFoundInSuperRow = True
                    idSuperRow = cell.SuperRowId
                    superrows = []
                    superrows = getStubCells(cell.SuperRowId, cells, superrows)
                    for superrow in superrows:
                        for word in WhiteDescList:
                            for ann in superrow.Annotations:
                                if ann.AnnotationDesc == word:
                                    selectCell = True
                                    CueFoundInSuperRow = True
                        for word in WhiteIDList:
                            for ann in superrow.Annotations:
                                if ann.AnnotationCID == word:
                                    selectCell = True
                                    CueFoundInSuperRow = True

#=============================================================================================
                # Check black list against data cells
                if rule.bl_look_data:
                    for word in BlackWordList:
                        if cell.Content != None:
                            if (word in cell.Content):
                                selectCell = False
                    for word in BlackDescList:
                        for ann in cell.Annotations:
                            if ann.AnnotationDesc == word:
                                selectCell = False
                    for word in BlackIDList:
                        for ann in cell.Annotations:
                            if ann.AnnotationCID == word:
                                selectCell = False


                # Check black list against heades
                if rule.bl_look_header:
                    for word in BlackWordList:
                        if cell.Header != None:
                            if (word in cell.Header):
                                selectCell = False
                    idHeader = cell.HeaderId
                    heads = []
                    heads = getHeaderCells(cell.HeaderId, cells, heads)
                    for head in heads:
                        for word in BlackDescList:
                            for ann in head.Annotations:
                                if ann.AnnotationDesc == word:
                                    selectCell = False
                        for word in BlackIDList:
                            for ann in head.Annotations:
                                if ann.AnnotationCID == word:
                                    selectCell = False

                                                # Check white list against stub
                if rule.bl_look_stub:
                    for word in BlackWordList:
                        if cell.Stub != None:
                            if (word in cell.Stub):
                                selectCell = False
                    idStub = cell.StubId
                    stubs = []
                    stubs = getStubCells(cell.StubId, cells, stubs)
                    for stub in stubs:
                        for word in BlackDescList:
                            for ann in stub.Annotations:
                                if ann.AnnotationDesc == word:
                                    selectCell = False
                        for word in BlackIDList:
                            for ann in stub.Annotations:
                                if ann.AnnotationCID == word:
                                    selectCell = False

                # Check white list against super-row
                if rule.bl_look_superrow:
                    for word in BlackWordList:
                        if cell.Super_row != None:
                            if (word in cell.Super_row):
                                selectCell = False
                    idSuperRow = cell.SuperRowId
                    superrows = []
                    superrows = getStubCells(cell.SuperRowId, cells, superrows)
                    for superrow in superrows:
                        for word in BlackDescList:
                            for ann in superrow.Annotation:
                                if ann.AnnotationDesc == word:
                                    selectCell = False
                        for word in BlackIDList:
                            for ann in superrow.Annotation:
                                if ann.AnnotationCID == word:
                                    selectCell = False

                if selectCell:
                    FoundSemantics = False
                    AllSemSaved = False
                    # Iterate trought all the patterns
                    for syn_rule in rule.PatternList:
                        if(AllSemSaved ==True):
                            break
                        # check pattern
                        pattern = unicode(syn_rule.regex.replace('\n',''),'utf-8')
                        m = re.search(pattern,cell.Content,re.UNICODE)
                        # in case pattern is not found continue to the next one
                        if m == None:
                            continue
                        c = 0
                        contains_term = False
                        last_sem_extracted = -1
                        # Itterate semantics for each pattern rule (syntactic rule)
                        for sem in syn_rule.SemanticValues:
                            if contains_term and sem.Semantics=='mean':
                                contains_term = False
                                FoundSemantics = False
                                continue
                            if(AllSemSaved ==True):
                                break
                            if last_sem_extracted >= sem.position:
                                continue
                            # extract value
                            value = m.group(sem.position)
                            #Checking terms in case there are multiple semantics for certain group
                            if len(sem.SemTermList)>0:
                                contains_term = CheckSemTermListUsingRegex(True,True,True,False,sem.SemTermList,cell.Header,cell.Stub,cell.Super_row,cell.Content)
                                if(contains_term):
                                    semValue  = sem.Semantics
                                    FoundSemantics = True
                            # Getting semantics for certain group
                            if len(sem.SemTermList)==0:
                                semValue  = sem.Semantics
                                FoundSemantics = True
                            c = c+1
                            if FoundSemantics:
                                syn_rule_name = syn_rule.name
                                # Be a bit smart for generating Source
                                if(CueFoundInHeader and rule.data_in_data):
                                    Source = cell.Stub
                                else:
                                    Source = cell.Header
                                # Get unit
                                Unit = CheckUnits(cell.Header, cell.Stub, cell.Super_row, cell.Content, rule.DefaultUnit, rule.PossibleUnits)
                                #Save the value to the database
                                db.SaveExtracted(cell.idArticle,cell.idTable,cell.tableOrder,cell.idPMC,rule.ClassName,semValue,value,Unit,Source,rule.RuleName,syn_rule_name)
                                last_sem_extracted = sem.position
                                FoundSemantics = False
                                if(c == len(syn_rule.SemanticValues)):
                                    AllSemSaved = True



            #print cells
    print "Finished!!!"
    print "Done!!!!"
    #FinishScreen()
    
def GetExtractedData(project_name):
    DBSettings = FileManipulationHelper.LoadDBConfigFile(project_name)
    db = QueryDBClass.QueryDBCalss(DBSettings['Host'],DBSettings['User'],DBSettings['Pass'],DBSettings['Database'])
    extracted = db.getExtracted()
    return extracted
    

