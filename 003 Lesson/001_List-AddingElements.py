#Adding Elements into List

#append() : end of the list
#extend() : end of the list - multiple
#insert() : to a specific position

#initilaize an empty list 
import os 
os.system("cls")

aList =[]
print(aList)

#append() : add one element
aList.append(10)
print(aList)

aList.append(5)
print(aList)

#insert element
aList.insert(1,7.5)
print(aList)

aList.insert(0,12.5)
print(aList)

#extended
aList.extend([2.5,0,-2.5,-5,-7.5])
print(aList)

strList =["Sun"]
strList.append("Tues")
print(strList)

strList.insert(1,"Mon")
print(strList)

#strExtended = ["Wed","Thu","Fri","Sat"]
#strList.extend(strExtended)

strList.extend(["Wed","Thu","Fri","Sat"])
print(strList)