import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()
#cur.execute("SELECT * FROM movie ORDER BY title")
#cur.execute("SELECT * FROM movie ORDER BY year")
#cur.execute("SELECT * FROM movie ORDER BY genre")


#cur.execute("SELECT * FROM movie ORDER BY year DESC")
#cur.execute("SELECT * FROM movie ORDER BY year ASC")
#cur.execute("SELECT rowid, * FROM movie ")
#cur.execute("SELECT rowid, * FROM movie LIMIT 2 ")

cur.execute("SELECT rowid, * FROM movie ORDER BY year LIMIT 1")


#print(cur.fetchone())
#print(cur.fetchmany(4))
print(cur.fetchall())
for row in cur.fetchall():
    print(row)
    
db.commit()
db.close()