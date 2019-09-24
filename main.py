import pandas as pd

def main():
    intro()

#Runs main menu and prints intro to program
def intro():
    choose = False
    usrChoice = 0
    print("Welcome to Spendy!  The friendly spending calculator!")
    print("Spendy (TM) is designed to take in your wishlist, with certain parameters, and inform you which items you should purchase!")
    while (choose != True):
        print("1. List current (SBL) Spending Budget List")
        print("2. Edit/Remove Item")
        print("3. Add New Item")
        print("4. List Pay Stub")
        print("5. Edit/Update Pay")
        print("6. ANALYZE DATA")
        print("7. Exit Program")
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
            listPay()
        elif(usrChoice == 5):
            editPay()
        elif(usrChoice == 6):
            analyzeData()
            choose = True
        elif(usrChoice == 7):
            print("Exiting Program...")
            choose = True
        else:
            print("Please enter a valid input")

#Lists contents of CSV File
def listSBL():
    print("Listing Products... \n" )
    #Reads csv file from code
    df = pd.read_csv("sbl.csv")
    #Display contents of DataFrame to user
    print(df)
    print("\n")

def listPay():
    print("Listing Balance... \n")
    #Reads csv file from code
    df = pd.read_csv("pay.csv")
    #Display contents of DataFrame to user
    print(df)
    print("\n")

#Called to edit or Remove an Item to the CSV file
def editRM():
    #Initialize local variables
    usrName = ""
    usrPrice = 0
    usrValue = 0
    usrLink = ""
    usrConf = ""
    usrRowNum = 0

    #Run listSBL() to display contents of SBL for user
    listSBL()
    #Read CSV file to dataframe
    df = pd.read_csv("sbl.csv")
    #Get user input for Row number to edit
    print("Select row to edit by number: ")
    usrRowNum = int(input("Enter number: "))
    #Locate row via row number
    rowDF = df.loc[usrRowNum]
    #Convert the new dataframe to Dictionary for editing
    editRow = rowDF.to_dict()
    #Print dictionary so user can confirm row is selected properly
    print(editRow)
    print("\n")
    #Get user input for values of Dictionary entry, and if they don't enter anything use the previous values
    usrName = str(input("Enter the Name of the product: ") or editRow["Name"])
    usrPrice = int(input("Enter the price of the product: $") or editRow["Price"])
    usrValue = int(input("Enter the value on a scale of 1-10:") or editRow["Value"])
    usrLink = str(input("Enter the link to the item: ") or editRow["Link"])

    #Failsafe to not allow null fields - In this case won't happen because of the precautions we took when getting the updates
    if(usrName != "" and usrPrice != 0 and usrValue != "" and usrLink != ""):

        #Apply changes to dictionary
        print("Applying changes to dictionary...")
        editRow["Name"] = usrName
        editRow["Price"] = usrPrice
        editRow["Value"] = usrValue
        editRow["Link"] = usrLink
        #Redisplay edited row, for user confirmation
        print(editRow)
        usrConf = str(input("Confirm addition (Y/N): ") or "null")
        if(usrConf == "Y" or usrConf == "y"):
            print("Adding Entry...")
            #Drop the previous version of the entry from the dataframe
            df.drop(df.index[usrRowNum], inplace=True)
            #Append updated row to the end of dataframe
            df = df.append(editRow, ignore_index = True)
            #Write dataframe to csv
            df.to_csv('sbl.csv', mode='w', header=True, index=False)
        elif(usrConf == "N" or usrConf == "n"):
            #Cancel addition
            print("Addition Cancelled...")
        else:
            print("Failed confirmation. exiting")
    else:
        print("Failure to enter all fields.  Exiting...")
    listSBL()

def editPay():
    #Initialize local variables
    usrName = ""
    usrPrice = 0
    usrValue = 0
    usrLink = ""
    usrConf = ""
    usrRowNum = 0

    #Run listSBL() to display contents of SBL for user
    listPay()
    #Read CSV file to dataframe
    df = pd.read_csv("pay.csv")
    #Get user input for Row number to edit
    print("Select row to edit by number: ")
    usrRowNum = int(input("Enter number: "))
    #Locate row via row number
    rowDF = df.loc[usrRowNum]
    #Convert the new dataframe to Dictionary for editing
    editRow = rowDF.to_dict()
    #Print dictionary so user can confirm row is selected properly
    print(editRow)
    print("\n")
    #Get user input for values of Dictionary entry, and if they don't enter anything use the previous values
    usrName = str(input("Enter current balance: ") or editRow["Balance"])
    usrPrice = int(input("Enter the price of the product: $") or editRow["Hourly"])
    usrValue = int(input("Enter the value on a scale of 1-10:") or editRow["PaydayAMT"])
    usrLink = str(input("Enter the link to the item: ") or editRow["PaydayFrequency"])

    #Failsafe to not allow null fields - In this case won't happen because of the precautions we took when getting the updates
    if(usrName != "" and usrPrice != 0 and usrValue != "" and usrLink != ""):

        #Apply changes to dictionary
        print("Applying changes to dictionary...")
        editRow["Balance"] = usrName
        editRow["Hourly"] = usrPrice
        editRow["PaydayAMT"] = usrValue
        editRow["PaydayFrequency"] = usrLink
        #Redisplay edited row, for user confirmation
        print(editRow)
        usrConf = str(input("Confirm addition (Y/N): ") or "null")
        if(usrConf == "Y" or usrConf == "y"):
            print("Adding Entry...")
            #Drop the previous version of the entry from the dataframe
            df.drop(df.index[usrRowNum], inplace=True)
            #Append updated row to the end of dataframe
            df = df.append(editRow, ignore_index = True)
            #Write dataframe to csv
            df.to_csv('pay.csv', mode='w', header=True, index=False)
        elif(usrConf == "N" or usrConf == "n"):
            #Cancel addition
            print("Addition Cancelled...")
        else:
            print("Failed confirmation. exiting")
    else:
        print("Failure to enter all fields.  Exiting...")
    listPay()

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
    #Get user input for each category, and default to null values if someone doesn't do it right
    print("Please enter information for the new row below:")
    usrName = str(input("Enter the Name of the product: ") or "")
    usrPrice = int(input("Enter the price of the product: $") or 0)
    usrValue = int(input("Enter the value on a scale of 1-10:") or 0)
    usrLink = str(input("Enter the link to the item: ") or "")
    print("\n")
    print(newRow)
    print("\n")

    #Failsafe to not allow null fields
    if(usrName != "" and usrPrice != 0 and usrValue != "" and usrLink != ""):
        #Apply changes to dictionary
        print("Applying changes to dictionary...")
        newRow["Name"] = usrName
        newRow["Price"] = usrPrice
        newRow["Value"] = usrValue
        newRow["Link"] = usrLink
        print(newRow)
        #Append to dataframe and re-display to confirm
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

def analyzeData():
    print("Analyzing Data Now...")
    #Import salary data into salDF
    salDF = pd.read_csv("pay.csv")
    #Load into dictionary
    #Locate row via row number
    sal = salDF.loc[0]
    #Convert the new dataframe to Dictionary for calculations
    salDict = sal.to_dict()
    print(salDict)
    #Import SBL data into sblDFk
    sblDF = pd.read_csv("sbl.csv")
    #Calculate Time to Buy for each item, in hours, and pay period.
    for i in sblDF.count():
        
        
    #Calculate based on value, and price, whether purchasing is a good option



#Statement to run main function if this is the main program and not a module    
if __name__ == '__main__':
    main()