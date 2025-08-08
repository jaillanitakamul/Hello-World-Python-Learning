'''
What is a Tuple in Python?
Tuple is an ordered, immutable collection of items.

Items can be of different data types.

Defined using parentheses () or the tuple() constructor.
'''
import os 
os.system('cls')

'''myTuple = (1,2,3,"Asad", "Ahad", 3.4, True)
print(myTuple)
print(type(myTuple))

print(type(myTuple[1]))

#empty Tuple 
tuple1 = (1,2,3)
tupleNested = (1, (2,3), (4,5))

tuple2 = 1,2,3
print(tuple2)

tuple3 = (5,)
print(type(tuple3))'''

#using list 
liValue = [1,2,3,5]
print(type(liValue))

tupValue = (tuple(liValue))

print (tupValue)
print(type(tupValue))

tupVal = tuple(["Sun","Mon","Tues"])
print(tupVal)

#using builtin function
tupVal1 = tuple('Jaillani')
print(tupVal1)

tupString =tuple(' Farid khan sahil ')
print(tupString.count(' '))
del tupString
print(tupString)

