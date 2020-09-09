#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
import MySQLdb
import cgi
import pointdef
from password import password
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']
print(Tiecheck)
form = cgi.FieldStorage()
if form.getfirst('serve'):
    Howwinner=1
elif form.getfirst('rally'):
    Howwinner=2
if Howwinner==1:
    if Tiecheck==0:
        pointdef.returnpointcheck()
    elif Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()
elif Howwinner==2:
    cursor.execute("""INSERT INTO howwinner(ornot) VALUES (2)""")
    connection.commit()
    if Tiecheck==0:
        pointdef.returnpointcheck()
    elif Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()
else:
    print("前に戻ってください")
