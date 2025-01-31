
"""

1) the project is set up within a virtual environment.
2) This project is backed up at a Github repository.
3) The code is documented with my # notes.
4) The project uses libraries like pandas. 
5) It uses OOP to define a new class.
6) There is a "try-except" to handle errors.
7) There is a while loop and conditional statements.
8) The code makes effort to handle typing errors made by users.

"""

import pandas as pd
import numpy as np
from tabulate import tabulate


# Read a CSV file and shift the ID numbering of rows so that the first one is 1 not 0.
print("Welcome in the employee database,user.")
df = pd.read_csv("employees.csv", dtype={'phone': int})
df.index = np.arange(1, len(df) + 1)


# We define a menu of available commands as a function.
def menu():
    return  print("Available commands: \n",\
            "1 - select a file\n",\
            "2 - list all staff\n",\
            "3 - sort by surname\n",\
            "4 - add an employee\n",\
            "5 - delete employees\n",\
            "6 - show a person \n",\
            "7 - find by any parameter\n",\
            "8 - edit data\n",\
            "9 - export to csv\n",\
            "10 - quit")

menu()

# Commands are input as numbers and we need exception handling 
# in case users type something else.
try:
    choice = int(input("Select the number of the command: \n"))
except: 
    print("This is not a number")
    choice = int(input("Select a valid integer: \n"))


# As the program starts withe a menu offered to the users, 
# the main loop also ends with the same menu offerd to the user.
# If the user decides to continue, the menu is offered again.

while True:

    # If-elif statements walk the user through all the numeric commands available.

    # The user must input the number of the file with which he or she intends to work.
    if choice == 1:
        print("This is a list of available files:\n1.employees.csv \n2.cities.csv.\n")
        
        file1 = int(input("Write the number of the csv file you wish to open: \n"))
        while file1 != 1:
            file1 = int(input("File currently unavailable. Select a different number: \n"))
        print("File selected")
    
    # We print the full table in a nice format. 
    elif choice == 2:
        print(tabulate(df, headers='keys', tablefmt='psql'))

    # We shall sort the employees by their surnames alphabetically.             
    elif choice == 3:
        df = df.sort_values(by='surname')
        print(tabulate(df, headers='keys', tablefmt='psql'))

    # The user will input new data and a while loop makes sure
    # that only valid data are entered.
    elif choice ==4:
        new_name = input("Name: ")
        while len(new_name) == 0 or new_name.isalpha() != True:
            new_name = input("This field is mandatory. No numbers: ")

        new_surname = input("Surname: ")
        while len(new_surname) == 0 or new_surname.isalpha() != True:
            new_surname = input("This field is mandatory. No numbers: ")

        new_suffix = input("Sr or Jr: ")
        while new_suffix not in ["Sr", "Jr", "jr", "sr", ""]:
            print("Only Sr or Jr")
            new_suffix = input("Sr or Jr: ")

        new_email = str(input("Email: " ))
        xyz = list(new_email)
    
        while "." not in xyz or "@" not in xyz:    
            new_email = input("This is not proper email format. Try again: ")
            xyz = list(new_email)
        
        while len(xyz) == 0:
            new__email = str(input("Email is mandatory: " ))
                
        new_phone = input("Phone: ")
        phonestr = str(new_phone)
       
        while new_phone.isdigit() != True:
            print("Only numbers, please")
            new_phone = input("Phone: ")
                    
        while len(phonestr) < 11:
            print("Add national prefix:  +")
            new_phone = input()
            phonestr = str(new_phone)

        while len(phonestr) == 0:
            print("Mandatory: ")
            new_phone = input()
            phonestr = str(new_phone)

        while new_phone.isalpha() == True:
            print("Only numbers: ")
            new_phone = input()               
            
        # We use the .loc method and the len function to insert
        # the new data at the very end.
        # If the given employee is already somewhere in the table, 
        # the new data will be dropped.
        df.loc[len(df)] = [new_surname, new_name, new_suffix, new_email, new_phone]
        df.drop_duplicates()
        print(tabulate(df, headers='keys', tablefmt='psql'))
    
    # We use the len function to coun the number of rows.
    # Then we use the .drop method to delete the selected row.
    # It is advisable to adapt the IDs of the rows to suit the new situation.
    elif choice == 5:
        rows = len(df)
        print(f"The number of available rows is: {rows}")
        
        delete_no = int(input("Write the number of the row you wish to delete: \n"))
        while delete_no > rows:  
            delete_no = int(input("Write a valid number: \n"))
        
        df = df.drop(labels=int(delete_no), axis=0)
        df = df.reset_index(drop=True)
        
        print(f"This is what the table looks like without the deleted data: \n")
        print(tabulate(df, headers='keys', tablefmt='psql'))
    
    # We ask the user to input the number of the row with the searched person.
    # We need to handle the exception when the user mistakenly inputs something else instead of integers..
    # The .iloc method localises the row in the dataframe.
    # The .transpose method flips the axes so the keys (name, surname etc.)
    # are above each other vertically.
    elif choice == 6:
        try:
            business_card = int(input("Write the number of the person whose data you wish to print out: \n"))
        except: 
            print("This is not a number")
            business_card = int(input("Write the number of the person whose data you wish to print out: \n"))
        selection = df.iloc[[business_card]]
        selection = selection.transpose()
        print(tabulate(selection, headers='keys', tablefmt='psql'))
    
    # The .isin method finds the row with the searched for value.
    # The .iloc method allows us to find and print this row.
    elif choice == 7:
        find = input("Enter the value you want to find: \n")
        indexx = df.isin([find]).any(axis=1).idxmax()
        print(f"Row number: {indexx}")
        sell = df.iloc[[indexx]]
        print(tabulate(sell, headers='keys', tablefmt='psql'))

    # The user defines which row and which column shall be edited.
    # The changes are implanted via the .loc method  
    elif choice == 8:
        row_index = int(input("Write the number of the row you wish to edit:\n "))
        column = input("Write the label of the column you wish to edit:\n ")
        new_value = input("Input the new value: \n")
        df.loc[row_index, column] = new_value
        print(f"This is the updated table: \n {df}")
    
    # Modified data is exported into a new file 
    elif choice ==9:
        df = df.to_csv('employees_modified.csv')
        print("File exported.\n")
    
    elif choice == 10:
        exit()

    # We need to provide for situations when
    # the input is incorrect number or data type. 
    else:
        print("This is not a valid number")


    # The while loop ends with a question if the user wishes to quit.
    # We need to tke into account that the user input may be typed incorrectly.

    continuation = input("Do you wish to continue? Y or N?\n")
    cont = continuation.upper()
    if cont not in ["Y","N"]:
        continuation = input("Invalid. Only Y or N: \n")
        cont = continuation.upper()
               
    if cont == "Y":
        menu()
        try:
            choice = int(input("Select the number of the command: \n"))
        except: 
            print("This is not a number")
            choice = int(input(" Select the number of the command: \n"))
    
    else:
        quit()