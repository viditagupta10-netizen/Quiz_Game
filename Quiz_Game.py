import random

def quiz_game():
    # Quiz questions with options and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "correct": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Jupiter", "B) Mars", "C) Venus", "D) Mercury"],
            "correct": "B"
        },
        {
            "question": "What is 15 * 4?",
            "options": ["A) 45", "B) 60", "C) 75", "D) 90"],
            "correct": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
            "correct": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "correct": "D"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
            "correct": "C"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Ag", "B) Au", "C) Fe", "D) Cu"],
            "correct": "B"
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "correct": "B"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["A) Elephant", "B) Lion", "C) Tiger", "D) Gorilla"],
            "correct": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "correct": "C"
        },
        {
            "question": "Which programming language is Python named after?",
            "options": ["A) Monty Python", "B) Python Snake", "C) Python Programming", "D) Python Games"],
            "correct": "A"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A) Tomato", "B) Onion", "C) Avocado", "D) Pepper"],
            "correct": "C"
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("🎉 Welcome to the General Knowledge Quiz! 🎉")
    print("Answer 12 questions by typing A, B, C, or D")
    print("-" * 50)
    
    # Shuffle questions for variety
    random.shuffle(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D only!")
        
        if answer == q['correct']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['correct']}")
    
    # Results
    print("\n" + "="*50)
    print("📊 QUIZ RESULTS 📊")
    print("="*50)
    print(f"Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    
    if percentage >= 90:
        print("🏆 Excellent! You're a genius! 🏆")
    elif percentage >= 70:
        print("👍 Great job! Well done! 👍")
    elif percentage >= 50:
        print("👌 Good effort! Keep learning! 👌")
    else:
        print("📚 Keep studying! You'll get better! 📚")
    
    print(f"Percentage: {percentage:.1f}%")

# Run the quiz
if __name__ == "__main__":
    quiz_game()
    
    # Ask if user wants to play again
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            print("\n" + "~"*50 + "\n")
            quiz_game()
        else:
            print("Thanks for playing! 👋")
            break