# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import ICTTutoringChatbot  # Import the chatbot

app = Flask(__name__)
chatbot = ICTTutoringChatbot()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend page

# Route to handle chatbot interaction
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message received"}), 400
    
    # Process user input with the chatbot
    bot_response = chatbot.process_command(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
