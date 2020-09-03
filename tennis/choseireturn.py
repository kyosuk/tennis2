#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
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
<form action="1returndelete.py" method="post">
<p>消去したいデータ<br>
		<input type="checkbox" name="score of 1" value="score of 1">score of 1<br></br>
		<input type="checkbox" name="score of 2" value="score of 2">score of 2<br></br>
		<input type="checkbox" name="netwin" value="netwin">netwin<br></br>
		<input type="checkbox" name="netlose" value="netlose">netlose<br></br>
		<input type="checkbox" name="1stserve" value="1stserve">1stserve<br></br>
    <input type="checkbox" name="2ndserve" value="2ndserve">2ndserve<br></br>
		<input type="checkbox" name="doublefault" value="doublefault">doublefault<br></br>
		<input type="checkbox" name="1stservewin" value="1stservewin">1stservewin<br></br>
		<input type="checkbox" name="2ndservewin" value="2ndservewin">2ndservewin<br></br>
		<input type="checkbox" name="serviceace" value="serviceace">serviceace<br></br>
    <input type="checkbox" name="winner" value="winner">winner<br></br>
		<input type="checkbox" name="unforcederror" value="unforcederror">unforcederror<br></br>
		<input type="checkbox" name="forcederror" value="forcederror">forcederror
	</p>
	<p><input type="submit" value="消去する"></p>    
    """)
print (string)
