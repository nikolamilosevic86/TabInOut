'''
Created on 26 Oct 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import csv
first_row = True
last_Sid =''
last_TabOrder = ''
current_Sid = ''
Current_TabOrder = ''
out = open('DDIExtractionSample.csv','w')
with open('DDIExtractionDataSample2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        current_Sid = row[0]
        Current_TabOrder = row[1]
        if(first_row):
            out.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+'\n')
            first_row = False
        else:
            if(last_Sid!='' and (last_Sid!=current_Sid or last_TabOrder!=Current_TabOrder)):
                out.write('\n')
            else:
                out.write(row[0]+',"'+row[1]+'","'+row[2]+'","'+row[3]+'","'+row[4]+'"\n')
        last_Sid = current_Sid
        last_TabOrder = Current_TabOrder
        print(row)