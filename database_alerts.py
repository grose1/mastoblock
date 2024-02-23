# This is the first attempts at setting up alerts for when a Mastodon server is under spam attacks. This script connects to the postgresql database and counts how many rows are present and compairs the count to the last time it was ran.
# It counts the rows from the accounts table that lists all accounts known to your server. 
# spammers like to create lots of accounts and instances to spam with at a high rate, idea is that this will catch those accounts being added to your database at a high rate and alert you. 
# this is intended to eventually be run on a schedule to monitor how quickly records are being added to the database.
# You will most likely need to establish a baseline of how many accounts are logged into your database on an average and then set the threshold for this program. 

import psycopg2
import smtplib, ssl

connection = psycopg2.connect(database="DATABASE", user="USER", password="PASSWORD",
                              host="SERVER", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) from accounts;")
try:
    with open("demofile2.txt", "r") as file:
        last_line = file.readlines()[-1]
except:
    pass
# Fetch all rows from database
record = cursor.fetchall()
r = record[0]
r2 = r[0]
print("Data from Database:- ", r2)
w = str(r2)
f = open("demofile2.txt", "a")
f.write(w)
f.write('\n')
f.close()


try:
    last = int(last_line)

    dif = r2 - last
    print('difference:', dif)
    if dif >= 100:
        smtp_server = "smtp.SERVER"
        port = 587  # For starttls
        sender_email = "SENDER EMAIL"
        password = "PASSWORD"
        receiver_email = "RECIVER EMAIL"
        message = "Possible Spam Attack on Mastodon Server"
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
except:
    pass
