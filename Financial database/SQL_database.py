#Import the libraries
import sqlite3

#Connect to database
conn = sqlite3.connect('stocks_data.db')

#Create a cursor
cursor = conn.cursor()

#Create a Table
cursor.execute("""CREATE TABLE IF NOT EXISTS exchange (
        id INTEGER, 
        name TEXT NOT NULL,
        currency,
        code TEXT NOT NULL UNIQUE,
        PRIMARY KEY(id)
    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS company (
        id INTEGER, 
        name TEXT NOT NULL,
        industry TEXT,
        sector TEXT,
        hq_location TEXT,
        security_id INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY (security_id) REFERENCES security (id)
    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS security (
        id INTEGER, 
        ticker TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        company_id INTEGER,
        exchange_id INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY (company_id) REFERENCES company (id),
        FOREIGN KEY (exchange_id) REFERENCES exchange (id)
    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS security_price (
        id INTEGER, 
        date text NOT NULL,
        open decimal NOT NULL,
        high decimal NOT NULL,
        low decimal NOT NULL,
        close decimal NOT NULL,
        volume integer,
        adj_close decimal NOT NULL,
        security_id integer,
        PRIMARY KEY(id),
        FOREIGN KEY (security_id) REFERENCES security (id) 
    );""")

#Commit our command
conn.commit()

#Close our connection
conn.close()