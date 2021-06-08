#sqlite part 1

import sqlite3

conn = sqlite3.connect('customer2.db')

#conn = sqlite3.connect(':memory:')
#just keep it in memory instead

c = conn.cursor() #create the cursor instance
'''
#not much point in making it over and over!
c.execute(""" CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")

#insert records one at a time
#c.execute("INSERT INTO customers VALUES ('Tippy', 'Timperton', 'tippy@google.com')") #put a record into the table
#c.execute("INSERT INTO customers VALUES ('Winkle', 'Winner', 'winkwin@google.com')")
'''
''' #Inserting many records by way to a python list
many_customers = [
					('Crinkle', 'Crafter', 'crinky@google.com'),
					('Dinky', 'Doer', 'dingy@google.com'),
					('Minty', 'Mouther', 'minty@google.com'),
					('Biscuit', 'Baker', 'baker@google.com')
				]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) #execute many instead, with placeholder then
#passing the list
'''


#QUERYING THE DATABASE

c.execute(" SELECT * FROM customers")
#print(c.fetchone())
#print(c.fetchone()[0]) #let me get the first element from the tuple
#print(c.fetchmany(3)) #get three records

#print(c.fetchall())

items = c.fetchall()
#print(items)

#Ways to display the data we get from the database


print("\n", "DISPLAYING RECORDS FROM DATABASE", "\n")


print("\n", "Printing all the records in the table and all their elements", "\n")
for item in items:
	print(item)

print("\n", "Or printing just the first and second elements, so name", "\n")
for item in items:
	print(item[0], item[1]) #first and second elements from tuple ,notice there is a space between them?

print("\n", "Or let's format them nice!", "\n")
for item in items:
	print("\n" + "Name: " + item[0] + " " + item[1] + "\n" + "Email: " + item[2]) 

conn.commit()




# Datatypes are NULL, INTEGER, REAL, TEXT, BLOB // BLOB stored as is e.g. image, audio etc.

conn.close()