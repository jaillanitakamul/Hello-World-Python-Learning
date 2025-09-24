import os 
import myCalculator 
#from myGreeting import welcome
import myGreeting as mG

os.system('cls')

print(myCalculator.AddNo(1,2))
print(myCalculator.SubNo(1,2))
print(myCalculator.MultiNo(1,2))
print(myCalculator.DivideNo(1,2))

print(mG.welcome("Samor Samim"))
print(mG.goodBye("Ahadullah Zahid"))

#pip
#pip install pyjokes
#pip uninstall pyjokes
'''
import pyjokes as pj
print(pj.get_joke())'''
