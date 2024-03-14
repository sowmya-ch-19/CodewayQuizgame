# Import necessary modules
import sys

def welcome_message():
    print("Welcome to the General Knowledge Quiz Game!")
    print("You will be asked multiple choice and fill-in-the-blank questions.")
    print("Try to get as many correct as possible. Good luck!\n")

def load_questions():
    # This function returns a list of questions. Each question is a dictionary.
    # Modify this list to add more questions or change topics.
    return [
        {"question": "What is the capital of France?", "options": ['Paris', 'Berlin', 'Madrid', 'Lisbon'], "answer": "Paris"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ['Harper Lee', 'Mark Twain', 'J.K. Rowling', 'Stephen King'], "answer": "Harper Lee"},
        {"question": "Fill in the blank: The inventor of the telephone was Alexander Graham ____.", "options": ['Bell', 'Edison', 'Tesla', 'Jobs'], "answer": "Bell"},
        {"question": "What is the smallest planet in our solar system?", "options": ['Mercury', 'Mars', 'Venus', 'Earth'], "answer": "Mercury"},
    ]

def display_question(question):
    print(question["question"])
    for idx, option in enumerate(question["options"], 1):
        print(f"{idx}. {option}")
    user_answer = input("Enter your answer: ")
    return user_answer

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def play_game(questions):
    score = 0
    for question in questions:
        user_answer = display_question(question)
        if check_answer(user_answer, question["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question['answer']}.")
        print()
    return score

def main():
    welcome_message()
    questions = load_questions()
    score = play_game(questions)
    print(f"Game Over! Your final score is {score} out of {len(questions)}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing. Goodbye!")
        sys.exit()

if __name__ == "__main__":
    main()
