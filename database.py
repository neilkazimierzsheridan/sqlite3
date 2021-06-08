import sqlite3

#DATABASE FUNCTIONS

#Function: query db and return all the records 
def show_all():
	conn = sqlite3.connect('customer3.db')
	c = conn.cursor() #create the cursor instance

	c.execute("SELECT rowid, * FROM customers")

	items = c.fetchall()

	print("\n", "Displaying records from database:")
	for item in items:
		print("\n" + "ID: " + str(item[0]) + "\n" + "Name :"+ item[1] + " " + item[2] + "\n" + "Email: " + item[3]) 

	conn.commit()
	conn.close()

#Function: add a new record to table
def add_one(first, last, email):
	conn = sqlite3.connect('customer3.db')
	c = conn.cursor() #create the cursor instance
	#insert the first last and mail into the table
	c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
	conn.commit()
	conn.close()

#Function: delete a record from table
def delete_one(id):
	conn = sqlite3.connect('customer3.db')
	c = conn.cursor() #create the cursor instance
	#delete from table using primary key passed to us as id
	str(id)
	c.execute("DELETE FROM customers WHERE rowid = (?)", id)
	conn.commit()
	conn.close()

#Function: add many records to table
def add_many(list):
	conn = sqlite3.connect('customer3.db')
	c = conn.cursor() #create the cursor instance
	#pass the list using executemany
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	conn.commit()
	conn.close()

#Function: lookup email
def email_lookup(email):
	conn = sqlite3.connect('customer3.db')
	c = conn.cursor() #create the cursor instance
	c.execute("SELECT rowid,* FROM customers WHERE email = (?)", (email,))
	items = c.fetchall()

	print("\n", "Displaying records from database:")
	for item in items:
		print("\n" + "ID: " + str(item[0]) + "\n" + "Name :"+ item[1] + " " + item[2] + "\n" + "Email: " + item[3]) 

	conn.commit()
	conn.close()







