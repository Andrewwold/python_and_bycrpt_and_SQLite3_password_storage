import bcrypt
import sqlite3

user_name = input("PLease enter a name ")
user_password = input("PLease enter a Password ")
age = int(input("PLease enter an age "))

hashed_password = bcrypt.hashpw(user_password.encode("utf8"), bcrypt.gensalt())

print(hashed_password)


conn = sqlite3.connect('demo.db')
print("Opened database connection")

conn.execute("INSERT INTO EMPLOYEES (ID,USERNAME,PASSWORD,AGE) \
	VALUES (1,?,?,?)", (user_name, hashed_password, age));

conn.commit()

print("All records Entered")

conn.close()