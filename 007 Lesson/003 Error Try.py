import os
os.system('cls')  

try:
    iVal1 = int(input("Enter your first No: "))
    iVal2 = int(input("Enter your second No: "))

    if iVal2 == 0:
        raise ValueError("Come on man, why divide by Zero!")

    print(f"{iVal1} / {iVal2} = {iVal1 / iVal2}")

except ValueError as e:
    print("Error:", e)
else:
    print("Else Message is here")
finally:
    print("I am done")


