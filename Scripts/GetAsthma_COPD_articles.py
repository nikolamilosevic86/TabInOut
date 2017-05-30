import os
import MySQLdb
host = "localhost"
username = "root"
password="bd5102"
database = "shared"
db = MySQLdb.connect(host,username,password,database,charset='utf8')
directory = "COPD"
if not os.path.exists(directory):
    os.makedirs(directory)
cursor = db.cursor()
sql = "select PMCid,XML from pmc_articles_2017 where PMCid in (27372,3023060,1747438,3263438,2104567,2921687,3266210,2838456,2848004,2677771,3580134,2629970,1746668,1913915,1747331,3233513,1746483,2939686,2964613,3485572,2693850,3528484,3276256,3276257,3098801,3098801)"
cursor.execute(sql)
results = cursor.fetchall()
for res in results:
    filename = res[0]
    content = res[1]
    f = open("COPD/PMC"+str(filename)+".xml", 'w')
    f.write(content)
    f.close()

directory = "Asthma"
if not os.path.exists(directory):
    os.makedirs(directory)
cursor = db.cursor()
sql = "select PMCid,XML from pmc_articles_2017  where PMCid in (3992367,3561510,4515999);"
cursor.execute(sql)
results = cursor.fetchall()
for res in results:
    filename = res[0]
    content = res[1]
    f = open("Asthma/PMC"+str(filename)+".xml", 'w')
    f.write(content)
    f.close()