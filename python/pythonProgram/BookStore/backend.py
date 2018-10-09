import sqlite3

def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
    conn.commit()
    conn.close()

def insert(title,author,year,ISBN):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM  bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(title="",author="",year="",ISBN=""):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * from bookstore where title=? or author=? or year=? or ISBN=?",(title,author,year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def update(id,title,author,year,ISBN):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookstore SET title=?,author=?,year=?,ISBN=? WHERE id=?",(title,author,year,ISBN,id))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.close()
    return rows


connect()
##insert("The Water", "Mr. Grahm","1989",127)
##update(2,"The Land1","Mr. Smith","1988",8899)
##delete(4)
print(view())
print(search(author="Mr. Grahm"))
