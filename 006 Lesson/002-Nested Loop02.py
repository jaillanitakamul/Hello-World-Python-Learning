#data dictionary
#Key, Value
import os 
os.system('cls')

days_In_Month= {"Jan":31,"Feb":28,"Mar":31,"Apr":30}
'''
print("Month of Jan","has ",days_In_Month["Jan"],"days" )
print("Month of Feb","has ",days_In_Month["Feb"],"days" )
print("Month of Mar","has ",days_In_Month["Mar"],"days" )
print("Month of Apr","has ",days_In_Month["Apr"],"days" )

#key, value

for monthName,nday in days_In_Month.items():
    print("Month of",monthName,"has",nday,"days")

# Month Name " Jan " - Jan-01,Jan-02
'''


monthNames=["Jan","Feb","Mar"]
nDays_in_Month={"Jan":31,"Feb":28,"Mar":31}
'''
for month in monthNames:
    print("Month:", month)
    for nDay in range(1,nDays_in_Month[month]+1):
        print(f"{month} {nDay}", end=" ")
    print("\n")
'''


