
email = input("Enter your email: ")
user_input = input("Enter your password/username: ")

if user_input == "":
    print("Input must not be empty.")

elif len(user_input) < 8:
    print("Input must be at least 8 characters long.")

elif user_input.upper() == user_input:   # means no lowercase
    print("Input must contain at least one lowercase letter.")

elif user_input.lower() == user_input:   # means no uppercase
    print("Input must contain at least one uppercase letter.")

elif user_input == email:
    print("Input must not be the same as the email.")

elif " " in user_input:
    print("Input must not contain spaces.")

elif not (user_input[0].isalnum() and user_input[-1].isalnum()):
    print("Input must start and end with a letter or digit.")

else:
    print("✅ Input is valid!")
