'''
try:
except:
else:
finally:
'''
import os 
os.system('cls')
'''
while True:
    try:
        iVal1= int(input("Enter your Age:"))
        print(f"Your Age is : {iVal1}")
    except Exception as e:
        print("Error:",e)'''
'''
try:
    firstVal = 10
    secondVal = 0

    print(f"{firstVal}/{secondVal}={firstVal/secondVal}")

except ZeroDivisionError as ex:
    print("Error Zero Division:", ex)
except ValueError as ex:
    print("Error Value:", ex)
except TypeError as ex:
    print("Error Type:", ex)
except Exception as ex:
    print("Error:", ex)
    '''

try:
    firstVal = 10
    secondVal = 0
    print(f"Result - {firstVal}/{secondVal}={firstVal/secondVal}")

except Exception as ex:
    print("Error Type:", type(ex).__name__)
    print("Error Message:", ex)

finally:
    print("Program Ended")
    

