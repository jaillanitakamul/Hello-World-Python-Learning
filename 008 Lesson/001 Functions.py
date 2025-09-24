#function (parameters) - Return value 
#create function ... call function 
#lambda function or inline function 
import os 
os.system('cls')
'''
#define function
def greeting():
    print("Welcome to Python Class")

#call of function
greeting()
print("Name:Jaillani")
greeting()
print("Name:Enayat")
greeting()
print("Name:Samim")
greeting()
print("Name:Asad")
greeting()'''

'''

def addNum(x,y,z=0):
    print(f"{x}+{y}+{z}={x+y+z}")

#argument/Parameters
addNum(12,4)
addNum(11,5,1)

#return key
def addNum(x,y):
    return x+y

resultNo = addNum(12,4)
print("Your Result is :", resultNo)


def giveNo():
    return 101

print(giveNo())
'''

def mathOperation(x,y,sign):
    if sign=="+":
        return x+y
    elif sign=="-":
        return x-y
    else:
        return ""
    
c = mathOperation(1,2,"+")
print(c*10)

print("the answer is :",mathOperation(7,2,"-"))


def addNum(x,y):
    return x/y

resultNo = addNum(y=3,x=12)
print("Your Result is :", resultNo)


