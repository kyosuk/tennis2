#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-

import MySQLdb
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor= connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`player1`) FROM `score`")
player1=cursor.fetchone()['COUNT(`player1`)']
Player1=int(player1)

cursor.execute("SELECT COUNT(`player2`) FROM `score`")
player2=cursor.fetchone()['COUNT(`player2`)']
Player2=int(player2)

cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
setplayer1=cursor.fetchone()['COUNT(`player1`)']
setPlayer1=int(setplayer1)

cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
setplayer2=cursor.fetchone()['COUNT(`player2`)']
setPlayer2=int(setplayer2)

cursor.execute("SELECT COUNT(`tieplayer1`) FROM `score`")
tiebplayer1=cursor.fetchone()['COUNT(`tieplayer1`)']
tiePlayer1=int(tiebplayer1)

cursor.execute("SELECT COUNT(`tieplayer2`) FROM `score`")
tiebplayer2=cursor.fetchone()['COUNT(`tieplayer2`)']
tiePlayer2=int(tiebplayer2)

cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']
if setPlayer1==6 and setPlayer2==6:
    point1=tiePlayer1
    point2=tiePlayer2
else:
    if Player1>3 or Player2>3:
        if abs(Player1-Player2)>1:
            point1="-"
            point2="-"   
        else:
            if Player1==Player2:
                point1="DEUCE"
                point2="DEUCE" 
            elif Player1>Player2:
                point1="Adv"
                point2="-"
            elif Player1<Player2:
                point1="-"
                point2="Adv"

    else:
        if Player1==0:
            point1=0
        elif Player1==1:
            point1=15
        elif Player1==2:
            point1=30
        elif Player1==3:
            point1=40

        if Player2==0:
            point2=0
        elif Player2==1:
            point2=15
        elif Player2==2:
            point2=30
        elif Player2==3:
            point2=40      
    
        
def hyoji():
        String = ("""
        <table border=1><tr><th>プレイヤー</th><th>ゲーム</th><th>スコア</th></tr>
        <tr><td>1</td><td>""")
        print (String)
        print (setPlayer1)
        print ("""</td><td>""")
        print (point1)
        print ("""</td></tr><tr><td>2</td><td>""")
        print (setPlayer2)
        print ("""</td><td>""")
        print (point2)
        print ("""</td></tr></body></html>""")
        
        
    
        
