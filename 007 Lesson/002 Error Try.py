import os 
os.system('cls')

#Custom Message

try:
    firstVal = 10
    secondVal = 0

    if secondVal==0:
        raise ValueError("Why always divided by Zero!")
    print(f"Result - {firstVal}/{secondVal}={firstVal/secondVal}")

except ValueError as e:
    print("Error Message:", e)

finally:
    print("Program Ended")