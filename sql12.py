import sqlite3

# Connect to the database
db = sqlite3.connect('movies.db')
cur = db.cursor()

# Delete the row with rowid 3
cur.execute("DELETE FROM movie WHERE title = 'Dunkirk'")

# Show the remaining rows
cur.execute("SELECT rowid, * FROM movie")
data = cur.fetchall()
for row in data:
    print(row)

# Commit the changes and close the connection
db.commit()
db.close()
