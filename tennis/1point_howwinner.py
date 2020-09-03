#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-s
import MySQLdb
import cgi
import pointdef
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']

form = cgi.FieldStorage()
if form.getfirst('serve'):
    Howwinner=1
elif form.getfirst('rally'):
    Howwinner=2
if Howwinner==1:
    cursor.execute("""INSERT INTO howwinner(serve) VALUES (1)""")
    connection.commit()
    if  Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()   
    else:
        pointdef.servepointcheck()
elif Howwinner==2:
    cursor.execute("""INSERT INTO howwinner(ornot) VALUES (2)""")
    connection.commit()
    if  Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()   
    else:
        pointdef.servepointcheck()
