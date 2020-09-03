#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import MySQLdb
import pointhyoji
import cgi
form = cgi.FieldStorage()
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor = connection.cursor()
def force():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>フォースドエラーですか？</h1>
    <form action='1pointre_force.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'>
    </form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji()
def howwinner():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>どんなウィナーですか？（1=サーブ,2=ストローク)</h1>
    <form action='1pointre_howwinner.py' method='POST'>
    <input type='submit' name='serve' value='1' class='button'><br></br>
    <input type='submit' name='rally' value='2' class='button'>
    </form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji()   
if form.getfirst('yes'):
    How=1
elif form.getfirst('no'):
    How=2
if How==1:
    cursor.execute("""INSERT INTO how(error) VALUES (1)""")
    connection.commit()
    force()
elif How==2:
    cursor.execute("""INSERT INTO how(noterror) VALUES (2)""")
    connection.commit()
    howwinner()
else:
    print("前に戻ってください")
