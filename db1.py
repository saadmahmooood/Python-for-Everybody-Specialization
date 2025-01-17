import sqlite3

# Connect to the database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the Counts table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Prompt for the file name
fname = input('Enter file name: ')
if len(fname) < 1: 
    fname = 'mbox2.txt'  # Default file name
fh = open(fname)

# Process each line in the file
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]  # Extract the domain name
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit changes to the database after processing all lines
conn.commit()

# Display the top organizations by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts by Organization:")
for row in cur.execute(sqlstr):
    print(f'{row[0]}: {row[1]}')

# Close the cursor and the connection
cur.close()
conn.close()
