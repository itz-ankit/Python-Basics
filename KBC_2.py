questions = [
    {
        "question": "WHICH IS THE LARGEST PLANET IN OUR SOLAR SYSTEM?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "WHICH IS THE CAPITAL CITY OF AUSTRALIA?",
        "options": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Perth"],
        "correct_answer": "B"
    },
    {
        "question": "WHO PAINTED THE MONA LISA?",
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
        "correct_answer": "A"
    }
]

total_questions = len(questions)
current_question = 1
total_won = 0

print("Welcome to KBC Quiz Game!")
print("You will be asked a series of questions. Answer each question correctly to win more money.")
print("Let's begin!")

for question in questions:
    print(f"\nQuestion {current_question}/{total_questions}:")
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ")
    
    if answer.upper() == question["correct_answer"]:
        total_won = total_won + 10000
        print("Correct answer! You won ₹10,000.")    
    else:
        print("Sorry, that is incorrect. Better luck next time!")
        break
    
    current_question += 1
    
print("\nCongratulations! You have completed the quiz.")
print(f"You are taking home a total of ₹{total_won}.")