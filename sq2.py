#sqlite part 2

import sqlite3

conn = sqlite3.connect('customer2.db')


c = conn.cursor() #create the cursor instance


#c.execute(" SELECT rowid, * FROM customers") #rowid to get autogenerated primary key, this is element 0 now


## USING THE WHERE CLAUSE SEARCHING 

#c.execute(" SELECT rowid, * FROM customers WHERE last_name = 'Baker'")
#using the WHERE clause to search for something specific in field e.g. last_name
# if e.g. age could do WHERE age >= 21 etc
# WHERE last_name LIKE 'B%' for all the ones beginning B
#c.execute(" SELECT rowid, * FROM customers WHERE last_name LIKE 'M%'")
c.execute(" SELECT rowid, * FROM customers WHERE email LIKE '%google.com'")

items = c.fetchall()

print("\n", "Displaying records from database:")
for item in items:
	print("\n" + "ID: " + str(item[0]) + "\n" + "Name :"+ item[1] + " " + item[2] + "\n" + "Email: " + item[3]) 

# display them with the primary key

conn.commit()




# Datatypes are NULL, INTEGER, REAL, TEXT, BLOB // BLOB stored as is e.g. image, audio etc.

conn.close()