# database.py
import sqlite3

class Database:
    def __init__(self, db_name="chatbot.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Create the necessary tables for the chatbot"""
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern TEXT NOT NULL,
            response TEXT NOT NULL
        )
        """)
        self.conn.commit()
    
    def add_response(self, pattern, response):
        """Add a new pattern-response pair to the database"""
        self.cur.execute("INSERT INTO responses (pattern, response) VALUES (?, ?)",
                        (pattern, response))
        self.conn.commit()
    
    def get_response(self, pattern):
        """Get a response for a given pattern"""
        # The fix is in these two lines:
        self.cur.execute("SELECT response FROM responses WHERE pattern LIKE ?",
                        ('%' + pattern + '%',))
        result = self.cur.fetchone()  # Remove .execute - this was the error
        return result[0] if result else None
