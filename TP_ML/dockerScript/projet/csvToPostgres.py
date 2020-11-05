import csv
import psycopg2
conn = psycopg2.connect("host=172.28.1.4 dbname=anime user=aymeric password=aymeric")
cur = conn.cursor()
cur.execute('DROP TABLE users')
conn.commit()
cur.execute("""
    CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    Title varchar,
    Type varchar,
    Episodes integer,
    Status varchar,
    Start airing varchar,
    End airing varchar,
    Starting season varchar,
    Broadcast varchar,
    Producers integer,
    Licensors varchar,
    Studios varchar,
    Sources varchar,
    Genres varchar,
    Duration varchar,
    Rating varchar,
    Score real,
    Scored by int,
    Members int,
    Favorites int,
    Description varchar
)
""")
conn.commit()
with open('dataanime.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Ne pas faire le header
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (DEFAULT,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()