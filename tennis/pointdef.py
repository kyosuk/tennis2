#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")    
    
def game1(a):
    import MySQLdb
    import result1
    import pointre_win
    from password import password
    cursor = a.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(`player1`) FROM `score`")
    player1=cursor.fetchone()['COUNT(`player1`)']
    Player1=int(player1)
    cursor.execute("SELECT COUNT(`player2`) FROM `score`")
    player2=cursor.fetchone()['COUNT(`player2`)']
    Player2=int(player2)
    cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
    player1game=cursor.fetchone()['COUNT(`player1`)']
    Player1game=int(player1game)
    cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
    player2game=cursor.fetchone()['COUNT(`player2`)']
    Player2game=int(player2game)
    if Player1game>5 or Player2game>5:
        if abs(Player1game-Player2game)>2:
            result1.result1()
        elif Player1game==6 and Player2game==6:
            cursor.execute("INSERT INTO score(tiecheck) VALUES (1)")
            cursor.execute("INSERT INTO score(tiecheck) VALUES (1)")
            a.commit()
            returntiebreak()
        elif Player1game==7 or Player2game==7:
            result1.result1()
        else:
            pointre_win.pointre_win()           
    else:
        pointre_win.pointre_win()
def game2(a):
    import MySQLdb
    import result1
    import point_win
    cursor = a.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(`player1`) FROM `score`")
    player1=cursor.fetchone()['COUNT(`player1`)']
    Player1=int(player1)
    cursor.execute("SELECT COUNT(`player2`) FROM `score`")
    player2=cursor.fetchone()['COUNT(`player2`)']
    Player2=int(player2)
    cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
    player1game=cursor.fetchone()['COUNT(`player1`)']
    Player1game=int(player1game)
    cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
    player2game=cursor.fetchone()['COUNT(`player2`)']
    Player2game=int(player2game)
    if Player1game>5 or Player2game>5:
        if abs(Player1game-Player2game)>2:
            result1.result1()
        elif Player1game==6 and Player2game==6:
            cursor.execute("INSERT INTO score(tiecheck) VALUES (1)")
            cursor.execute("INSERT INTO score(tiecheck) VALUES (1)")
            a.commit()
            returntiebreak()
        elif Player1game==7 or Player2game==7:
            result1.result1()
        else:
            point_win.point_win()           
    else:
        point_win.point_win()            
def returntiebreak():
    import pointre_win
    import point_win
    import result1
    import MySQLdb
    from password import password
    connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(`tieplayer1`) FROM `score`")
    Tieplayer1=cursor.fetchone()['COUNT(`tieplayer1`)']
    cursor.execute("SELECT COUNT(`tieplayer2`) FROM `score`")
    Tieplayer2=cursor.fetchone()['COUNT(`tieplayer2`)']
    point=Tieplayer1+Tieplayer2
    def tiebreak():
        if point % 4 == 0 or point % 4 == 3:
            pointre_win.pointre_win()
        else:
            point_win.point_win()   

    if Tieplayer1>6 or Tieplayer2>6:
        if abs(Tieplayer1-Tieplayer2)>1:
            result1.result1()
        else:
            tiebreak()
    else:
        tiebreak()
     
def servetiebreak():
    import pointre_win
    import point_win
    import result1
    import MySQLdb
    from password import password
    connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
    cursor= connection.cursor(MySQLdb.cursors.DictCursor)    
    cursor.execute("SELECT COUNT(`tieplayer1`) FROM `score`")
    Tieplayer1=cursor.fetchone()['COUNT(`tieplayer1`)']

    cursor.execute("SELECT COUNT(`tieplayer2`) FROM `score`")
    Tieplayer2=cursor.fetchone()['COUNT(`tieplayer2`)']

    point=Tieplayer1+Tieplayer2
    def tiebreak():
        if point % 4 == 0 or point % 4 == 3:
            point_win.point_win()
        else:
            pointre_win.pointre_win()   

    if Tieplayer1>6 or Tieplayer2>6:
        if abs(Tieplayer1-Tieplayer2)>1:
            result1.result1()
        else:
            tiebreak()
    else:
        tiebreak()        
def servepointcheck():
    import point_win
    import pointre_win
    import result1
    import MySQLdb
    from password import password
    connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(`player1`) FROM `score`")
    player1=cursor.fetchone()['COUNT(`player1`)']
    Player1=int(player1)
    cursor.execute("SELECT COUNT(`player2`) FROM `score`")
    player2=cursor.fetchone()['COUNT(`player2`)']
    Player2=int(player2)
    cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
    player1game=cursor.fetchone()['COUNT(`player1`)']
    Player1game=int(player1game)
    cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
    player2game=cursor.fetchone()['COUNT(`player2`)']
    Player2game=int(player2game)
    if Player1>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player1) VALUES (1)")
            connection.commit()
            cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
            player1game=cursor.fetchone()['COUNT(`player1`)']
            Player1game=int(player1game)
            cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
            player2game=cursor.fetchone()['COUNT(`player2`)']
            Player2game=int(player2game)
            game1(connection)
        else:
            point_win.point_win()
    elif Player2>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player2) VALUES (2)")
            connection.commit()
            cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
            player1game=cursor.fetchone()['COUNT(`player1`)']
            Player1game=int(player1game)
            cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
            player2game=cursor.fetchone()['COUNT(`player2`)']
            Player2game=int(player2game)
            game1(connection)
        else:
            point_win.point_win()
    else:
        point_win.point_win() 
        
def returnpointcheck():
    import point_win
    import pointre_win
    import result1
    import MySQLdb
    from password import password
    connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(`player1`) FROM `score`")
    player1=cursor.fetchone()['COUNT(`player1`)']
    Player1=int(player1)
    cursor.execute("SELECT COUNT(`player2`) FROM `score`")
    player2=cursor.fetchone()['COUNT(`player2`)']
    Player2=int(player2)
    cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
    player1game=cursor.fetchone()['COUNT(`player1`)']
    Player1game=int(player1game)
    cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
    player2game=cursor.fetchone()['COUNT(`player2`)']
    Player2game=int(player2game)
    
    if Player1>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player1) VALUES (1)")
            connection.commit()
            cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
            player1game=cursor.fetchone()['COUNT(`player1`)']
            Player1game=int(player1game)
            cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
            player2game=cursor.fetchone()['COUNT(`player2`)']
            Player2game=int(player2game)
            game2(connection)
        else:
            pointre_win.pointre_win()
    elif Player2>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player2) VALUES (2)")
            connection.commit()
            cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
            player1game=cursor.fetchone()['COUNT(`player1`)']
            Player1game=int(player1game)
            cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
            player2game=cursor.fetchone()['COUNT(`player2`)']
            Player2game=int(player2game)
            game2(connection)
        else:
            pointre_win.pointre_win()
    else:
        pointre_win.pointre_win()   