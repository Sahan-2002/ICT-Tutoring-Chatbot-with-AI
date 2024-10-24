
# chatbot.py
import re
from database_setup import Database

class Chatbot:
    def __init__(self):
        self.db = Database()
        self.initialize_responses()
    
    def initialize_responses(self):
        """Initialize basic responses"""
        basic_responses = [
            ("hello", "Hi! How can I help you today?"),
            ("how are you", "I'm doing well, thank you for asking!"),
            ("bye", "Goodbye! Have a great day!"),
            ("help", "I can help you with basic questions. Just type your query!")
        ]
        
        for pattern, response in basic_responses:
            self.db.add_response(pattern, response)
    
    def get_response(self, user_input):
        """Generate a response to user input"""
        # Convert to lowercase for better matching
        user_input = user_input.lower().strip()
        
        # Try to find a matching response in the database
        response = self.db.get_response(user_input)
        
        if response:
            return response
        else:
            return "I'm not sure how to respond to that. Could you rephrase your question?"

    def run(self):
        """Run the chatbot in an interactive loop"""
        print("Chatbot: Hello! Type 'bye' to exit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("Chatbot: Goodbye!")
                break
                
            response = self.get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()