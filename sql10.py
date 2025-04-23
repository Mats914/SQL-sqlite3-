import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()


#cur.execute("SELECT  * FROM movie  WHERE title = 'oppenheimer'")
#cur.execute("SELECT * FROM movie WHERE LOWER(genre) != 'war'")


# AND operator
cur.execute("SELECT * FROM movie WHERE  genre = 'war' AND year = 2017")

# OR operator
cur.execute("SELECT * FROM movie WHERE genre = 'war' OR year = 2017")

# UPPER function
cur.execute("SELECT * FROM movie WHERE title = UPPER('OppEnheimer')")

# LOWER function
cur.execute("SELECT * FROM movie WHERE title = LOWER('OppEnheimer')")

# LIKE operator
cur.execute("SELECT * FROM movie WHERE title LIKE 'O%'")
cur.execute("SELECT * FROM movie WHERE title LIKE '%Oppenheimer%'")
cur.execute("SELECT * FROM movie WHERE title LIKE '%Oppenheimer'")
cur.execute("SELECT * FROM movie WHERE title LIKE '%0'")

# BETWEEN operator
cur.execute("SELECT * FROM movie WHERE year BETWEEN 2010 AND 2015")
print(cur.fetchall())
for row in cur.fetchall():
    print(row)
    
db.commit()
db.close()