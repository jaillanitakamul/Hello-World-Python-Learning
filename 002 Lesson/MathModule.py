#Squre Root
import os
os.system('cls')

import math
'''print(math.sqrt(16))
print(2**3)
print(math.pow(2,3))

print(math.floor(3.9))
print(math.ceil(3.1))

print(math.pi)
print(math.factorial(5))'''

#pi* *(radius power of 2)
radius = int(input("Enter Radius Value:"))
#area = math.pi * (math.pow(radius,2))
area = math.pi * (radius**2)
print("Total Area:", area)