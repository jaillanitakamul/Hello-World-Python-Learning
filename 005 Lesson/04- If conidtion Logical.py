import os 
os.system('cls')
'''
stuMark = int(input("Please enter your marks"))
#stuAssignment
# 
# 100-90 (A) - 89-80 (B) - 79-70 (C) - 69-60 (D) - 59-50 (E) - F 
#  

if stuMark >=90 and stuMark<=100:
#if 90>=stuMark<=100:
    print("A Grade")
elif stuMark>=80 :
    print("B Grade")
elif stuMark>=70:
    print("C Grade")
else:
    print("Fail")'''

userRole = "admin"
userName = "jaillani1"
userPassword="pythonlesson"

#Nested If Condition
'''
if userName=="jaillani":
    if userPassword=="pythonlesson":
        print("Welcome to class")
    else: 
        print("Wrong Password")
else:
    print("Invalid User Name")

if userName=="jaillani" and userPassword=="pythonlesson":
    print("Welcome to class")
if userRole=="admin" or userName=="jaillani":
    print("Welcome to Admin Panel")
else:
    print("sorry no access..")


panelView = False
panelManage=False
#button click - View False - Manage - True

panelManage = not(panelView)
print(panelView)
print(panelManage)'''

strGender = "m"

#if strGender=="M":print("Male") 
#else:print("Female")

#inline if condition

#genderText = "Male" if strGender=="M" or strGender =="m" else "Female" if strGender=="F" or strGender=="f" else "No Gender"

genderText = "Male" if strGender.lower()=="m" else "Female" if strGender.lower()=="f" else "No Gender"


print(genderText)














