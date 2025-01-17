import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Setup database schema
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Prompt for the file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Load the JSON data
with open(fname) as f:
    json_data = json.load(f)

# Debug: Print loaded data
print("Loaded JSON Data:", json_data)

# Insert data into the database
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]  # Extract role as provided in the JSON

    # Debug: Print current entry data
    print(f"Inserting: Name={name}, Title={title}, Role={role}")

    # Insert or ignore user
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore course
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace member with role
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) 
        VALUES ( ?, ?, ? )''', (user_id, course_id, role))

# Commit changes to the database
conn.commit()

# Debug: Check the contents of the Member table
print("Member Table Contents:")
for row in cur.execute('SELECT * FROM Member'):
    print(row)

print("Data loaded successfully.")
