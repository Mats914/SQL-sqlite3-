import sqlite3

# Connect to the database
db = sqlite3.connect('movies.db')
cur = db.cursor()

# Execute the query
cur.execute("SELECT * FROM movie")

# Fetch all results once and store them
results = cur.fetchall()

# Print all rows
print(results)

# Print the third column (index 2) for each row
for row in results:
    print(row[2])

# Close the database connection
db.close()
