import os 
os.system('cls')

'''t1= (1,2,3,4)
t2=(5,6)

print(t1+t2)

t3=("-")
print(t3*10)

tcollection = (1,2,3,2,3,4,2,6)
print(tcollection.count(3))
print(tcollection.index(2))

tupValue = ("Sun","Mon","Tue","Wed","Thur","Fri","Sat")
a,*b,c = tupValue

print(a)
print(b)
print(c)

tval = (1,2,3,4,5,6,7)

print(len(tval))
print(max(tval))
print(min(tval))
print(sum(tval))

tvalUnSort = (8,1,3,4,6,5,2,7)
#print(sorted(tvalUnSort))
tvalSorted = sorted(tvalUnSort)
print(tuple(reversed(tvalSorted)))


tvalMonths=('Apr','Jan','Feb','May','Mar')
print(sorted(tvalMonths))'''

#Packing 
personInfo = ("Sherzad", 45, "USA")
#pName, pAge, pLocation = personInfo

#print("The person info is as below \nName is :" , pName, "\nAge is :", pAge,"\nLocation :" , pLocation)

'''sName, *sBio = personInfo
print(sName, sBio)

tNested = (1,(2,3),(4,(5,6)))
print(tNested)
print(tNested[0])

print(tNested[1])
print(tNested[1][0])
print(tNested[1][1])

print(tNested[2])
print(tNested[2][0])

print(tNested[2][1])
print(tNested[2][1][0])
print(tNested[2][1][1])'''

tData = (1,2,3)
lData = list(tData)

lData.append(4)

tData2 = tuple(lData)
print(tData2)


