#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-

string = ("""
<!DOCTYPE html>
<html lang='ja'>
<head>
<meta charset='utf-8/'>
<link href="css/style.css" rel="stylesheet" type="text/css">
<title>sample1</title>
</head>
<body>
<h1>最初のサーブ</h1>
<form action='choice2.py' method='POST'>
<input type='submit' name='player1' value='player1' class='button'>
</form>
<br></br>
<form action='choice2.py' method='POST'>
<input type='submit' name='player2' value='player2' class='button'>

</form></body></html>""")
print(string)    