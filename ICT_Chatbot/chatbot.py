# chatbot.py
import re
import json
import random
from database_setup import Database

class ICTTutoringChatbot:
    def __init__(self):
        self.db = Database()
        self.current_topic = None
    
    def get_topics(self):
        """Get list of available topics"""
        self.db.cur.execute("SELECT topic_name, difficulty_level, description FROM topics")
        return self.db.cur.fetchall()
    
    def start_topic(self, topic_name):
        """Start learning a specific topic with improved matching"""
        # Make the search case-insensitive
        self.db.cur.execute("""
        SELECT id, topic_name, description 
        FROM topics 
        WHERE LOWER(topic_name) = LOWER(?)
        """, (topic_name,))
        topic = self.db.cur.fetchone()
        
        if topic:
            self.current_topic = topic[0]
            return f"Let's start learning about {topic[1]}!\n{topic[2]}\nType 'quiz' when you're ready to test your knowledge."
        
        # If exact match not found, try partial matching
        self.db.cur.execute("""
        SELECT id, topic_name, description 
        FROM topics 
        WHERE LOWER(topic_name) LIKE LOWER(?)
        """, (f"%{topic_name}%",))
        topics = self.db.cur.fetchall()
        
        if topics:
            if len(topics) == 1:
                self.current_topic = topics[0][0]
                return f"Let's start learning about {topics[0][1]}!\n{topics[0][2]}\nType 'quiz' when you're ready to test your knowledge."
            else:
                response = "Did you mean one of these topics?\n"
                for t in topics:
                    response += f"- {t[1]}\n"
                return response
        
        return "Topic not found. Type 'topics' to see available topics."
    
    def take_quiz(self):
        """Start a quiz for the current topic"""
        if not self.current_topic:
            return "Please select a topic first using 'start topic_name'"
        
        self.db.cur.execute("""
        SELECT question, correct_answer, options 
        FROM quizzes 
        WHERE topic_id = ?
        """, (self.current_topic,))
        questions = self.db.cur.fetchall()
        
        if not questions:
            return "No quiz questions available for this topic."
        
        question = random.choice(questions)
        options = json.loads(question[2])
        
        quiz_text = f"\nQuestion: {question[0]}\n\n"
        for i, option in enumerate(options, 1):
            quiz_text += f"{i}. {option}\n"
        quiz_text += "\nType the number of your answer."
        
        return quiz_text
    
    def process_command(self, user_input):
        """Process user commands and generate responses"""
        command = user_input.lower().strip()
        
        if command == "topics":
            topics = self.get_topics()
            response = "Available Topics:\n\n"
            for topic in topics:
                response += f"📚 {topic[0]} ({topic[1]})\n   {topic[2]}\n\n"
            response += "Type 'start topic_name' to begin learning!"
            return response
            
        if command.startswith("start "):
            topic_name = command[6:].strip()
            return self.start_topic(topic_name)
            
        if command == "quiz":
            return self.take_quiz()
            
        if command == "help":
            return """Available commands:
- topics: Show all available ICT topics
- start topic_name: Begin learning a specific topic
- quiz: Take a quiz on the current topic
- help: Show this help message
- bye: Exit the chatbot"""
        
        return "I'm not sure what you mean. Type 'help' to see available commands."

    def run(self):
        """Run the ICT tutoring chatbot"""
        print("="*50)
        print("Welcome to the ICT Tutoring Chatbot!")
        print("Type 'help' to see available commands")
        print("="*50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() == "bye":
                    print("\nChatbot: Thanks for learning with me! Goodbye!")
                    break
                
                response = self.process_command(user_input)
                print(f"\nChatbot: {response}")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Learning session ended.")
                break
            except Exception as e:
                print(f"\nChatbot: Sorry, I encountered an error. Please try again.")
                print(f"Error details: {str(e)}")

if __name__ == "__main__":
    chatbot = ICTTutoringChatbot()
    chatbot.run()

