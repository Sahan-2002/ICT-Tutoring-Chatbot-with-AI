import sqlite3

# Initialize score globally
score = 0

def ask_quiz():
    """Fetch a quiz question from the database and check the user's answer."""
    global score

    # Example: Fetch a random quiz question from the database
    conn = sqlite3.connect("quiz_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM quiz ORDER BY RANDOM() LIMIT 1")
    question, correct_answer = cursor.fetchone()
    conn.close()

    print(f"Question: {question}")
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == correct_answer.lower():
        score += 1
        print("Correct! 🎉")
    else:
        print(f"Wrong. The correct answer was: {correct_answer}")

    print(f"Your current score: {score}\n")

def chatbot_response(user_input):
    """Generate a response based on the user's input."""
    if user_input.lower() == "start quiz":
        ask_quiz()
    elif user_input.lower() == "check score":
        print(f"Your total score is: {score}")
    else:
        print("Sorry, I didn't understand that. Try 'start quiz' or 'check score'.")

# Main chatbot loop
def main():
    print("Welcome to the ICT Tutoring Chatbot!")
    print("Type 'start quiz' to begin or 'check score' to view your score.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! See you next time.")
            break
        chatbot_response(user_input)

if __name__ == "__main__":
    main()
