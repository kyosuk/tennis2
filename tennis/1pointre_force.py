#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import cgi
import MySQLdb
import pointdef
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']

form = cgi.FieldStorage()
if form.getfirst('yes'):
    Force=1
elif form.getfirst('no'):
    Force=2
if Force==1:
    cursor.execute("""INSERT INTO forcedornot(forced) VALUES (1)""")
    connection.commit()
    if Tiecheck==0:
        pointdef.returnpointcheck()
    elif Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()
elif Force==2:
    cursor.execute("""INSERT INTO forcedornot(unforced) VALUES (2)""")
    connection.commit()
    if Tiecheck==0:
        pointdef.returnpointcheck()
    elif Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()    
