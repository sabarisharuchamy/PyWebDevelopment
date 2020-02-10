from db_utils import db_connect
con = db_connect()
cur = con.cursor()
product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
cur.execute(product_sql, ('A Guide to Writing Short Stories', 17.99))
cur.execute(product_sql, ('Data Structures and Algorithms', 11.99))
cur.execute(product_sql, ('Advanced Set Theory', 16.99))
customer_sql = "INSERT INTO customers (first_name, last_name) VALUES (?, ?)"
cur.execute(customer_sql, ('Alan', 'Turing'))
customer_id = cur.lastrowid
print(customer_id)
order_sql = "INSERT INTO orders (date, customer_id) VALUES (?, ?)"
date = "1944-02-22" # ISO formatted date 
cur.execute(order_sql, (date, customer_id))
order_id = cur.lastrowid
print(order_id)
1
li_sql = """INSERT INTO lineitems (order_id, product_id, quantity, total) VALUES (?, ?, ?, ?)"""
product_id = 1
cur.execute(li_sql, (order_id, 1, 1, 7.99))
con.commit()
