import sqlite3

connection = sqlite3.connect("programming_journal.db")

def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )
    
def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
                "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date) #to avoid SQL injection
        )

def get_entries():
    return entries