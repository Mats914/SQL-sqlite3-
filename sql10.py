import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()


cur.execute("SELECT rowid, * FROM movie ")



print(cur.fetchall())
for row in cur.fetchall():
    print(row)
    
db.commit()
db.close()