import pandas as pd

def main():
    intro()

#Runs main menu and prints intro to program
def intro():
    choose = False
    usrChoice = 0
    print("Welcome to Spendy!  The friendly spending calculator!")
    while (choose != True):
        print("1. List current (SBL) Spending Budget List")
        print("2. Edit/Remove Item")
        print("3. Add New Item")
        print("4. Exit Program")
        usrChoice = int(input("Enter Choice: "))
        if(usrChoice == 1):
            listSBL()
            choose == True
        elif(usrChoice == 2):
            editRM()
            choose == True
        elif(usrChoice == 3):
            addItem()
        elif(usrChoice == 4):
            print("Exiting Program...")
            choose = True
        else:
            print("Please enter a valid input")

#Lists contents of CSV File
def listSBL():
    print("Listing Products... \n" )
    df = pd.read_csv("sbl.csv")
    print(df)
    print("\n")

#Called to edit or Remove an Item to the CSV file
def editRM():
    listSBL()
    df = pd.read_csv("sbl.csv")
    print("Select row to edit by Product name: ")
    
    print(df)
#Called to add an Item to the CSV file
def addItem():
    #Initialize local variables
    usrName = ""
    usrPrice = 0
    usrValue = 0
    usrLink = ""
    usrConf = ""
    #List the contents of the csv
    listSBL()
    print("Add item: \n" )
    #Read CSV to Pandas DataFrame
    df =  pd.read_csv("sbl.csv")
    #Create dictionary to hold information
    newRow = {"Name" : "Null", "Price" : 0, "Value" : 0, "Link" : "http://talkelley3.com/" }
    #Get user input for each category
    print("Please enter information for the new row below:")
    usrName = input("Enter the Name of the product: ")
    usrPrice = int(input("Enter the price of the product: $"))
    usrValue = int(input("Enter the value on a scale of 1-10:"))
    usrLink = input("Enter the link to the item: ")
    #Failsafe to not allow null fields
    if(usrName != "" or usrPrice != 0 or usrValue != "" or usrLink != ""):
        #Apply changes to dictionary
        print("Applying changes to dictionary...")
        newRow["Name"] = usrName
        newRow["Price"] = usrPrice
        newRow["Value"] = usrValue
        newRow["Link"] = usrLink
        print(newRow)
        #Append to csv file and re-display to confirm
        df = df.append(newRow, ignore_index = True)
        print(df)
        print("\n")
        usrConf = input("Confirm addition (Y/N): ")
        if(usrConf == "Y" or usrConf == "y"):
            print("Adding Entry...")
            df.to_csv('sbl.csv', mode='w', header=True, index=False)
        elif(usrConf == "N" or usrConf == "n"):
            print("Addition Cancelled...")
        else:
            print("Failed confirmation. exiting")
    else:
        print("Failure to enter all fields.  Exiting...")


#Statement to run main function if this is the main program and not a module    
if __name__ == '__main__':
    main()