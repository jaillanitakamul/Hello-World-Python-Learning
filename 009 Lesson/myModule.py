def printMessage(actionStr):
    if actionStr=="Insert":
        print("Record Inserted Successfully!")
    elif actionStr=="Update":
        print("Update Done Successfully!")
    elif actionStr=="Delete":
        print("Row Deleted Successfully!")
    else:
        print("Unknown Action Request")