import MySQLdb
import csv
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="table_db")        # name of the data base

cur = db.cursor()

cur.execute("SELECT * FROM ieattribute")
writer = csv.writer(open("ieattribute.csv", 'w'),delimiter=',',lineterminator='\n')
list = []
list.append("id")
list.append("document_id")
list.append("PMC")
list.append("idTable")
list.append("TableName")
list.append("Class")
list.append("SubClass")
list.append("Option")
list.append("Dimension1")
list.append("Dimension2")
list.append("StringValue")
list.append("IntValue")
list.append("Unit")
list.append("CueRule")
list.append("SynRule")
writer.writerow(list)
# print all the first cell of all the rows
for row in cur.fetchall():
    list = []
    list.append(row[0])
    list.append(row[1])
    list.append(row[2])
    list.append(row[3])
    list.append(row[4].replace("\n",""))
    list.append(row[5].replace("\n",""))
    list.append(row[6].replace("\n",""))
    list.append(row[7].replace("\n",""))
    list.append(row[8])
    list.append(row[9].replace("\n",""))
    list.append(row[10].replace("\n",""))
    list.append(row[11])
    list.append(row[12].replace("\n",""))
    list.append(row[13].replace("\n",""))
    list.append(row[14].replace("\n",""))
    writer.writerow(list)

db.close()