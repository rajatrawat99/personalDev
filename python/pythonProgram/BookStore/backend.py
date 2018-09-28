def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
    conn.commit()
    conn.close()
