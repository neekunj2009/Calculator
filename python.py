from gettext import install
from threading import Timer
from tkinter import Y, Place
from tokenize import Name
import webbrowser


X=  5 * 2
Y= "Hello World"
print ("Five Is greater Than two!")
print(X)
print(Y)
print("Cheers,Matel!")
x = str(4)
y = int(3)
z =float(3)
print(x)
print(z)
print(y)
#This is for Asking About the User
import time
s=time.time()
Name,Age,Placeliving = input("What is your Name"),input("What is your age"),input("Where Do you Live")
 
 
print("Hello",Name,"so your age is",Age,"And You Live in",Placeliving)

e=time.time()
print(e-s)
import urllib.request
webUrl = urllib.request.urlopen('https://neekunj2009.github.io/chatbot/')
print("result code: " + str(webUrl.getcode()))
data = webUrl.read()
print (data)