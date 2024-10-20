import mysql.connector as sq
def connection():
    try:
        con = sq.connect( host="localhost", user="root", password="mysql",database="hospital_management_system")
        if con.is_connected() == False:
            print("database not connected")
        else:
            return con except
        sq.Error as er:
                print(er)

def insertDoctor():
    try:
        con = connection()
        cur = con.cursor()
        name = input("enter name of doctors")
        age = int(input("enter age of doctors"))
        date_of_birth = input("enter date of birth of doctors")
        mobile_no = input("enter mobile no of doctors")
        specialization = input("enter specialization of doctors")
        fees = int(input("enter fees of doctors"))
        years_of_experience = int(input("enter years of experience"))
        cur.execute("insert	into doctors(name,age,date_of_birth,mobile_no,specialization,fees,years_of_experien ce) values('%s',%d,'%s','%s','%s',%d,%d)"
                    % (
                        name,
                        age,
                        date_of_birth,
                        mobile_no,
                        specialization,
                        fees,
                        years_of_experience,
                      )
                    )
                    print()
                    print("data inserted successfully")
                    con.commit()
                    except sq.Error as er:
                        print(er)

def displayDoctor():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from doctors") for i
        in cur.fetchall():
            print(i)
            except sq.Error as er:
                print(er)

def updateDoctor():
    try:
        con = connection()
        cur = con.cursor()
        name = input("enter name of doctors")
        id = int(input("enter id of doctors"))
        age = int(input("enter age of doctors"))
        date_of_birth = input("enter date of birth of doctors")
        mobile_no = input("enter mobile no of doctors")
        specialization = input("enter specialization of doctors")
        fees = int(input("enter fees of doctors"))
        years_of_experience = int(input("enter years of experience"))
        cur.execute(
            "update doctors set name='%s',age=%d, date_of_birth='%s', mobile_no='%s', specialization='%s', fees=%d,years_of_experience=%d where id= %d"
          % (name,
             age,
             date_of_birth,
             mobile_no,
             specialization,
             fees,
             years_of_experience,
             id,
             )
            )
        print()
        con.commit()
        print("data updated successfully")
        except sq.Error as er:
            print(er)

def deleteDoctor():
    try:
        con = connection()
        cur = con.cursor()
        id = int(input("enter id of doctors whose record you want to delete \nEnter id"))
        cur.execute("delete from doctors where id= %d" % (id))
        print()
        con.commit()
        print("Data Deleted successfully")
        except sq.Error as er:
            print(er)

def insertPatient():
    try:
        con = connection()
        cur = con.cursor()
        name = input("enter name of patients")
        age = int(input("enter age of patients"))
        gender = input("enter gender of patients")
        address = input("enter address of patients")
        contact_no = input("enter contact no of patients")
        date_of_birth = input("enter date of birth of patients")
        consultant_name = input("enter consultant name of patients")
        date_of_consultancy = input("enter date of consultancy of patients")
        department = input("enter department of patients")
        consultancy_fees = int(input("enter consultancy fees of patients"))
        cur.execute("insert into patients(name,age,gender,address,contact_no,date_of_birth,consultant_name,da te_of_consultancy,department,consultancy_fees) values('%s',%d,'%s','%s','%s','%s','%s','%s','%s',%d)"
          % (
                name,
                age,
                gender,
                address,
                contact_no,
                date_of_birth,
                consultant_name,
                date_of_consultancy,
                department,
                consultancy_fees,
            )
        )
        print()
        print("data inserted successfully")
        con.commit()
        except sq.Error as er: print(er)
 

def displayPatient():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from patients")
        for i in cur.fetchall():
            print(i)
            except sq.Error as er: print(er)

def updatePatient():
    try:
        con = connection()
        cur = con.cursor()
        patient_ID = int(input("enter id of patients"))
        name = input("enter name of patients")
        age = int(input("enter age of patients"))
        gender = input("enter gender of patients")
        address = input("enter address of patients")
        contact_no = input("enter contact no of patients")
        date_of_birth = input("enter date of birth of patients")
        consultant_name = input("enter consultant name of patients")
        date_of_consultancy = input("enter date of consultancy of patients")
        department = input("enter department of patients")
        consultancy_fees = int(input("enter consultancy fees of patients"))
        cur.execute(
           " update	patients	set	name='%s',age=%d ,gender='%s',address='%s',contact_no='%s',date_of_birth='%s',consultant_name='%s',date_of_consultancy='%s',department='%s',consultancy_fees=%d where patient_ID= %d"
       % (
           name,
           age,
           gender,
           address,
           contact_no,
           date_of_birth,
           consultant_name,
           date_of_consultancy,
           department,
           consultancy_fees,
           patient_ID,
           )
        )
        print()
        con.commit()
        print("data updated successfully")
        except sq.Error as er:
            print(er)

def deletePatient():
    try:
        con = connection()
        cur = con.cursor()
        patient_ID = int(input("enter id of patients whose record you want to delete \nEnter id"))
        cur.execute("delete from patients where patient_ID= %d" % (patient_ID)) print()
        con.commit()
        print("Data Deleted successfully")
        except sq.Error as er:
            print(er)

def insertRoom():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no"))
        room_type = input("enter room type")
        room_charges_per_day = int(input("enter room charges per day"))
        room_status = input("enter room status")
        patient_name = input("enter patient name")
        cur.execute(
            "insert into room_info(room_no, room_type, room_charges_per_day, room_status, patient_name )values(%d,'%s',%d,'%s','%s')"
               % (room_no, room_type, room_charges_per_day, room_status,patient_name)
            )
        print()
        print("data inserted successfully")
        con.commit()
        except sq.Error as er:
            print(er)

def displayRoom():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from room_info")
        for i in cur.fetchall():
            print(i)
            except sq.Error as er:
                print(er)

def updateRoom():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no"))
        room_type = input("enter room type")
        room_charges_per_day = int(input("enter room charges per day"))
        room_status = input("enter room status")
        patient_name = input("enter patient name of occupied room")
        cur.execute("update Room_Info set room_type='%s',room_charges_per_day=%d,room_status='%s',patient_name='%s 'where room_no= %d"
               % (room_type, room_charges_per_day, room_status, patient_name,room_no)
             )
        print()
        con.commit()
        print("data updated successfully")
        except sq.Error as er:
            print(er)

def deleteRoom():
    try:
        con = connection()
        cur = con.cursor()
        room_no = int(input("enter room no from Room_Info whose record you want to delete\nEnter room no"))
        cur.execute("delete from Room_Info where room_no= %d" % (room_no)) print()
        con.commit()
        print("Data Deleted successfully")
        except sq.Error as er:
            print(er)

def insertBill():
    try:
        con = connection()
        cur = con.cursor()
        bill_date = input("enter bill date")
        name = input("enter name")
        print('1.General ward')
        print('2.Semi Private sharing')
        print('3.Private')
        print('please enter in this format G\S\P')
        room_type = input("enter room type")
        if room_type=='G' or room_type=='g':
            print('room_charges=2000 per day')
        elif room_type=='S' or room_type=='s':
            print('room_charges=5000 per day')
        elif room_type=='P' or room_type=='p':
            print('room_charges=10000 per day')
            print('please multipy the charges with day stay and enter below')
        room_charges = int(input("enter room charges"))
        pathology_fees = int(input("enter pathology fees"))
        doctor_fees = int(input("enter doctor fees"))
        t=room_charges+pathology_fees+doctor_fees
        total=t*0.05
        print('total amount=',total)
        total_amount = int(input("enter total amount of bill"))
        cur.execute(
            "insert into bill_details(bill_date, name, room_type, room_charges, pathology_fees, doctor_fees, total_amount) values('%s','%s','%s',%d,%d,%d,%d)"
        % (bill_date, name, room_type, room_charges, pathology_fees, doctor_fees, total_amount,  )
          )
        print()
        print("data inserted successfully")
        con.commit()
        except sq.Error as er:
            print(er)

def displayBill():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from bill_details")
        for i in cur.fetchall():
            print(i)
            except sq.Error as er:
                print(er)

def updateBill():
    try:
        con = connection()
        cur = con.cursor()
        bill_no = int(input("enter bill no"))
        bill_date = input("enter bill date")
        name = input("enter name")
        room_type = input("enter room type")
        room_charges = int(input("enter room charges"))
        pathology_fees = int(input("enter pathology fees"))
        doctor_fees = int(input("enter doctor fees"))
        total_amount = int(input("enter total amount of bill"))
        cur.execute("update bill_details set bill_date='%s', name='%s', room_type='%s', room_charges=%d, pathology_fees=%d, doctor_fees=%d, total_amount=%d where bill_no= %d"
                    % (
                        bill_date,
                        name,
                        room_type,
                        room_charges,
                        pathology_fees,
                        doctor_fees,
                        total_amount,
                        bill_no,
                        )
                    )
        print()
        con.commit()
        print("data updated successfully")
        except sq.Error as er:
            print(er)
 
def deleteBill():
    try:
        con = connection()
        cur = con.cursor()
        bill_no = int(input("enter bill no from bil_ details whose record you want to delete \nEnterbill no"))
        cur.execute("delete from bill_details where bill_no= %d" % (bill_no))
        print()
        con.commit()
        print("Data Deleted successfully")
        except sq.Error as er:
            print(er)

def menu():
    print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    print()
    while True:
        try:
            print("Select Your Choice From The Given Alternatives") print()
            print(
                "1.Add Record Of Doctors\n2.Update Record Of Existing Doctors\n3.Delete Record Of Doctors\n4.Access All The Records Of Doctors\n5.Add Record Of patients\n6.Update Record Of Existing patients\n7.Delete Record Of patients\n8.Access All The Records Of patients\n9.Add Record Of room info\n10.Update Record Of Existing room info\n11.Delete Record Of room info\n12.Access All The Records Of room info\n13.Add Records Of bill details\n14.Update Record Of Existing bill details\n15.Delete Record Of bill detais\n16.Access All The Records Of bill details\n17.Exit"
                a = input("Enter Your Choice") if a == "1":
 
insertDoctor()
                print()

elif a == "2": displayDoctor() print() updateDoctor() print()

elif a == "3": displayDoctor() print() deleteDoctor() print()

elif a == "4": displayDoctor()

elif a == "5": insertPatient() print()

elif a == "6": displayPatient() print() updatePatient() print()

elif a == "7": displayPatient() print() deletePatient() print()

elif a == "8": displayPatient()
 
elif a == "9": insertRoom() print()

elif a == "10": displayRoom() print() updateRoom() print()

elif a == "11": displayRoom() print() deleteRoom() print()

elif a == "12": displayRoom()

elif a == "13": insertBill() print()

elif a == "14": displayBill() print() updateBill() print()

elif a == "15": displayBill() print() deleteBill() print()

elif a == "16": displayBill()
 

elif a == "17": print("Exiting...") break

else:
print("Invalid choice. Please try again.")

except sq.Error as er: print(er)


def init():
    try:
        con = sq.connect( host="localhost", user="root", password="mysql",)
        if con.is_connected() == False:
            print("Database connection failed")
            return
        cursor = con.cursor()
        cursor.execute("CREATE	DATABASE	IF	NOT	EXISTS hospital_management_system")
        cursor.execute("USE hospital_management_system")

# Create tables if they don't exist
        cursor.execute("""CREATE TABLE IF NOT EXISTS doctors ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),age INT, date_of_birth DATE, mobile_no VARCHAR(20), specialization VARCHAR(255),fees INT, years_of_experience INT,""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS patients ( patient_ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),age INT,gender VARCHAR(10), address VARCHAR(255), contact_no VARCHAR(20), date_of_birth DATE,consultant_name VARCHAR(255), date_of_consultancy DATE, department VARCHAR(255), consultancy_fees INT""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS room_info (room_no INT PRIMARY KEY, room_type VARCHAR(255), room_charges_per_day INT, room_status VARCHAR(20), patient_name VARCHAR(255))""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS bill_details ( bill_no INT AUTO_INCREMENT PRIMARY KEY,bill_date DATE,name VARCHAR(255),room_type VARCHAR(255),room_charges INT, pathology_fees INT, doctor_fees INT, total_amount INT""")
        menu()
        except sq.Error as er:
            print(er)


init()
