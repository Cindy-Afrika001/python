import sqlite3

conn = sqlite3.connect('acer.db')
print("opened database successfully")

cursor = conn.execute("SELECT * from EMPLOYEE")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4])
print("Operation done successfully")
conn.close()
