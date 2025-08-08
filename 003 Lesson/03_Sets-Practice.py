import os 
os.system('cls')

engList ={'Sherzad','Samsoor Friendly','Farid Sahil'}
programmerList = {'Asad Zahid', 'Hamza Tickety','Jaillani' }
mangList = {'Enayat khan', 'Sherzad','Jaillani' }

#Union Function
employeeList = engList | programmerList | mangList
print(employeeList)

#intersection
engManger = engList & mangList
print(engManger)

#
fullTimeManager = mangList - engList  - programmerList
fullTimeProgrammer = programmerList - engList - mangList

print(fullTimeManager)
print(fullTimeProgrammer)

programmerList.remove('Jaillani')
programmerList.add('Naseeb')
print(programmerList)

programmerList.clear()
print(programmerList)
programmerList.update(['Asadullah 2.0','Hamza 2.0','Naseeb 2.0'])
print(programmerList)