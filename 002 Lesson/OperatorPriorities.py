#Operators and their priorities
import os
os.system('cls')

'''
| **Priority** | **Operator**     | **Description**                          | **Associativity** |
| ------------ | ---------------- | ---------------------------------------- | ----------------- |
| 1 (Highest)  | `**`             | Exponentiation (Power)                   | Right → Left      |
| 2            | `+x` `-x`        | Unary plus & minus (sign)                | Right → Left      |
| 3            | `*` `/` `//` `%` | Multiplication, Division, Floor Div, Mod | Left → Right      |
| 4 (Lowest)   | `+` `-`          | Addition & Subtraction                   | Left → Right      |
'''
print(2 * 3 % 5)

#Operators and parentheses

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#(25 % 13) = 12 + 100 = 112
#26 = (5* 112 /26 )//2 
# = (560 /26 )//2 
# = 21.54//2 = 10.0 


print(5* 2**3)
print(-2*5)


print((2 ** 4), (2 * 4.), (2 * 4))
#Home Work

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
#Home Work

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
#Home Work


