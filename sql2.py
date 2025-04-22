# Create tables in the database
import sqlite3
con = sqlite3.connect('movies.db')
cursor = con.cursor()
cursor.execute('')

con.close()