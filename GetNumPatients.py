# -*- coding: utf-8 -*-
'''
Created on 26 Feb 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from QueryDBClass import QueryDBCalss
from  Data.Table import Table
import re
if __name__=="__main__":
    queryclass = QueryDBCalss("localhost","root","","table_db" )
    queryclass.ClearCreatedTables()
    queryclass.CreateAdditionalTables()
    results = queryclass.getArticles()
    articleIds = []
    PMCs = []
    for row in results:
        articleIds.append(row[0])
        PMCs.append(row[1])
    del results
    l=0
    #articleIds = [5531]
    for id in articleIds:
        results = queryclass.getArticleTablesWithPragmatic(id,"BaselineCharacteristic")
        tables = []
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
            #print table.tableCaption
            hasValuesInCaption = False
            hasValueInHeader = False
            m = re.search('\\b[0-9]+ [a-z\\-]{0,}[ ]{0,1}(subject[s]{0,1}|patient[s]{0,1}|person[s]{0,1}|individual[s]{0,1}|participant[s]{0,1}|men{0,1}|women{0,1}people[s]{0,1})\\b',table.tableCaption.lower().replace(",",""))
            if("outcome by patient" not in table.tableCaption.lower() and "outcome patient" not in table.tableCaption.lower() ):
                if(m<>None):
                    pat = m.group(0)
                    m2 = re.search('(\d)* ',pat)
                    totalNum = int(m2.group(0))
                    if(totalNum>0):
                        print totalNum
                        Num = totalNum
                        queryclass.SaveAttribute(id,"Total",table.tableId,table.tableOrder,PMCs[l],"Number of Patients","",Num,"Persons","Total") 
                
            m = re.search('\\b(n[? ]{0,1}[^\x00-\x7F]{0,1}=[^\x00-\x7F]{0,1}[? ]{0,1}[0-9]*)\\b',table.tableCaption.lower())
            if(m<>None and m<>''):
                pat = m.group(0)
                armname = "Total"
                m2 = re.search('(\d)+',pat)
                if(m2==None):
                    continue
                Num = m2.group(0)  
                if Num=='' or Num==0:
                    continue
                print Num 
                queryclass.SaveAttribute(id,"Total",table.tableId,table.tableOrder,PMCs[l],"Number of Patients","",Num,"Persons",armname) 
                hasValueInCaption = True
                
            if(hasValuesInCaption):
                continue
            resulta = queryclass.getHeaderCellsContainingListOR(table.tableId, ["%n=%","%n = %","%n =%","%N=%","%N =%","N=%","N =%","n=%",'%N%',"n =%","%n?=%","%N?=%","%(n %","%(n %"])    
            armnamedupl = ''
            for res in resulta:
                if armnamedupl == res[10]+" "+res[9]:
                    continue
                m = re.search('(n[ ?]{0,1}[^\x00-\x7F]{0,1}[=]{0,1}[^\x00-\x7F]{0,1}[ ?]{0,1}[0-9]{1,})\\b',res[9].lower().replace(",",""))
                if(m<>None and m<>''):
                    pat = m.group(0)
                    armname = res[10]+" "+res[9].replace(pat,"")
                    armname = armname.replace("()","")
                    if((armname==" ") or (armname=="")):
                        armname="Total"
                    m2 = re.search('(\d)+',pat)
                    if(m2==None):
                        continue
                    Num = m2.group(0)  
                    if Num=='' or Num==str(0):
                        continue
                    print Num 
                    armnamedupl = res[10]+" "+res[9]
                    queryclass.SaveAttribute(id,"Total",table.tableId,table.tableOrder,PMCs[l],"Number of Patients","",Num,"Persons",armname) 
                
                    hasValueInHeader = True
            if(hasValueInHeader):
                continue
            resulta = queryclass.getHeaderCellsContainingListOR(table.tableId, ["No. of patient%","no. of patient%","No. patient%","no. patient%", "no patient%","No patient%","num patients", "Num patients"])    
            armnamedupl = ''
            for res in resulta:
                if armnamedupl == res[10]+" "+res[9]:
                    continue
                m2 = re.search('(\d)+',res[9])
                if(m2==None):
                    continue
                Num = m2.group(0)  
                if Num=='' or Num==str(0):
                    continue
                print Num 
                armnamedupl = res[10]+" "+res[9]
                queryclass.SaveAttribute(id,"Total",table.tableId,table.tableOrder,PMCs[l],"Number of Patients","",Num,"Persons",armname) 
                
                hasValueInHeader = True

            if(hasValueInHeader):
                continue   
            resultas = queryclass.getCellsContainingInStubListOR(table.tableId, ["%umber of patients%","% patients%","% patients number%","Total N patients","%otal\nN\npatient%",
                                                                                 "%no of patients%","number","n","n (%","n=","Number","%otal patient%","%atient number",
                                                                                 "%otal Patient%","%treated%","%o. of patients%","%ubjects%","Patients (%","Patients","patients",
                                                                                 "%otal individual%","%atients, n%","Number (%","%umber of Subject%","%ample%","total","Total",
                                                                                 "%umber of subject%","%umber of Pts%","%umber of pts%","%o. of pts","%otal Number%","%population","%otal number%","%ntered","%nrolled%","%otal participant%","%otal Participant%","%valuable"])
            
            #resultas = queryclass.getCellsContainingInStubListOR(table.tableId, ["%o. of pts%","%otal Number%"])
            
            
            armnamedupl = ''
            for res in resultas:
                if armnamedupl!='' and armnamedupl == res[10]:
                    continue
                if res[12] != None and( "median" in res[12].lower() or "mean" in res[12].lower() or "history" in res[12].lower()):
                    continue
                if res[11] != None and( "%" in res[11].lower() or "p value" in res[11].lower()):
                    continue
                if  "(%)" in res[10].lower() or"% ;" in res[10].lower() or "p value" in res[10].lower() or "ale" in res[10].lower():
                    continue
                m2 = re.search('(\d)+',res[9].replace(",",""))
                if(m2==None):
                    continue
                Num = m2.group(0)  
                if Num=='' or Num==str(0):
                    continue
                print Num 
                armname = armnamedupl = res[10]
                if armname == '':
                    armname = res[10]+" "+res[9].replace(str(Num),"")
                    armname = armname.replace("()","")
                if armname == '' or  armname == ' ':
                    armname = 'Total'
                queryclass.SaveAttribute(id,"Total",table.tableId,table.tableOrder,PMCs[l],"Number of Patients","",Num,"Persons",armname) 
                
            
            #armnamedupl = ''
            #resultas = queryclass.getCellsContainingInHeaderListOR(table.tableId, ["%umber of patients","%n%","%N%"])
            #for res in resultas:
            #    armname=res[11]
            #    if ( "n " not in res[10].lower()):
            #        continue
            #    if ( "an " in res[10].lower() or "in " in res[10].lower() or "en " in res[10].lower() or "on "in res[10].lower() or "un " in res[10].lower()):
            #        continue
            #    value = res[9]
            #    m2 = re.search('(\d)+',value.replace(",",""))
            #    if(m2==None):
            #        continue
            #    Num = m2.group(0)  
            #    if Num=='' or Num==str(0):
            #        continue
            #    print Num 
            #    armid = queryclass.SaveArm(armname, id,table.tableId) 
            #    queryclass.SaveAttribute(armid, "Number of Patients", Num)
        l=l+1

    print "Done"
    
    #table 4038 has no cellroles
    #document 2949 collects more
    #3204 classifier fault