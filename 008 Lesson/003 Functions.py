#function with undefined variables/parameters
import os
os.system('cls')
'''
def sumNum(x,y,z=0,m=0,l=0,n=0):
    return x+y+z+m+n+l

print("sum no:", sumNum(1,2,4,7,1,2,3))'''
'''
*args
def totalNo(*no):
    return sum(no)

print(totalNo(1,2))
print(totalNo(1,2,7))
print(totalNo(1,2,8,8,7,6))
print(totalNo(1))
print(totalNo(1,2,6,4,3,2,1,2))
print(totalNo())'''

#*kwargs 
def print_detail(**details):
    for key, value in details.items():
        print(f"{key}:{value}")

print_detail(name="Samsor", age=40)
print_detail(firstname="Enayat", surName="Kila",city="Dari-e-Noor")