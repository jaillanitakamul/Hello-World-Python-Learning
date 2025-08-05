'''
| Operator | Description             | Example  | Result |
| -------- | ----------------------- | -------- | ------ |
| `+`      | Addition                | `5 + 3`  | 8      |
| `-`      | Subtraction             | `10 - 4` | 6      |
| `*`      | Multiplication          | `6 * 2`  | 12     |
| `/`      | Division (float result) | `7 / 2`  | 3.5    |
| `//`     | Floor Division (int)    | `7 // 2` | 3      |
| `%`      | Modulus (remainder)     | `7 % 2`  | 1      |
| `**`     | Exponent (power)        | `2 ** 3` | 8      |
'''

import os 
os.system('cls')

# Type Conversion (Casting)
#Using the math Module (sqrt,pow,floor,ceil,pi,factorial)

#Exponentiation

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Multiplication
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#Division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#Integer division (floor division)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

#Remainder (modulo)
print(14 % 4)
print(12 % 4.5)

#Addition
print(-4 + 4)
print(-4. + 8)

#Subtraction 
print(-4 - 4)
print(4. - 8)
print(-1.1)

# Type Conversion (Casting)

strValue = "100"
strValue2="200"

print(strValue + strValue2)
print(int(strValue) + int(strValue2))
print(float(strValue) + int(strValue2))