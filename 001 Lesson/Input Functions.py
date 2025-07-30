#input function
import os 
os.system('cls')

xname = input("Please, enter your name:")
print("the entered name is : ", xname)

num1=float(input("Enter your first number:"))
num2= float(input("Enter your second number:"))

print(type(num1))
print(type(num2))
res = num1 + num2

print(type(res))
print(res)

res = int(num1)+ int(num2)

print(type(res))
print (res)