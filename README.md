# mastoblock
### A python program aimed at automating the process of blocking instances with out of date and vulnerable software versions from federating with your server. 

It creates a local database of instances you federate with and their software versions. It then uses that database to automatically block those instances with out of date software. 
The id number for the domain blocks returned from your mastodon server are then logged in the database so that they can be unblocked via the api at a later date if need be. 
currently the software version to block is set at anything less than 4.2



1. Run the `create_database.py` script to create your sqlite database and table. You only need to call this once.
2. Create a  `.env` file (see `.env.example` file) replace `instance_url` in the `server_url` field with the domain of your instance.
3. Run main.py
4. Run `DB_to_CSV.py` to export your database as a csv file

## Its a slow process be patient 

# Future Goals
1. Automate blocking domains using the Mastodon API and the database built by this program.
2. Automatic unblocking if remote server updates software
3. Toot as much as tootingly possible 