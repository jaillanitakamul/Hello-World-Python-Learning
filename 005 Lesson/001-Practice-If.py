# User email input validation
# Rules:
# - No spaces
# - Not empty
# - Must contain exactly one @
# - Must contain at least one .
# - Must be at least 10 characters
# - Must include one uppercase and one lowercase
# - Must start with an alphabet and end with an alphabet or digit
# - Must end with .com, .org, or .net

import os
os.system('cls')

# userEmail = input("Enter your Email ID: ")
userEmail = "jaillanitakamul@gmail.com"

emailDomain = (".com", ".org", ".net")

# Cleaning input
userEmail = userEmail.strip()

# Split for name part
if "@" in userEmail:
    nameSplit = userEmail.split("@")
    userName = nameSplit[0]
    firstLetter = userName[0]
else:
    nameSplit = [""]
    userName = ""
    firstLetter = ""

# Checks
if userEmail == "":
    print("Empty email address not allowed")
elif " " in userEmail:
    print("Spaces are not allowed in email")
elif "@" not in userEmail or "." not in userEmail:
    print("Email address must contain both '@' and '.'")
elif userEmail.count("@") != 1:
    print("Too many '@' signs, only one allowed")
elif len(userEmail) < 10:
    print("The email must be at least 10 characters long")
elif userName.upper() == userName:
    print("Must have at least one lowercase letter")
elif userName.lower() == userName:
    print("Must have at least one uppercase letter")
elif not firstLetter.isalpha():
    print("Email should start with an alphabet")
elif not (userEmail[-1].isalpha() or userEmail[-1].isdigit()):
    print("Email should end with an alphabet or digit")
elif not userEmail.endswith(emailDomain):
    print("Invalid domain, must end with .com, .org, or .net")
else:
    print("Valid Email Address")
