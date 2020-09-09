#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import cgi
import pointdef
form = cgi.FieldStorage()
if form.getfirst('player1'):
    pointdef.servepointcheck()
elif form.getfirst('player2'):
    pointdef.returnpointcheck()
