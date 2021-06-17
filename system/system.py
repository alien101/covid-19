import sqlite3




# create database if not exists otherwise open existed database
connection = sqlite3.connect("q2.db")
print("Database has been connected!")

crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE IF NOT EXISTS patients (   
last VARCHAR(20),  
first VARCHAR(40),
hk_ID VARCHAR(20) PRIMARY KEY,
phone_num int,
address VARCHAR(50),
dob int, 
gender VARCHAR(1))"""

# execute the statement
crsr.execute(sql_command)


def mainMenu():
    print("")
    print("")
    print("")
    print("******************************************************************")
    print("*         WELCOME TO PRIVATE CLINIC INFORMATION SYSTEM           *")
    print("******************************************************************")
    print("*                                                                *")
    print("*                 1. Enter a new record.                         *")
    print("*                 2. Retrieve all records.                       *")
    print("*                 3. Export all records to a text file.          *")
    print("*                 4. Exit the system.                            *")
    print("*                                                                *")
    print("******************************************************************")
    print("")
    print("")
    print("")

    try:
        x = int(input("Please make your choice (1/2/3/4): "))
        print("")
        print("")
        print("")
        if (x == 1):
            opt_1()
            mainMenu()
        elif (x == 2):
            opt_2()
            mainMenu()
        elif(x == 3):
            opt_3()
            mainMenu()
        elif(x == 4):
            connection.close()
            print("Database has been closed.")

    except ValueError:
        print("Invalid choice.")
        mainMenu()


def opt_1():
    try:
        last = str(input("Step 1. Please enter the LAST name of the patient: "))
        first = input("Step 2. Please enter the FIRST name of the patient: ")
        hkid = input("Step 3. Please enter the HKID of the patient (e.g. A123456(7) ): ")
        phone = int(input("Step 4. Please enter the Mobile phone number of the patient: "))
        address = input("Step 5. Please enter the address of the patient: ")
        birth = int(input("Step 6. Please enter the Date of Birth of the patient (YYYMMDD) : "))
        sex = input("Step 7. Please enter the gender of the patient (M/F): ")
    except ValueError:
        print("Invalid input.")
    crsr.execute("""INSERT INTO patients VALUES (?, ?, ?, ?, ?, ? ,?);""", (last, first, hkid, phone, address, birth, sex))
    connection.commit()
    print("Record has been inserted successfully!")

def opt_2():
    crsr.execute("""SELECT * FROM patients;""")
    rows = crsr.fetchall()
    row_iterator = iter(rows)
    try:
        row = next(row_iterator)
        print_r(row)
        while(True):
            x = input("Press enter to continue")
            print("")
            row = next(row_iterator)
            if(x == ""):
                print_r(row)
    except StopIteration:
        print("Last record reached. Returning back to menu.")

def print_r(row):
    print("HKID         : {2} \nLast name    : {0} \nFirst name   : {1} \nGender       : {6} \nDOB          : {5} "
          "\nMobile #     : {3} \nAddress      : {4}".format(*row))
    print("")
    print("")
    print("")



def opt_3():
    crsr.execute("""SELECT * FROM patients;""")
    rows = crsr.fetchall()

    f = open("output.txt", "w")

    for r in rows :
        f.write("HKID: " + r[2] + "\n")
        f.write("Patient name: " + r[1] + " " + r[0] + "\n")
        f.write("Gender: " + r[6] + "\n")
        f.write("DOB: " + str(r[5]) + "\n")
        f.write("Mobile #: " + str(r[3]) + "\n")
        f.write("Address: " + r[4] + "\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    f.close()
    print("All records have been exported.")




mainMenu()






















