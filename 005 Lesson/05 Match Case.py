import os
os.system('cls')

countryCode = input("Please enter your country 2 digit code:")
'''
if countryCode=="AF":print("Afghanistan")
elif countryCode=="US": print("USA")
elif countryCode=="IN": print("India")
else: print ("Out of World.")
'''
#Switch Case Default - Match Case _ underscore
match countryCode:
    case "AF": print("Afghanistan")
    case "US": print("United States of America")
    case "In": print("India")
    case _: print("Out of World!")


