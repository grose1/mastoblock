import sqlite3

# filename to form database
file = "Sqlite3.db"

try:
    conn = sqlite3.connect(file)
    print("Database Sqlite3.db formed.")
except:
    print("Database Sqlite3.db not formed.")

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Sqlite3.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS Sqlite3")

# Creating table
table = """ CREATE TABLE Instances (
            Domain VARCHAR(255),
            Title VARCHAR(255),
            Version VARCHAR(255)
        ); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
