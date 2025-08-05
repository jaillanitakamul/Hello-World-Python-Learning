import os 
os.system("cls")

#Delete : on a specific position (delete) - del statement
#remove:first occurance
#pop(): specific or the last element

varList =[10,20,30,40,30,40,50,30]
print(varList)

'''setList = {10,20,30,40,30,40,50,30}
print(setList)
varList.remove(30)
print(varList)'''

varList.pop(4)
print(varList)

del varList[0]
print(varList)