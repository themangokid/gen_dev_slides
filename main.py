
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///offline_db.db', echo=True)

# Create a table
engine.execute('''CREATE TABLE IF NOT EXISTS users
             (user_id INTEGER PRIMARY KEY,
              user_name TEXT,
              user_password TEXT)''')

# Insert values
engine.execute("INSERT INTO users VALUES (1, 'John', 'password1')")
engine.execute("INSERT INTO users VALUES (2, 'Mary', 'password2')")
engine.execute("INSERT INTO users VALUES (3, 'Harry', 'password3')")