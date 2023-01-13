from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/tifin")
q="select * from plus2_products" 
rs=my_conn.execute(q)
for row in rs:
    print(row)
