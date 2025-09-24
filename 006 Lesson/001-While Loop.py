#while loop 
#While Condition 
import os 
os.system('cls')

'''iCounter = 1
while iCounter <=5:
    print("Count No:", iCounter)
    iCounter +=1

iCounter = 0
while iCounter <5:
    iCounter +=1
    print("Count No:", iCounter)


strText = "Ahadullah"
i = 0

while i< len(strText):
    print("Character is :", strText[i], "Index No:" ,i)
    i +=1

for ivalue , ichar in enumerate(strText):
    print("Index No:", ivalue,"Character:", ichar)

daysName=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for iDayNo,iDayValue in enumerate(daysName):
    print("Day:", iDayValue, "#:", iDayNo+1)


strText = "Ahadullah"
iNo=0
for ichar in strText:
    print("Index No:", iNo,"Character:", ichar)
    iNo += 1    

#while true:

strChoice =""
while True:
    strChoice= input("Enter your choice:")
    if strChoice=="N":
        break   
    print (strChoice)


while True:  
    iValue1 = input("Enter your First No:")  
    iValue2 = input("Enter your second No:")
    print(int(iValue1)+ int(iValue2))

    strChoice= input("To Continue Press Y and to Exit Press N:")

    if strChoice.upper()=="N":
        print("Exiting Program....")
        break
    elif strChoice.upper()=="Y":
       continue
    else:
        print("Invalid choice, exiting...")
        break


while True:
    iTable = int(input("Enter the number :"))
    for i in range(10):
        print(iTable,"x", i,"=", iTable*i)
    
    strchoice= input("Press 1 to Continue and Press 2 to Exit..")
    if strchoice=="1":
        continue
    elif strchoice=="2":
        print("Exiting .... ")
        break'''
'''
#user name and password
strUser = input("Enter your user Name:")
strPassword = input("Enter Password:")

#strPassword =python123 
if strPassword=="python123":
    print ("Welcome..")
else:
    print("Invalid Password")'''

'''three attempt 1 output (Invalid Password),
2 (Invalid Password),
3(invalid Password and Exiting)'''


#Hint While True, iAttempt wrong +1 '''exit

'''while True:
    print("This will run forever. Press Ctrl+C to stop!")'''
'''
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1'''

n=1
while n>=3:
    print(n)
    n+=1
else:
    print("Loop Finished!")

#numList = [1,2,3,4,5] - Sum using while


    



