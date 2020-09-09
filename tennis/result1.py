def result1():
    #!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
    #-*- coding: utf -8  -*-
    print("Content-Type: text/html\n")
    import MySQLdb
    import result1
    from password import password
    connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password=password.PASSWORD,
    db='tennis2'
    )
    cursor= connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("SELECT COUNT(`doublefault`) FROM `serve`")
    Doublefault=cursor.fetchone()['COUNT(`doublefault`)']

    cursor.execute("SELECT COUNT(`1st`) FROM `serve`")
    First=cursor.fetchone()['COUNT(`1st`)']

    cursor.execute("SELECT COUNT(`2nd`) FROM `serve`")
    Second=cursor.fetchone()['COUNT(`2nd`)']

    cursor.execute("SELECT COUNT(`1st`) FROM `servewinpercent`")
    Firstwin=cursor.fetchone()['COUNT(`1st`)']

    cursor.execute("SELECT COUNT(`2nd`) FROM `servewinpercent`")
    Secondwin=cursor.fetchone()['COUNT(`2nd`)']

    cursor.execute("SELECT COUNT(`serve`) FROM `howwinner`")
    Serveace=cursor.fetchone()['COUNT(`serve`)']

    cursor.execute("SELECT COUNT(`ornot`) FROM `howwinner`")
    Winner=cursor.fetchone()['COUNT(`ornot`)']

    cursor.execute("SELECT COUNT(`unforced`) FROM `forcedornot`")
    Unforcederror=cursor.fetchone()['COUNT(`unforced`)']

    cursor.execute("SELECT COUNT(`win`) FROM `net`")
    Netwin=cursor.fetchone()['COUNT(`win`)']

    cursor.execute("SELECT COUNT(`lose`) FROM `net`")
    Netlose=cursor.fetchone()['COUNT(`lose`)']

    serve=Doublefault+First+Second
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head><body>""")
    print (string)
    print("""<table border=1><tr><th>ACES</th><th>ダブルフォルト</th><th>1st serve in %</th><th>1st points won %</th><th>2st points won %</th><th>Winners</th><th>Unforced error</th><th>Netpoints won</th></tr><tr><td>""")
    print(Serveace)
    print("</td><td>")
    print(Doublefault)
    print("</td><td>")
    print(First/serve*100)
    print("</td><td>")
    print(Firstwin/First*100)
    print("</td><td>")
    print(Secondwin/Second*100)
    print("</td><td>")
    print(Winner)
    print("</td><td>")
    print(Unforcederror)
    print("</td><td>")
    print(Netwin)
    print("/")
    print(Netwin+Netlose)
    print("""</td></tr></table>""")
