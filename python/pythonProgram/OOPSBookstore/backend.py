import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows=self.cur.fetchall()
        return rows

    def insert(self,title,author,year,ISBN):
        self.cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
        self.conn.commit()

    def delete(self,id):
        self.cur.execute("DELETE FROM  bookstore WHERE id=?",(id,))
        self.conn.commit()

    def search(self,title="",author="",year="",ISBN=""):
        self.cur.execute("SELECT * from bookstore where title=? or author=? or year=? or ISBN=?",(title,author,year,ISBN))
        rows=self.cur.fetchall()
        return rows

    def update(self,id,title,author,year,ISBN):
        self.cur.execute("UPDATE bookstore SET title=?,author=?,year=?,ISBN=? WHERE id=?",(title,author,year,ISBN,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


    #connect()
    ##insert("The Water", "Mr. Grahm","1989",127)
    ##update(2,"The Land1","Mr. Smith","1988",8899)
    ##delete(4)
    #print(view())
    #print(search(author="Mr. Grahm"))
