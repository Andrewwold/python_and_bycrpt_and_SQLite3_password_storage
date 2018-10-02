import sqlite3
import bcrypt

conn = sqlite3.connect('demo.db')
print("Opened database connection")

cursor = conn.execute("SELECT id, username, password, age FROM EMPLOYEES")
for row in cursor:
	print("ID = ", row[0])
	print("USERNAME = ", row[1])
	print("PASSWORD = ", row[2])
	print("AGE = ", row[3], "\n")

	password_hash = row[2]
	print("password_hash")

	user_password =input("PLease Verfy your Password : ")

	valid_password = bcrypt.hashpw(user_password.encode(), password_hash) == password_hash

	print(valid_password)

print("DATA Return is a success")

conn.close()