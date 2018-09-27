import psycopg2

def create_table():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=(?)",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=(?), price=(?) WHERE item=(?)",(quantity,price,item))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

choice=input("Press 1 to enter data \n Press 2 to delete data \n Press 3 to update data \n Press 4 to view data \n")
if choice == "1":
    item=input("Enter the name of ITEM ")
    quantity=int(input("Enter Quantity "))
    price=float(input("Enter Price "))
    insert(item,quantity,price) # or insert("Wine Glass",2,30.5)

elif choice == "2":
    item=input("Enter the name of ITEM to delete ")
    delete(item) # or insert("Wine Glass")

elif choice == "3":
    item=input("Enter the name of ITEM which you want to modify ")
    quantity=int(input("Enter Quantity "))
    price=float(input("Enter Price "))
    update(quantity,price,item) # or insert("Wine Glass")

elif choice == "4":
    print(view())
