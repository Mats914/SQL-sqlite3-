
# SQLite Movie Database Project

This is a basic Python project for interacting with a SQLite database called `movies.db`. The project includes functionality for selecting, updating, and deleting data from a table named `movie`.

## 🗂 Table Structure

The `movie` table contains the following columns:
- `title` (TEXT)
- `genre` (TEXT)
- `year` (INTEGER)

## 🔧 Features

### 1. View All Movies
Fetch and display all movie records from the database.

```python
cur.execute("SELECT rowid, * FROM movie")
