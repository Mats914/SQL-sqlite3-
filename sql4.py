import sqlite3
con = sqlite3.connect('movies.db')
cursor = con.cursor()
movies = [
    ('Oppenheimer', 'Drama', 2023),
    ('The Dark Knight', 'Action', 2008),
    ('Inception', 'Sci-Fi', 2010),
    ('Interstellar', 'Sci-Fi', 2014),
    ('Dunkirk', 'War', 2017)
]
cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", movies)




con.commit()
con.close()