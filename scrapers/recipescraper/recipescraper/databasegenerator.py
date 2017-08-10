import sqlite3

database = "/home/adam/Personal Projects/scrapers/recipescraper/recipedb.sqlite3"
conn = sqlite3.connect(database)
c = conn.cursor()
c.execute('''CREATE TABLE recipe(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, author text, ingredients text, recipeyield text, difficulty text, totaltime text, activetime text, directions text);
''')
c.execute('''CREATE TABLE ingredient(name text PRIMARY KEY)''')