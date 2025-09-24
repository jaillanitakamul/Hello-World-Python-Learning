"""
Module: contains functions, classess or variables you can reuse 
in the other programs

External 
Internal
import module name
"""
import os
import math 
import random as rd
from datetime import datetime

os.system('cls')
'''
print(math.sqrt(16))
print(math.pi)

#https://docs.python.org/3/py-modindex.html

#print(random.randint(1,100))
print(rd.randint(1,200))
print(rd.choice(["Asadullah","Sherzad","Samsor","Enayat","Jaillani"]))

print(os.getcwd())
print(os.listdir("."))

dtNow = datetime.now()
print("Current Time:", dtNow)
print("Current Year:", dtNow.year)
print("Current Month:", dtNow.month)
print("Current Day:", dtNow.day)

#Mean, Median and Stdev
dataNo=[10,20,30,40,50]
#Mean - Average 1,2,3,4 = (1+2+3+4)/4= 2.5
#Median - 1,2,3,4,5 = 3 
#standard deviation 1,2,3,4,5,6 =

import statistics as st
print("Mean:", st.mean(dataNo)) 
print("Median:", st.median(dataNo))
print("Standard Devision:", st.stdev(dataNo))'''

import myModule

strAction = "Delete ALL"
print(myModule.printMessage(strAction))


