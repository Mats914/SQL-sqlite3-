import sqlite3

# Connect to the database
db = sqlite3.connect('movies.db')
cur = db.cursor()

# Execute the query to select all rows from the movie table
cur.execute("SELECT * FROM movie")


#cur.execute("SELECT title FROM movie")
#cur.execute("SELECT year FROM movie")
#cur.execute("SELECT genre FROM movie")

# Iterate through the fetched data and print each row
for row in cur.fetchall():
    print(row)

# Close the connection to the database
db.close()



