import sqlite3

conn = sqlite3.connect('demo.db')

print("Database connection success.")

conn.execute('''CREATE TABLE EMPLOYEES
         (ID INT PRIMARY KEY     NOT NULL,
         USERNAME           TEXT    NOT NULL,
         PASSWORD		TEXT	NOT NULL,
         AGE            INT     NOT NULL);''')
print("Table created successfully");


conn.close()