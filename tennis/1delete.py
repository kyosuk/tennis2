#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
import MySQLdb
import cgi
import pointdef
from password.password import *

connection = MySQLdb.connect(
    host="localhost", user="root", password=PASSWORD, db="tennis2"
)
cursor= connection.cursor(MySQLdb.cursors.DictCursor)
form = cgi.FieldStorage()
def delete():
    if form.getfirst('score of 1'):
        cursor.execute("DELETE FROM score WHERE player1 LIMIT 1")
        connection.commit()
    if form.getfirst('score of 2'):
        cursor.execute("DELETE FROM score WHERE player2 LIMIT 1")
        connection.commit()
    if form.getfirst('netwin'):
        cursor.execute("DELETE FROM net WHERE win LIMIT 1")
        connection.commit()
    if form.getfirst('netlose'):
        cursor.execute("DELETE FROM net WHERE lose LIMIT 1")
        connection.commit()
    if form.getfirst('1stserve'):
        cursor.execute("DELETE FROM serve WHERE 1st LIMIT 1")
        connection.commit()
    if form.getfirst('2ndserve'):
        cursor.execute("DELETE FROM serve WHERE 2nd LIMIT 1")
        connection.commit()
    if form.getfirst('doublefault'):
        cursor.execute("DELETE FROM serve WHERE doublefault LIMIT 1")
        connection.commit()                    
    if form.getfirst('1stservewin'):
        cursor.execute("DELETE FROM servewinpercent WHERE 1st LIMIT 1")
        connection.commit()
    if form.getfirst('2ndservewin'):
        cursor.execute("DELETE FROM servewinpercent WHERE 2nd LIMIT 1")
        connection.commit()
    if form.getfirst('serviceace'):
        cursor.execute("DELETE FROM howwinner WHERE serve LIMIT 1")
        connection.commit()
    if form.getfirst('winner'):
        cursor.execute("DELETE FROM howwinner WHERE ornot LIMIT 1")
        connection.commit()
    if form.getfirst('unforcederror'):
        cursor.execute("DELETE FROM forcedornot WHERE unforced LIMIT 1")
        connection.commit()
    if form.getfirst('forcederror'):
        cursor.execute("DELETE FROM forcedornot WHERE forced LIMIT 1")
        connection.commit()                
delete()
pointdef.servepointcheck()
