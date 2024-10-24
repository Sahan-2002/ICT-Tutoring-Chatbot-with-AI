# database.py
import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="chatbot.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_tables()
        self.initialize_topics()  # Add this line to initialize topics when database is created
    
    def create_tables(self):
        """Create all necessary tables for the ICT tutoring chatbot"""
        # First, drop existing tables if they exist
        self.cur.execute("DROP TABLE IF EXISTS user_progress")
        self.cur.execute("DROP TABLE IF EXISTS quizzes")
        self.cur.execute("DROP TABLE IF EXISTS topics")
        self.cur.execute("DROP TABLE IF EXISTS responses")
        
        # Responses table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern TEXT NOT NULL,
            response TEXT NOT NULL,
            category TEXT NOT NULL
        )
        """)
        
        # Topics table for structured learning
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_name TEXT NOT NULL,
            difficulty_level TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """)
        
        # Quizzes table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER,
            question TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            options TEXT NOT NULL,
            FOREIGN KEY (topic_id) REFERENCES topics (id)
        )
        """)
        
        # User progress table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            topic_id INTEGER,
            quiz_score INTEGER,
            completion_date DATETIME,
            FOREIGN KEY (topic_id) REFERENCES topics (id)
        )
        """)
        
        self.conn.commit()
    
    def initialize_topics(self):
        """Initialize the basic topics and their quizzes"""
        # Add Computer Basics topic
        self.add_topic(
            "Computer Basics",
            "Beginner",
            "Introduction to computer hardware and software"
        )
        
        # Get the topic ID for Computer Basics
        self.cur.execute("SELECT id FROM topics WHERE topic_name = ?", ("Computer Basics",))
        computer_basics_id = self.cur.fetchone()[0]
        
        # Add quiz questions for Computer Basics
        self.add_quiz_question(
            computer_basics_id,
            "What are the four main components of a computer?",
            "CPU, Memory, Input devices, Output devices",
            '["CPU, Memory, Input devices, Output devices", "Monitor, Keyboard, Mouse, Printer", "Windows, Mac, Linux, Android", "Word, Excel, PowerPoint, Outlook"]'
        )
        
        # Add Programming Fundamentals topic
        self.add_topic(
            "Programming Fundamentals",
            "Intermediate",
            "Basic concepts of programming and algorithms"
        )
        
        # Get the topic ID for Programming Fundamentals
        self.cur.execute("SELECT id FROM topics WHERE topic_name = ?", ("Programming Fundamentals",))
        programming_id = self.cur.fetchone()[0]
        
        # Add quiz questions for Programming Fundamentals
        self.add_quiz_question(
            programming_id,
            "What is a variable in programming?",
            "A container that holds data",
            '["A container that holds data", "A mathematical equation", "A type of loop", "A programming language"]'
        )
        
        self.conn.commit()
    
    def add_topic(self, topic_name, difficulty_level, description):
        """Add a new ICT topic"""
        self.cur.execute("""
        INSERT INTO topics (topic_name, difficulty_level, description)
        VALUES (?, ?, ?)
        """, (topic_name, difficulty_level, description))
        self.conn.commit()
    
    def add_quiz_question(self, topic_id, question, correct_answer, options):
        """Add a new quiz question"""
        self.cur.execute("""
        INSERT INTO quizzes (topic_id, question, correct_answer, options)
        VALUES (?, ?, ?, ?)
        """, (topic_id, question, correct_answer, options))
        self.conn.commit()