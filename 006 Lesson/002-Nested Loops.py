import os 
os.system('cls')

modelList = ["Hyundai","Toyota","Honda","BMW"]
colorList = ["Red","White","Black"]

'''
for color in colorList:
    print(modelList[0], "color:", color)

for color in colorList:
    print(modelList[1], "color:", color)

for color in colorList:
    print(modelList[2], "color:", color)

for color in colorList:
    print(modelList[3], "color:", color)

for m in modelList:
    print(m)

for c in colorList:
    print(c)

#outerloop 
#innerloop

for m in modelList:
    for c in colorList:
        print("color:", c, "car:", m, end="\t")
    print()
'''
'''
*
**
***
****

for i in range(1,4):
    print("*")

print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)

for i in range(1,5):
    print("*"*i)

n=5
for i in range (1,n+1):
    print('*'*i)

n=5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()'''

matrixList = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]
#row and columns
print(matrixList[0][2])
print(matrixList[2][3])

'''
print(matrixList[0][0])
print(matrixList[0][1])
print(matrixList[0][2])
print(matrixList[0][3])

print(matrixList[1][0])
print(matrixList[1][1])
print(matrixList[1][2])
print(matrixList[1][3])

print(matrixList[2][0])
print(matrixList[2][1])
print(matrixList[2][2])
print(matrixList[2][3])

'''

for row in matrixList:
    for item in row:
        print(item, end=" ")
    print()