
"""
1) the project is set up within a virtual environment.
2) This project is backed up at a Github repository.
3) The code is documented with my # notes.
4) The project uses libraries like pandas. 
5) It uses OOP to define a new class.
6) There is a "try-except".
7) There is a while loop.
8) The code makes effor to handle typing errors made by users.

"""

import pandas as pd
import numpy as np
from tabulate import tabulate

# reading csv file
# df is a DataFrame (Pandas table)  

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

df = pd.read_csv("employees.csv", dtype={'phone': int})
df.index = np.arange(1, len(df) + 1)



print("Welcome in the employee database,user.")

menu()
try:
    choice = int(input("Select the number of the command: \n"))
except: 
    print("This is not a number")
    choice = int(input("Select a valid integer: \n"))


while True:

    if choice == 1:
        print("This is a list of available files:\n1.employees.csv \n2.cities.csv.\n")
        
        file1 = int(input("Write the number of the csv file you wish to open: \n"))
        while file1 != 1:
            file1 = int(input("File currently unavailable. Select a different number: \n"))
        print("File selected")
    
    elif choice == 2:
        print(tabulate(df, headers='keys', tablefmt='psql'))
                
    elif choice == 3:
        df = df.sort_values(by='surname')
        print(tabulate(df, headers='keys', tablefmt='psql'))

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
                
        
        new_phone = int(input("Phone: "))
        phonestr = str(new_phone)

        while phonestr.isdigit() != True:
            print("Only numbers, please")
            new_phone = int(input("Phone: "))
                    
        while len(phonestr) < 11:
            print("Add national prefix:  +")
            new_phone = int(input())
            phonestr = str(new_phone)

        while len(phonestr) == 0:
            print("Mandatory: ")
            new_phone = int(input())
            phonestr = str(new_phone)

        while phonestr.isalpha() == True:
            print("Only numbers: ")
            new_phone = int(input())               
            
                                
        df.loc[len(df)] = [new_surname, new_name, new_suffix, new_email, new_phone]
        df.drop_duplicates()
        print(tabulate(df, headers='keys', tablefmt='psql'))
    
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
    

    elif choice == 6:
        try:
            business_card = int(input("Write the number of the person whose data you wish to print out: \n"))
        except: 
            print("This is not a number")
            business_card = int(input("Write the number of the person whose data you wish to print out: \n"))
        selection = df.iloc[[business_card]]
        selection = selection.transpose()
        print(tabulate(selection, headers='keys', tablefmt='psql'))
    
    # I tried using a for loop with the dataframe.items() but it prints gibberish
    # for key, value in df.items():
    # print(key, value)

    elif choice == 7:
        find = input("Enter the value you want to find: \n")
        indexx = df.isin([find]).any(axis=1).idxmax()
        print(indexx)
        sell = df.iloc[[indexx]]
        print(tabulate(sell, headers='keys', tablefmt='psql'))
        
    elif choice == 8:
        row_index = int(input("Write the number of the row you wish to edit:\n "))
        column = input("Write the label of the column you wish to edit:\n ")
        new_value = input("Input the new value: \n")
        df.loc[row_index, column] = new_value
        print(f"This is the updated table: \n {df}")
    
    elif choice ==9:
        df = df.to_csv('employees2.csv')
        print("File exported.\n")
    
    elif choice == 10:
        exit()

    else:
        print("This is not a valid number")

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