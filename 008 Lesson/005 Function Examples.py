#Function with string and conditions
#Modules (Internal)
import os 
os.system('cls')

'''
def check_Case(userText):
    if userText.isupper():
        print("Upper Case")
    elif userText.islower():
        print("Lower Case")
    else:
        print("Mixed Case")

check_Case("HELLO")
check_Case("Hello")
check_Case("hello")

def printItems(itemsList):
    for eachItem in itemsList:
        print(eachItem)
    
printItems([1,2,3,5,6,])
printItems(["Asad","Ahad"])
printItems(["Male","Female","Binary","Shemale","HeShe"])'''

'''
#tuple = [10,90,80,40,1]
tupleValue =(10,90,80,40,1)
print("First Value",tupleValue[0],"Last Value", tupleValue[-1])
'''
def getValues(numberValues):
    return(numberValues[0], numberValues[-1])


resultType = getValues((10,90,80,40,1))
print(resultType)

print(type(resultType))    



