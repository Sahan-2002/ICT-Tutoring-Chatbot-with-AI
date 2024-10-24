
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
            # Greetings
            ("hello", "Hi! How can I help you today?"),
            ("hi", "Hello! What can I do for you?"),
            ("hey", "Hey there! How can I assist you?"),
            ("good morning", "Good morning! How can I help you today?"),
            ("good afternoon", "Good afternoon! What can I do for you?"),
            ("good evening", "Good evening! How may I assist you?"),
            
            # Farewells
            ("bye", "Goodbye! Have a great day!"),
            ("goodbye", "Bye! Hope to chat with you again soon!"),
            ("see you", "See you later! Take care!"),
            
            # General queries
            ("how are you", "I'm doing well, thank you for asking! How about you?"),
            ("what's up", "Not much, just here to help! What's on your mind?"),
            ("who are you", "I'm an ICT chatbot created to help answer your questions!"),
            
            # Help and Support
            ("help", "I can help you with various topics. Just ask me a question!"),
            ("what can you do", "I can provide information about various ICT topics, answer general questions, and assist with basic queries."),
            ("menu", "Here are some things I can help with:\n1. General information\n2. Technical support\n3. Basic conversation"),
            
            # ICT-specific queries
            ("what is ict", "ICT stands for Information and Communication Technology. It includes all digital technology that assists individuals, businesses, and organizations in using information."),
            ("computer", "A computer is an electronic device that processes data according to instructions stored in its memory."),
            ("programming", "Programming is the process of creating a set of instructions that tell a computer how to perform a task."),
            ("internet", "The Internet is a global network of connected computers that allows information sharing and communication worldwide."),
            
            # Technical Support
            ("error", "Could you please describe the error you're experiencing in detail? I'll try my best to help."),
            ("not working", "I'm sorry to hear that. Could you tell me what exactly isn't working? This will help me assist you better."),
            ("how to fix", "To help you fix the issue, I'll need more specific information about what you're trying to fix."),
            
            # Common Questions
            ("weather", "I'm sorry, I don't have access to real-time weather information. Please check a weather website or app."),
            ("time", "I don't have access to real-time information, but you can check the time on your device."),
            ("thank you", "You're welcome! Is there anything else I can help you with?"),
            ("thanks", "You're welcome! Let me know if you need anything else!"),
            
            # Educational Topics
            ("what is coding", "Coding is the process of writing instructions for computers using programming languages. It's how we create software, websites, and apps."),
            ("what is database", "A database is an organized collection of structured information or data, typically stored electronically in a computer system."),
            ("what is network", "A network is a collection of computers and other devices that are connected together to share resources and communicate."),
            
            # Problem-solving
            ("slow computer", "Here are some tips to speed up your computer:\n1. Close unused programs\n2. Delete temporary files\n3. Run virus scan\n4. Check available storage"),
            ("virus", "To protect from viruses:\n1. Use antivirus software\n2. Keep software updated\n3. Be careful with downloads\n4. Don't click suspicious links"),
            ("backup", "It's important to backup your data regularly. You can use:\n1. External hard drives\n2. Cloud storage\n3. Network storage"),
            
            # Fun responses
            ("tell me a joke", "Why don't programmers like nature? It has too many bugs! 😄"),
            ("are you human", "No, I'm a chatbot - a computer program designed to help and chat with you!"),
            ("do you sleep", "I don't sleep - I'm always here to help!")
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