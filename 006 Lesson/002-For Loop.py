import os 
os.system('cls')

#break continue and pass + If condition

'''for i in range(10):
    if i == 5:
        break
    print("result is : ",i)

for i in range(10):
    if i==4:
        continue
    else:
        print("result is : ", i)

for i in range(10):
    if i==6:
        pass 
    print("result is :", i)

for i in range(10):
    if i == 3:
        continue   # skip 3
    elif i == 5:
        break      # stop at 5
    elif i==2:
        pass
    print(i)

stuName =["Samim","Zahid","Sahil","Hamza","Jaillani"]

for student in stuName:
    if student=="Zahid":
        break
    print("Allowed Students:", student)

for marks in range(0,100,10):
    if marks ==60:
        break
    print("fail Marks are :", marks)


resultMarks = [50,60,89,90,100,75,65]
totalMarks = 0 
averageMarks=0

for marks in resultMarks:
    totalMarks = marks + totalMarks

averageMarks= totalMarks/len(resultMarks)
print("Your Total Marks are :",totalMarks, " which makes the average : ", averageMarks )
'''

#table 2 2*1=2
numList = [1,2,3,4,5,6,7,8,9,10]
numTable = int(input("Enter your number : "))

for num in numList:
    print (numTable, " * ", num , " = ", numTable*num)


#Pythonic Functions  - Sum 
resultMarks = [50,60,89,90,100,75,65]
print("Total marks are : ", sum(resultMarks))
