# Read data from the table

import dbm
import sqlite3
db = sqlite3.connect('movies.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM movie")
# or this way
#cursor.execute("SELECT title, genre, year FROM movie")
