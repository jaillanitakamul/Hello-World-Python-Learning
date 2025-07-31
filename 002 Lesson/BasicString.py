#Basic String Operations
#a. Concatenation (Joining Strings)
#b. Repetition
#c. Accessing Characters (Indexing & Slicing)
#d. Reverse String [::-1]

import os 
os.system('cls')

varStr = "String Value"
varStr2 = "Hi Value"

print(varStr + varStr2)
print(varStr +" "+ varStr2)
print(varStr, varStr, sep="--")

repWord = "--"
print(repWord * 5)

strName = "Sherzad"
print(strName[0])
print(strName[-1])

print(strName[0:4])
print(strName[2:])
print(strName[:4])
print(strName[::-1])

name1="Sherzad"
name2="Zahid"

para ='''Multi line paragraph 
example to enter here 
this is  my question.
'''

print(para)




