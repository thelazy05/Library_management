import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS library
                         (id INTEGER PRIMARY KEY,Name TEXT,Author TEXT,PY TEXT, ISBN TEXT)''')
        self.con.commit()

    def insert(self, name, author, date, isbn):
        self.cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?)',(name,author,date,isbn))
        self.con.commit()
    
    def search(self, name='', author='', date='', isbn=''):
        query = "SELECT * FROM library"
        conditions = []
        params = []

        if name:
            conditions.append("Name LIKE ?")
            params.append(f"%{name}%")
        if author:
            conditions.append("Author LIKE ?")
            params.append(f"%{author}%")
        if date:
            conditions.append("PY LIKE ?")
            params.append(f"%{date}%")
        if isbn:
            conditions.append("ISBN LIKE ?")
            params.append(f"%{isbn}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        self.cur.execute(query, params)
        return self.cur.fetchall()



    def select(self):
        self.cur.execute('SELECT * FROM library')
        return self.cur.fetchall()

    def delete(self,id):
        self.cur.execute('DELETE from library WHERE id = ?',(id,))
        self.con.commit()
