import sqlite3
import os
import csv
from sqlite3 import Error
# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

 # Export data into CSV file
print("Exporting data into CSV............")
cursor = conn.cursor()
cursor.execute("select * from Instances")
with open("out.csv", 'w',newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)
conn.close()
