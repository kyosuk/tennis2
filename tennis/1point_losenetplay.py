#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import MySQLdb
import cgi
import pointhyoji
import pointdef
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']
def losenetplay():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>ネットプレイした？（1=yes,2=no)</h1>
    <form action='1point_losehow.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'>
    </form>
    <form action='chosei.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji()
    
form = cgi.FieldStorage()
if form.getfirst('first'):
    Loseserve=1
elif form.getfirst('second'):
    Loseserve=2
elif form.getfirst('doublefault'):    
    Loseserve=3

if Loseserve==1:
    cursor.execute("""INSERT INTO serve(1st) VALUES (1)""")
    connection.commit()
    losenetplay()
elif Loseserve==2:
    cursor.execute("""INSERT INTO serve(2nd) VALUES (2)""")
    connection.commit()
    losenetplay()  
elif Loseserve==3:
    cursor.execute("""INSERT INTO serve(doublefault) VALUES (3)""") 
    connection.commit()
    if  Tiecheck==1:
        pointdef.servetiebreak()
    elif Tiecheck==2:
        pointdef.returntiebreak()   
    else:
        pointdef.servepointcheck()
