'''
Created on 10 Mar 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import MySQLdb
def processTable(tableid,clas):
    print tableid
    db = MySQLdb.connect("localhost","root","","table_db")
    containsDemographic = 0
    containsPatientsCap = 0
    containsPatientsCell = 0
    containsBaseline = 0
    containsAge = 0
    containsN = 0
    containsTrialCap = 0
    containsCharacteristicCap = 0
    containsEglibility= 0
    containsInclusionExclusionCell=0
    containsToxicity = 0
    containsHaematologic = 0
    containsCriteria = 0
    NoColumn = 0
    NoRows = 0
    ContainsInclusion = 0
    ContainsExclusion = 0
    CellNumeric = 0
    CellText = 0
    CellEmpty = 0
    CellSemiNumeric =0
    TotalCellNo = 0
    ContainsAdverse = 0
    ContainsSideEffect = 0
    ContainsSignOrSymptomAnnotation = 0
    Caption = ""
    cursor = db.cursor()
    sql = "select * from arttable where idTable="+str(tableid)
    cursor.execute(sql)
    results = cursor.fetchall()
    for res in results:
        Caption = res[2]
    
    cursor = db.cursor()
    sql = "select * from cell where Table_idTable="+str(tableid)
    cursor.execute(sql)
    results = cursor.fetchall()
    for res in results:
        if(res[2]=="Empty"):
            CellEmpty=CellEmpty+1
        if(res[2]=="Text"):
            CellText=CellText+1
        if(res[2]=="Partially Numeric"):
            CellSemiNumeric=CellSemiNumeric+1
        if(res[2]=="Numeric"):
            CellNumeric=CellNumeric+1
        TotalCellNo = TotalCellNo+1
        if NoRows< res[4]:
            NoRows = res[4]
        if NoColumn< res[5]:
            NoColumn = res[5]
        
        if ("patient" in res[9]) or ("Patient" in res[9]):
            containsPatientsCell = 1
        if ("age" in res[9].lower()):
            containsAge = 1
        if ("n=" in res[9].lower()) or ("n =" in res[9].lower()):
            containsN = 1
        if(( "inclusion" in res[9].lower()) or ("exclusion" in res[9].lower())):
            containsInclusionExclusionCell = 1
        


    NoRows = NoRows+1
    NoColumn = NoColumn+1
    if  ("patient" in Caption) or ("Patient" in Caption):
        containsPatientsCap = 1
    if("characteristic" in Caption) or ("Characteristic" in Caption):
        containsCharacteristicCap = 1
    if("demograph" in Caption) or ("Demograph" in Caption):
        containsDemographic = 1
    if("baseline" in Caption) or ("Baseline" in Caption):
        containsBaseline = 1
    if("Trial" in Caption) or ("trial" in Caption):
        containsTrialCap = 1
    if("Inclusion" in Caption) or ("inclusion" in Caption):
        ContainsInclusion = 1
    if("Exclusion" in Caption) or ("exclusion" in Caption):
        ContainsExclusion = 1
    if("Adverse" in Caption) or ("adverse" in Caption):
        ContainsAdverse = 1
    if("side effect" in Caption.lower()):
        ContainsSideEffect = 1
    if("toxicity" in Caption.lower()):
        containsToxicity = 1
    if("haematologic" in Caption.lower()):
        containsHaematologic = 1
    if("eligibi" in Caption.lower()):
        containsEglibility = 1
    if("criteri" in Caption.lower()):
        containsCriteria = 1
    cursor = db.cursor()
    sql = "select * from annotation inner join cell on cell.idCell=annotation.Cell_idCell where  annotation.AgentName='MetaMap' and AnnotationDescription LIKE '%Symptom%' and Table_idTable="+str(tableid)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results)>0:
        ContainsSignOrSymptomAnnotation = 1
    CellEmpty = (float(CellEmpty)/float(TotalCellNo))*100
    CellText = (float(CellText)/float(TotalCellNo))*100
    CellNumeric = (float(CellNumeric)/float(TotalCellNo))*100
    CellSemiNumeric = (float(CellSemiNumeric)/float(TotalCellNo))*100
    outputline = str(tableid)+","+str(NoRows)+","+str(NoColumn)+","+ str(TotalCellNo)+","+str(CellEmpty)+","+str(CellNumeric)+","+str(CellSemiNumeric)+","+str(CellText)+","+str(ContainsAdverse)+","+str(containsAge)+","+str(containsBaseline)+","+str(containsCharacteristicCap)+","+str(containsDemographic)+","+str(ContainsExclusion)+","+str(ContainsInclusion)+","+str(containsN)+","+str(containsPatientsCap)+","+str(containsPatientsCell)+","+str(ContainsSideEffect)+","+str(ContainsSignOrSymptomAnnotation)+","+str(containsEglibility)+","+str(containsToxicity)+","+str(containsInclusionExclusionCell)+","+str(containsHaematologic) +","+str(containsTrialCap) +","+str(containsCriteria)+","+clas+"\n"
    return outputline    
if __name__=="__main__":
    dmeographicTables = [10,20,26,30,34,39,43,47,51,55,60,64,66,72,1656,3508,3572,12673,160,198,276,297,341,355,365,466,521,567,649,679,713,876,882,884,947,984,1067,1078,1122,1125,1146,1168,1180,1200,1206,1271,1273,1293,
1401,1481,1499,1527,1577,1584,1631,1675,1693,1715,1767,1837,1879,102,111,116,148, 150, 190,268,271,275,280,312,339,348,363,370,371,380,391,408,409,414,434,444,470,484,584,760,1588,1592,1597,1608,1612,1628,1636,1639,
1646,1656,1659,1666,1671,1688,1703,1707,1712,1724,1727,1734,1744, 9639,9658,9675,9697,9705,9718,9762,9788,9820,9844,9888,9890,9893,9895,9948,9954,
9997,10003,10050,10052,10055,10068,10072,10075,10132,10136,10169,10195,10212,10234,10255,10296,10297,
10299,10307,10311,10742,10746,10846,10863,10922,10927,10939,10945,10946,10947,10996,11026,89, 95,97,122,130,145,158,161,181,183,241,250,291,296,298,361,376,405,532,550,560,593,596,598,606,2932,2950,3727,4752]

    nonInterestingTables = [1,2,3,4,5,6,8,9,11,12,13,14,16,17,18,19,21,22,23,24,25,28,29,31,32,35,37,38,40,41,42,44,45,46,48,49,50,52,53,54,
                        56,57,58,59,61,62,63,65,67,68,69,70,71,73,74,75,76,77,78,539,764,6348,7866,7867,99,100,101,106,134,230,265,1027,1096,1106,1141,
                        1172,1224,197,388,389,595,655,656,1139,1140,1479,1702,2365,8624,8625,8626,8633,8986,8987,8988,9053,9054,9055,9434,9887,
                            79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,96,98,103,104,107,108,109,110,112,113,114,117,118,120,121,123,124,125,126,127,128,129,
131,132,133,134,135,136,137,138,1090,1096,290,292,294,295,299,3318]
    


    inclusionExclusionTables = [15,33,105,497,622,674,848,874,875,1095,1121,1291,1332,1381,3061,3882,3883,4027,4408,4876,4915,4944,5541,5725,
                            6177,6313,6332,6562,6923,7355,7386,7572,7781,7932,8073,8191,8324,8372,8408,8478,8989,9210,9252,9393,9701,
                            9708,10199,10962,11246,11269,11298,11809,11983,11984,12138,12159,12214,12337,12343,12604,12674,260,866,1717,3291,
                            3850,4419,5201,5409,6122,866,7238,7238,7546,7572,8080,8176,8327,10519,10603,10901,11343]

    adverseEventsTables = [7,36,115,394,428,440,464,765,766,771,799,944,1062,1091,1098,1102,1111,1112,1127,1170,1181,1209,1217,1243,1274,1277,
                           1279,1280,1285,1296,1297,1309,1390,1465,1466,1486,1515,1517,1544,1551,1585,1618,1624,1635,1664,1676,1764,1792,1800,1838,1871,1875,1916,1930,1947,1951,1958,
1959,1962,1963,1978,2013,2027,2045,2066,2161,2171,2249,2279,2286,2295,2316,2338,2374,2406,2532,2662,2699,2750,2778,2782,2885,2888,2923,
3155,3156,3162,3176,3251,3333,3338,3369,3371,3378,3379,3391,3399,3400,3419,3420,3478,3479,3484,3514,3543,3558,3592,3661,3736,3762,3766,
3811,3829,3848,3849,3888,3931,3979,4004,4055,4068,4093,4111,4136,4163,4202,4205,4206,4209,4223,4227,4312,4350,4351,4359,
4379,4380,4385,4406,4442,4485,4496,4532,4552,4559,4588,4589,4594,4595,4596,4610,4615,4617,4625,4629,4650,4664,4672,4673,4674,4675,4682,
4726,4781,4798,4850,4859,4882,4883,4923,4947,4963,4973,4975,4987,4988,4999,5000,5063,5092,5226,5240,5243,5284,5305,5322,8049,
8071,8107,8117,8139,8148, 293, 653, 1048,1658,1862,2466,2467,4127,4868,4901,4951,5292,5602,6186,6857,7052,7103,7104,7105,7506,7507,7508,7509,
7961,8163,8446,9505,11072,12375,12465,12466,12519,12559,61,68,140,257,314,439,486,492,627,742,3297,3296,3317,653]
    
    target = open("learnng2.csv", 'w')                                                                                          
    target.write("tableid,NoRows,NoColumn,TotalCellNo,CellEmpty,CellNumeric,CellSemiNumeric,CellText,ContainsAdverse,containsAge,containsBaseline,containsCharacteristicCap,containsDemographic,ContainsExclusion,ContainsInclusion,containsN,containsPatientsCap,containsPatientsCell,ContainsSideEffect,ContainsSignOrSymptomAnnotation,containsEglibility,containsToxicity,containsInclusionExclusionCell,containsHaematologic,containsCriteria,containsTrialCap,clas\n")
    for table in adverseEventsTables:
        target.write(processTable(table,"AdverseEvent"))
    for table in inclusionExclusionTables:
        target.write(processTable(table,"InclusionExclusion"))
    for table in nonInterestingTables:
        target.write(processTable(table,"Other"))
    for table in dmeographicTables:
        target.write(processTable(table,"BaselineCharacteristic"))
    target.close()
    
   #add like haematological 
    