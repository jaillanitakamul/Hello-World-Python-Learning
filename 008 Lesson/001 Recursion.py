'''
What is Recursion?

Recursion is when a function calls itself directly or indirectly to solve a problem.
Every recursive function must have:
'''
import os
os.system('cls')
'''
#countdown(10) - 10 9 8 7 6 5 4 3 2 1
def countDown(numValue):
    if numValue==0:
        print("Done!")
    else:
        print(numValue)
        countDown(numValue-1)

countDown(10)'''

#5!= 1x2x3x4x5/5x4x3x2x1

def factResult(nValue):
    if nValue==0 or nValue==1:
        return 1
    return nValue * factResult(nValue -1)

print("Your Result is:", factResult(5))

#fibonacci series 
# 1
# 0 + 1= 1
# 1 + 1 = 2
# 2 +1 = 3
# 3 +2 = 5
# 5 +3 = 8 
# 8 + 5 = 13
# result = (result - 1) + (result -2 ) 
# 13 = 8 + 5
# 21 = 8 + 13 

def pascalTriangle(userValue):
    if(userValue==0)or(userValue==1):
        return userValue
    return pascalTriangle(userValue -1 ) + pascalTriangle(userValue - 2)

print("Your Result is:",pascalTriangle(8))
