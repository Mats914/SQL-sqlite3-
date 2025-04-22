import sqlite3
con = sqlite3.connect('movies.db')
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movie (title TEXT, genre TEXT, year INTEGER)")

#cursor.execute("INSERT INTO movie(title, genre, year) VALUES('oppenheimer', 'drama', 2023)")

#Anthor way to insert data into the table
#cursor.execute("INSERT INTO move VALUES('oppenheimer', 'drama', 2023)")

cursor.execute("INSERT INTO users(name, age) VALUES('john', 25)")

con.commit()
con.close()