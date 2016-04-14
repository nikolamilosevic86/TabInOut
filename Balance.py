'''
Created on Dec 18, 2015

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import random
with open('learnngCellDatasetWClassPatientNum.csv') as f:
    content = f.readlines()
    f2 = open('learnngCellDatasetBalanced.csv', 'w+')
    f2.write("ArticleId,PMCid,TableName,SpecPragmatics,CellContent,Header,Stub,SuperRow,rowN,columnN,function,hasValue\n")
    i = 0
    countbad = 0
    countgood = 0
    NoArray = []
    while i<len(content):
        row = content[i]
        last = row.split(",")[11]
        print last
        if('yes' in last and countgood<182):
            f2.write(row)
            countgood = countgood + 1
        else:
            NoArray.append(row)
        i = i+1
    i=0
    random.seed(419)
    while i < 200:

        randNum = random.randrange(0,len(NoArray))
        f2.write(NoArray[randNum])
        i=i+1
    f2.close()
         
print "done"