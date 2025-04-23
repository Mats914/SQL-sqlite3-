import sqlite3

# Connect to the database
db = sqlite3.connect('movies.db')
cur = db.cursor()

# Update the title of the movie with rowid 3
cur.execute("UPDATE movie SET title = 'test' WHERE rowid = 3")

# Update the genre of the movie with rowid 3
cur.execute("UPDATE movie SET genre = 'crime' WHERE rowid = 3")


# Select all rows including rowid
cur.execute("SELECT rowid, * FROM movie")
data = cur.fetchall()

# Print each row
for row in data:
    print(row)

# Commit changes and close connection
db.commit()
db.close()
