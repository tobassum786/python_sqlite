import sqlite3

# def make_file(db_file):
# 	# Make a new connections and cursor
# 	conn = sqlite3.connect(db_file)
# 	cursor = conn.cursor()

# 	# Make a New Table
# 	cursor.execute("""CREATE TABLE customers(
# 					First_name text,
# 					Last_name text,
# 					Email text,
# 					Age int
# 					)
# 				""")

# 	conn.commit()

# 	conn.close()

def ahow_all():
	# Make a new connections and cursor
	conn = sqlite3.connect("customer.db")
	cursor = conn.cursor()

	cursor.execute("SELECT rowid, * FROM customers")

	users = cursor.fetchall()

	for user in users:
		print(user)

	conn.commit()

	conn.close()


def add_data(list):

	# Make a new connections and cursor
	conn = sqlite3.connect("customer.db")
	cursor = conn.cursor()

	cursor.executemany("INSERT INTO customers VALUES (?,?,?,?)", (list))

	conn.commit()

	conn.close()

def add_one(First_name,Last_name,Email,Age):

	conn = sqlite3.connect("customer.db")
	cursor = conn.cursor()

	cursor.execute("INSERT INTO customers VALUES (?,?,?,?)", (First_name, Last_name, Email, Age))

	conn.commit()
	conn.close()


def delete_one(id):

	conn = sqlite3.connect("customer.db")
	cursor = conn.cursor()

	cursor.execute("DELETE from customers WHERE rowid = (?)", id)

	conn.commit()
	conn.close()