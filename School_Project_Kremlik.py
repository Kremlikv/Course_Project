


"""
by Vítězslav Kremlík
mail: kremlik@seznam.cz
Prague, February 2025

 == A school project: An employee database == 

1) The project is set up within a virtual environment.
2) This project is backed up at a Github repository.
3) The code is documented with # notes.
4) The project uses libraries like pandas. 
5) It uses OOP to define a function
6) There is a "try-except" to handle errors.
7) There are while loop and conditional statements.
8) The code makes effort to handle typing errors made by users.
9) Any changes are remembered by the programme and can be stored for later use

"""

import pandas as pd
from tabulate import tabulate

print("")
print("Welcome in the employee database.")
print("")

# We define a menu of available commands as a function.
def menu():
    return  print("Available commands: \n\n",\
            "1 - original data\n",\
            "2 - open last save\n",\
            "3 - sort\n",\
            "4 - add\n",\
            "5 - delete\n",            
            "6 - find\n",\
            "7 - edit\n",\
            "8 - save changes\n",\
            "9 - quit\n",\
            "")

menu()

# Safeguards for proper use of the menu:
# 1) Users must type in only numbers
# 2) Users need to start with option 1 or 2 to open a dataset
def check_dataframe_exists(df_name):
        if df_name not in locals():
            print("Select option 1 or 2 first to open a file")
try:
    choice = int(input("Select the number of the command: \n"))
except: 
    print("This is not a number")
    choice = int(input("Select a valid integer: \n"))
while choice not in [1,2]:
    check_dataframe_exists('df_working')
    choice = int(input())
    

global df

# The program starts with a menu offered to users, 
# When the users complete an operation, they are asked whether to quit.
# If they wish to continue, the menu is offered again.

while True:

    # If-elif statements walk the users through all the numeric commands available.

    # Option 1 - open the original file
    if choice == 1:
        print("Original data: \n")   
        df_orig = pd.read_csv("employees_original.csv", dtype={'phone': int})
        df_orig.index = df_orig.index + 1     
        print(tabulate(df_orig, headers='keys', tablefmt='psql')) 
        global df_working
        df_working = df_orig
        
    
    # Option 2 - open the last saved changes in the file
    elif choice == 2:
        print("Last saved data: \n") 

        df_last_save = pd.read_csv("employees_last_save.csv", dtype={'phone': int})
        
       # It is advisable to re-index the rows to reflect any changes.
       # I changed the default python indexing so that the first row is not 0 but 1.  
       # This is done everywhere in the programme
        df_last_save.reset_index(drop=True, inplace=True)
        df_last_save.index = df_last_save.index + 1
    
        print(tabulate(df_last_save, headers='keys', tablefmt='psql'))
        df_working = df_last_save 
       
        

    # Option 3 - sort the employees by user-selected criteria.             
    elif choice == 3:
        
        # At the beginning of each step the working database is uploaded to "df" dataframe
        # We work with "df" dataframe
        # In the end we export the "df" back to a working dataframe "df_working" 

        df = df_working                  

        by_what = input("Options to sort the data by:\n1 - id\n2 - surname\n3 - name\n4 - email\n5 - phone\n:")
        while by_what not in ["1","2","3","4","5"]: 
            by_what = input("Invalid choice.\nYou can sort data by id, surname, name, email or phone.\nTry again.\n:")
        
        if by_what == "1":
            df = df.sort_values(by="id")    
        if by_what == "2":
            df = df.sort_values(by="surname")
        if by_what == "3":
            df = df.sort_values(by="name")        
        if by_what == "4":
            df = df.sort_values(by="email")
        if by_what == "5":
            df = df.sort_values(by="phone")
             
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1
        
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
        df_working = df

    # Option 4 - users can add new employees to the databse
    # A while loop makes sure that only valid data are entered.
    elif choice ==4:
        
        df = df_working
        
        new_id = input("id: ")
        while len(new_id) == 0:
            new_id = input("This field is mandatory: ")

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
            new_email = input("This is not proper email format. Try again: \n")
            xyz = list(new_email)
        
        while len(xyz) == 0:
            new__email = str(input("Email is mandatory: " ))
                
        # When entering a phone number, only numbers are allowed.
        # We also want the phone numbers with international prefixes.
        new_phone = input("Phone: ")
        phonestr = str(new_phone)
       
        while new_phone.isdigit() != True:
            print("Only numbers, please")
            new_phone = input("Phone: ")
                    
        while len(phonestr) < 11:
            print("Add national prefix: ")
            new_phone = input()
            phonestr = str(new_phone)

        while len(phonestr) == 0:
            print("Mandatory: ")
            new_phone = input()
            phonestr = str(new_phone)

        while new_phone.isalpha() == True:
            print("Only numbers: ")
            new_phone = input()               
            
        # The .loc method and the len function is used to insert new data at the very end.
        # If the given employee is already somewhere in the table, the duplicity will be dropped.
        df.loc[len(df)] = [new_id, new_surname, new_name, new_suffix, new_email, new_phone]
        df.drop_duplicates()   
        df.reset_index(drop=True, inplace=True)    
        df.index = df.index + 1
        
        print(tabulate(df, headers='keys', tablefmt='psql'))
        df_working = df
    
    # The len function is used to count the number of rows.
    # The .drop method is used to delete the selected row.
   
    elif choice == 5:
        
        df = df_working
        
        rows = len(df)
        print(f"The number of available rows is: {rows}")
        
        delete_no = int(input("Write the number of the row you wish to delete: \n"))
        while delete_no > rows:  
            delete_no = int(input("Write a valid number: \n"))
        
        df = df.drop(labels=int(delete_no), axis=0)
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1       
                
        print(f"This is what the table looks like without the deleted data: \n")
        print(tabulate(df, headers='keys', tablefmt='psql'))
        df_working = df
    
    # Option 6 - Find and display data of a specific person
    # The .isin method finds the row with the desired value.
    # The .iloc method allows us to find and print this row.
    # The .transpose method flips the axes 
    # so the keys (name, surname etc.) are above each other vertically.     
    elif choice == 6:
        # This while loop makes sure that if the input value is not found in the table
        # the user is asked to write a correct one.   
        df =df_working
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
        find = input("Enter the value you want to find.\nIt can be somebody's name, surname, id, phone or email:\n:")    
        while find not in df.values:
            find = input("Not found. Try again.\n:") 
                 
        indexx = df.isin([find]).any(axis=1).idxmax()    
        print(f"Row number: {indexx}")
        selection = df.iloc[[indexx-1]]       
        selection = selection.transpose()
        
        print(tabulate(selection, headers='keys', tablefmt='psql'))
       
        df_working = df
    
    # Option 7 - editing
    # The user defines which row and which column shall be edited.
    # The changes are implanted via the .loc method  
    elif choice == 7:
        
        # We make sure that only existing rows can be selected by the user
        # and that no nonsense non-integer values are input
        
        df = df_working        
        df.reset_index(drop=True, inplace=True)   
        df.index = df.index + 1
        print(tabulate(df, headers='keys', tablefmt='psql'))
        rows = len(df)
        print(f"The number of available rows is: {rows}")        
        try:
            row_index = int(input("Write the number of the row you wish to edit:\n ")) 
        except:
            row_index = int(input("Write a number: \n"))         
        while int(row_index) > rows: 
            try:
                row_index = int(input("Write a valid row number:\n ")) 
            except:
                row_index = int(input("Write a correct number: \n")) 
        
        # We show the table to the user so that he/she can see 
        # what is available to choose from
        
        chosen = df.iloc[[row_index-1]]
        print(f"This is row: {row_index-1}")
        print(tabulate(chosen, headers='keys', tablefmt='psql'))

        column = input("Write the label of the column you wish to edit:\n ")                  
        while column not in ["surname", "name", "id", "suffix", "email", "phone"]: 
            column = input("This is not a valid column heading: ")

        new_value = input("Input the new value: \n")

        df.loc[row_index, column] = new_value 
        df.reset_index(drop=True, inplace=True)   
        
        print(f"This is the updated table: \n {df}")
        df_working = df
    
    # Option 8 - Modified data is exported into a new CSV file 
    elif choice ==8:
        df = df_working
        
        df.reset_index(drop=True, inplace=True)
        df.index = df.index + 1
        df = df.to_csv('employees_last_save.csv', index = False)    
        print("File exported.\n")
    
    # Option 9 - quit programme and say goodbye
    elif choice == 9:
        print("Good bye")
        exit()

    # We need to provide for situations when
    # the input is incorrect number or data type. 
    else:
        print("This is not a valid number")


    # The while loop ends with a question if the user wishes to quit.
    # We need to take into account that the user input may be typed incorrectly.

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
    
    # If the user responds N to the Y/N question about whether to continue,
    # the program says good bye and quits 
    else:
        print("Good bye!")
        quit()