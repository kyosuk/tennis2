def point_win():   
    #!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
    #-*- coding: utf -8  -*-
    import MySQLdb
    import pointhyoji
    from password.password import *

    connection = MySQLdb.connect(
                 host="localhost", user="root", password=PASSWORD, db="tennis2"
                 )
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>サーブ　勝者は？（1=player1,2=player2)</h1>
    <form action='1point_serve.py' method='GET'>
    <input type='submit' name='player1' value='1' class='button'><br></br>
    <input type='submit' name='player2' value='2' class='button'><br></br>
    </form>
    <form action='chosei.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>
    """)
    print(string)    

    pointhyoji.hyoji()
