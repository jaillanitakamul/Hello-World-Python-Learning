import os 
os.system('cls')

#if 
'''
if conidtion:
    statement1
    statement2
statement3

xVal = 10 

if xVal > 0:
    print("Positve Number")
    print("The value is :",  xVal)
elif xVal == 0:
    print("Zero Value")
else:
    print("Negative Number")
print("Program Ends here..")

strName = "Asadullah"

if strName=="Naseeb":
    print("Sherzad 1st son")
elif strName=="Ahadullah":
    print("Sherzad 2nd son")
else:
    print("Shahrukh khan")

lessonList =["python","java","c#",".net","ruby","php"]

strLessonName = input("Enter you lesson name:")
if strLessonName in lessonList:
    print("welcome")
else:
    print("please check with department office")


domainList =(".com",".org",".afg")
strValue = "jaillanitakamul@gmail.com"

if strValue.endswith((domainList)):
    print("valid domain name")
else:
    print("invalid email address")


numValue = {1,2,3,4,5}
if 2 in numValue:
    print("2 is in set")
if 3 in numValue:
    print("3 is in set")
if 4 in numValue:
    print("4 is in set")
if 5 in numValue:
    print("5 is in set")
else :
    print("Not in set")

colorValue = ("pink","green","yellow","white","black")

if colorValue[0]=="red":
    print("Red value is in the tuple")
elif len(colorValue) == 4:
    print("we have 4 items in the tuple")
else:
    print("None of condition matches")


numValue = 7.0

if numValue == int(numValue):
    print("Whole number")
else:
    print("decimal point number")
'''

numValue = 7

if isinstance(numValue, int):
    print("whole no")
else:
    print("decimal no")



# print("Invalid email address")
'''strValue = "jaillanitakamul@gmail.com"

if "." in strValue:
    print(". is here and a valid email")
elif "@" in strValue:
    print("@ is here and a valid email")
elif strValue.count("@")!=1:
    print("valid email because of too many @")
else:
    print("Invalid email address")'''

#if - else 
#if - elif - else 
#if - if - if
#Nested - if (if - elif -else) 

#inline if condition

#match case