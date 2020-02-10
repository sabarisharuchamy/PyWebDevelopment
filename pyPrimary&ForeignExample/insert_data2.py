from db_utils import db_connect, create_customer, create_order, create_lineitem
con = db_connect()
cur = con.cursor()
##knuth_id = create_customer(con, 'Donald', 'Knuth')
##knuth_order = create_order(con, knuth_id, '1967-07-03')
##knuth_li1 = create_lineitem(con, knuth_order, 2, 1, 17.99)
##knuth_li2 = create_lineitem(con, knuth_order, 3, 1, 11.99)
##codd_id = create_customer(con, 'Edgar', 'Codd')
##codd_order = create_order(con, codd_id, '1969-01-12')
##codd_li = create_lineitem(con, codd_order, 4, 1, 16.99)
try:
##    codd_id = create_customer(con, 'Edgar', 'Codd')
##    codd_order = create_order(con, codd_id, '1969-01-12')
##    codd_li = create_lineitem(con, codd_order, 4, 1, 16.99)

    # commit the statements
    update_sql = "UPDATE products SET price = ? WHERE id = ?"
    cur.execute(update_sql, (10.99, 2))
    con.commit()
except:
    # rollback all database actions since last commit
    con.rollback()
    raise RuntimeError("Uh oh, an error occurred ...")
