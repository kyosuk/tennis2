def pointre_win():
    #!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
    #-*- coding: utf -8  -*-
    import pointhyoji
    import MySQLdb
    from password.password import *

    connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
    )
    cursor = connection.cursor()
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>リターン　勝者　（1=player1,2=player2) </h1>
    <form action='1pointre_netplay.py' method='POST'>
    <input type='submit' name='player1' value='1' class='button'><br></br>
    <input type='submit' name='player2' value='2' class='button'>
    </form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form></body></html>""")
    print(string)  
    pointhyoji.hyoji()
