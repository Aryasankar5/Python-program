# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:23:59 2020

@author: ARYA SHANKAR
"""

a = input("Input the file name: ").casefold()
s = a.split('.')

if(s[0]=="py"):
    print("The extension of file is :"+" Python")
elif(s[0]=="java"):
      print("The extension of file is :"+"Java")
elif(s[0]=="js"):
      print("The extension of the file is :"+"Javascript")
elif(s[0]=="mat"):
      print("The extension of the file is :"+"Matlab")
elif(s[0]=="txt"):
      print("The extension of the file is :"+"Text")
else:
      print("The extension of the file is :"+"Other file")            

