#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import MySQLdb
import cgi
import pointhyoji
form = cgi.FieldStorage()
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
def winnetplay():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>ネットプレイした？</h1>
    <form action='1pointre_winhow.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'>
    </form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji()

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
    <h1>ネットプレイした？</h1>
    <form action='1pointre_losehow.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'>
    </form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form></body></html>""")
    print(string)       
    pointhyoji.hyoji()

if form.getfirst('player1'):
    Win=1
elif form.getfirst('player2'):
    Win=2 
if Win==1:
    if Tiecheck==0:
        cursor.execute("""INSERT INTO win(player1) VALUES(1)""")
        cursor.execute("""INSERT INTO score(player1) VALUES(1)""")
        connection.commit()
        winnetplay()
    elif Tiecheck==1:
        cursor.execute("""INSERT INTO score(tieplayer1) VALUES(1)""")
        connection.commit()
        winnetplay()
    else:
        cursor.execute("""INSERT INTO score(tieplayer1) VALUES(1)""")
        connection.commit()
        winnetplay()
elif Win==2:
    if Tiecheck==0:
        cursor.execute("""INSERT INTO win(player2) VALUES(2)""")
        cursor.execute("""INSERT INTO score(player2) VALUES(2)""")
        connection.commit()
        losenetplay()
    elif Tiecheck==1:
        cursor.execute("""INSERT INTO score(tieplayer2) VALUES(2)""")
        connection.commit()
        losenetplay()
    else:
        cursor.execute("""INSERT INTO score(tieplayer2) VALUES(2)""")
        connection.commit()
        losenetplay()
