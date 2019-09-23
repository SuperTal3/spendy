import csv

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
            print("Exiting Program")
        else:
            print("Please enter a valid input")

def listSBL():
    print("Listing Products...")

def editRM():
    #Coolish
    print("Cool")

def addItem():
    #Cool
    print("Cool")
    
def main():
    intro()