import os 
os.system('cls')

monthName=["Jan","Feb","Mar"]

'''
upperList=[]
lowerList=[]

#-Insert, Append, Update
for m in monthName:
    upperList.append(m.upper())
    lowerList.insert(len(lowerList), m.lower())

print(upperList)
print(lowerList)'''

#Map list apply 

upperList=list(map(str.upper, monthName))
lowerList=list(map( str.lower, monthName))

print(upperList)
print(lowerList)