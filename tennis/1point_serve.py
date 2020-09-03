#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import MySQLdb
import cgi
import pointhyoji
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)

cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']
def winserve():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>サーブは？（1=first,2=second,3=double)</h1>
    <form action='1point_winnetplay.py' method='GET'>
    <input type='submit' name='first' value='first' class='button'><br></br>
    <input type='submit' name='second' value='second' class='button'>
    </form>
    <form action='chosei.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji() 
def loseserve():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>サーブは？（1=first,2=second,3=double)</h1>
    <form action='1point_losenetplay.py' method='GET'>
    <input type='submit' name='first' value='first' class='button'><br></br>
    <input type='submit' name='second' value='second' class='button'><br></br>
    <input type='submit' name='doublefault' value='doublefault' class='button'>
    </form>
    <form action='chosei.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string) 
    pointhyoji.hyoji()
        

form = cgi.FieldStorage()
if form.getfirst('player1'):
    Win=1
elif form.getfirst('player2'):
    Win=2    

if Win==1:
    if Tiecheck==0:
        cursor.execute("""INSERT INTO win(player1) VALUES(1)""")
        cursor.execute("""INSERT INTO score(player1) VALUES(1)""")       
    
    else:
        cursor.execute("""INSERT INTO score(tieplayer1) VALUES(1)""")
    
    connection.commit() 
    winserve()
elif Win==2:
    if Tiecheck==0:
        cursor.execute("""INSERT INTO win(player2) VALUES(2)""")
        cursor.execute("""INSERT INTO score(player2) VALUES(2)""")
    
    else:
        cursor.execute("""INSERT INTO score(tieplayer2) VALUES(2)""")
    connection.commit()
    loseserve()    
else:
    print("前に戻ってください")    
