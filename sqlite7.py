import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()
cur.execute("SELECT * FROM movie")

#print(cur.fetchone())
#print(cur.fetchmany(4))
print(cur.fetchall())
for row in cur.fetchall():
    print(row[2])
    
db.commit()
db.close()