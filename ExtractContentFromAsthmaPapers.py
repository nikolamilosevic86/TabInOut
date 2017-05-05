from QueryDBClass import QueryDBCalss

queryclass = QueryDBCalss("localhost","root","","table_db", )
cursor = queryclass.db.cursor()
    #Get tables
sql = """SELECT Content FROM table_db.article inner join arttable on arttable.Article_idArticle=article.idArticle inner
join cell on arttable.idTable=cell.Table_idTable where Title like '%asthma%' or Title like '%Asthma%' or Abstract like
'%asthma%' or  Abstract like '%Asthma%';"""
cursor.execute(sql)
results = cursor.fetchall()
file = open("content_asthma.txt","w")
for res in results:
    file.write(res[0].encode('utf-8')+'\n')
file.close()

print "Done Asthma"


sql = """SELECT Content FROM table_db.article inner join arttable on arttable.Article_idArticle=article.idArticle inner
join cell on arttable.idTable=cell.Table_idTable where Title like '%COPD%' or Title like '%copd%' or Abstract like
'%COPD%' or  Abstract like '%copd%' or Title like '%chronic obstructive pulmonary disease%' or Title like '%Chronic obstructive pulmonary disease%' or
Abstract like '%Chronic obstructive pulmonary disease%' or Abstract like "%chronic obstructive pulmonary disease%";"""
cursor.execute(sql)
results = cursor.fetchall()
file = open("content_copd.txt","w")
for res in results:
    file.write(res[0].encode('utf-8')+'\n')
file.close()

print "Done COPD"