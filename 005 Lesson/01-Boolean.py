import os
os.system('cls')

#Boolean - Values 
'''print(True)
print(False)
print(type(True))

strName = input("Please enter your name:")
print(bool(strName))'''
'''
#Boolean Function
print(bool(123))
print(bool())
print(bool(""))
print(bool(None))
print(bool(" "))
print(bool(0))
print(bool(1))

#any 
emailAddress ="enyat@gmail.com"
UserName="Enayat"
PhoneContact =""
print(any([emailAddress, PhoneContact, UserName]))

#all 
print(all([emailAddress, PhoneContact, UserName]))

#isinstance
print(isinstance( 1234, int))
print(isinstance("Samim", int))

strName="jaillani"
#print(strName.endswith("i"))
#print(strName.startswith("J"))
print(strName[0].isupper())
print(strName[-1].islower())

#Comparision
#Greater >, Greater and Equal, Not Equal, Equal, less, less and equal
#>,>=,<,<=,!=,== 
print(3>1<0)
userAge = int(input("Please enter your age"))
print(18<=userAge<=32)


#Logical Operator
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Not operator 
print(not(3>1))
print(not(1<0))

#Membership Operator
strText = "Samim"
print("s" in strText or "S" in strText)

print("s" in strText.lower())'''

strFavSubject = input("Enter your favrote subject:")

listSubjects = ["python","java","c#",".net"]
print(strFavSubject.lower() in listSubjects)


