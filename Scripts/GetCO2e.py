from QueryDBClassESG import QueryDBCalssESG
from  Data.Table import Table
from AnalyzePattern import GetMean, GetRange
import re

def getContentType(Content):
    digits = 0.0
    letters = 0.0
    total = len(Content)
    specchars = 0.0
    numspec = 0.0
    for c in Content.lower():
        if c in ['0','1','2','3','4','5','6','7','8','9']:
            digits = digits +1
        elif c in ['.',',',')','(','[',']','+','-','>','<','%']:
            numspec = numspec + 1
        elif c in ['!','"','$','^','&','*','@','~','#',';',':','|','\\','?','/']:
            specchars = specchars + 1
        else:
            letters = letters + 1

    if (digits/total)>0.8:
        return 'Numeric'
    else:
        return 'Text'


if __name__ == "__main__":
    queryclass = QueryDBCalssESG("localhost", "root", "", "sci_table", )

    queryclass.CreateAdditionalTablesESG()
    queryclass.DeleteAttribute("CO2e")
    results = queryclass.getArticles()
    articleIds = []
    articles = []
    for row in results:
        articleIds.append(row[0])
        articles.append(row[5])
    del results
    # articleIds = [1252]
    l = 0
    for id in articleIds:
        results = queryclass.getArticleTables(id)
        tables = []
        article = articles[l]
        for t in results:
            table = Table()
            table.tableId = t[0]
            table.tableOrder = t[1]
            table.tableCaption = t[2]
            table.tableFooter = t[3]
            table.StructureType = t[4]
            table.PrgamaticType = t[5]
            table.hasXML = t[6]
            table.articleId = t[7]
            tables.append(table)
            resulta = queryclass.getTableCells(table.tableId)
            for res in resulta:
                candidate = False
                cellType = res[2]
                cellRow = res[4]
                cellColumn = res[5]
                cellContent = res[9]
                cellHeader = res[10]
                cellStub = res[11]
                cellSuperRow = res[12]
                resulta2 = queryclass.getCellsFromTableRow(table.tableId,cellRow)
                FullStub = ''
                FullHead = ''
                Year = ''
                for res2 in resulta2:
                    cell2Type = res2[2]
                    cell2Row = res2[4]
                    cell2Column = res2[5]
                    cell2Content = res2[9]
                    cell2Header = res2[10]
                    cell2Stub = res2[11]
                    cell2SuperRow = res2[12]
                    if cell2Type == 'Text':
                        FullStub = FullStub +" ; "+ cell2Content
                    if cell2Column>cellColumn:
                        break

                    m = re.search(ur'(co2 emission)|(co2e)|(greenhouse gas)|(green house)',cell2Content.lower())
                    if (m != None):
                        candidate = True
                    if candidate == True:
                        m = re.search(ur'(change)|(some other bad word)', cell2Content)
                        if (m != None):
                            candidate = False
                    if candidate ==True:
                        value = re.search(ur'([1-9]{1,}\d{0,3}[,]*\d{0,3}[,]*\d{0,3}[.]{0,1}\d{1,3})',cellContent)
                        if(value== None):
                            continue
                        val = value.group(0)
                        val = val.replace(',','')
                        ccells = queryclass.getCellsInColumn(table.tableId,cellColumn)
                        for colCell in ccells:
                            cell3Type = colCell[2]
                            cell3Row = colCell[4]
                            cell3Column = colCell[5]
                            cell3Content = colCell[9]
                            cell3Header = colCell[10]
                            cell3Stub = colCell[11]
                            cell3SuperRow = colCell[12]
                            if cell3Row<cellRow and (cell3Type=='Text' or '2012' in cell3Content or '2013' in cell3Content or '2014' in cell3Content or '2015' in cell3Content or '2016' in cell3Content or '2017' in cell3Content or '2018' in cell3Content or '2019' in cell3Content
                                                     or '12' in cell3Content or '13' in cell3Content or '14' in cell3Content or '15' in cell3Content or '16' in cell3Content or '17' in cell3Content or '18' in cell3Content or '19' in cell3Content):
                                FullHead = FullHead +" ; "+ cell3Content
                                if ('2012' in cell3Content or '2013' in cell3Content or '2014' in cell3Content or '2015' in cell3Content or '2016' in cell3Content or '2017' in cell3Content or '2018' in cell3Content or '2019' in cell3Content
                                                     or '12' in cell3Content or '13' in cell3Content or '14' in cell3Content or '15' in cell3Content or '16' in cell3Content or '17' in cell3Content or '18' in cell3Content or '19' in cell3Content):
                                    yrmatch = re.search(ur'(\d{2,4})',cell3Content)
                                    if(yrmatch!=None):
                                        Year = yrmatch.group(0)

                    if candidate == True:
                        queryclass.SaveAttributeESG(id, "Value", table.tableId, table.tableOrder, article, "CO2e", Year,
                                                                                              float(val), "", FullHead,FullStub)
                        print article+str(Year)+":"+str(val)
                        break

        l = l + 1
    print "Done"