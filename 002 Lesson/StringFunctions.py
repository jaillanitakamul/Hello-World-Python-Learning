'''
| Method                   | Description                        | Example                                           |
| ------------------------ | ---------------------------------- | ------------------------------------------------- |
| `len(string)`            | Returns the length of the string   | `len("Python") → 6`                               |
| `string.lower()`         | Converts to lowercase              | `"PY".lower() → py`                               |
| `string.upper()`         | Converts to uppercase              | `"hi".upper() → HI`                               |
| `string.title()`         | Converts to Title Case             | `"hello world".title() → Hello World`             |
| `string.strip()`         | Removes spaces from both ends      | `"  hi  ".strip() → hi`                           |
| `string.replace(a,b)`    | Replaces `a` with `b`              | `"apple".replace("a","A") → Apple`                |
| `string.split()`         | Splits string into list by spaces  | `"a b c".split() → ['a','b','c']`                 |
| `"separator".join(list)` | Joins list into a string           | `" ".join(['I','love','Python']) → I love Python` |
| `string.find(sub)`       | Returns first index of substring   | `"banana".find("na") → 2`                         |
| `string.count(sub)`      | Counts occurrences of substring    | `"banana".count("na") → 2`                        |
| `string.startswith()`    | Checks if string starts with value | `"hello".startswith("he") → True`                 |
| `string.endswith()`      | Checks if string ends with value   | `"hello".endswith("lo") → True`                   |

'''

#Removing Spaces strip(), lstrip(), rstrip()
#Finding and Replacing find(str), replace(str)
#Count count(char) Length len(str)

import os 
os.system('cls')

varString = "This is my name"
print(len(varString))

varName = "Naseeb ahmadzai"
print(varName.lower())
print(varName.upper())
print(varName.capitalize())
print(varName.title())

varText = "     Pyhton          "
print(len(varText))

print(varText.strip())
print(len(varText.strip()))

print(varText.lstrip())
print(len(varText.lstrip()))

print(varText.rstrip())
print(len(varText.rstrip()))

varString = "I Hate Programming"
print(varString.find("Hate"))
print(varString.replace("Hate","Love"))

myWord = "Python30"
print(myWord.isalpha())
print(myWord.isdigit())
print(myWord.isalnum())

varWord ="Python with, friends is fun, and without, friends is hell"
print(varWord)
print(varWord.split())
print(varWord.split(','))

splitText = varWord.split(',')
joinedText ="".join(splitText)

print(joinedText)

vartxt = "Banana"
print("the number of a occurance",vartxt.count("a"),"\nthe number of n occurance", vartxt.count('n'))
print(vartxt.count("n"))
print(vartxt.count("b"))

varStartText = "Hello World"
print(varStartText.endswith("d"))

import re

strWordText = "Programming if fun"
#Vowels
vowel_count = len(re.findall(r"[aeiouAEIOU]", strWordText))
vowelWords = re.findall(r"[aeiouAEIOU]", strWordText)
print(vowel_count)
print(vowelWords)

strRemoveSpace = "H e L L O"
#remove the spaces 


text = "Programing is fun"
vowels = "aeiouAEIOU"

found_vowels = [char for char in text if char in vowels]
print("Vowels found:", found_vowels)

