import sqlite3

# Connect to the database
db = sqlite3.connect('movies.db')
cur = db.cursor()

# Execute the query to select all rows from the movie table
cur.execute("SELECT * FROM movie")



# Iterate through the fetched data and print each row
for row in cur.fetchall():
    print(row[0])

# Close the connection to the database
db.close()

