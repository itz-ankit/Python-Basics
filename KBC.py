def play_kbc():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
            "answer": "A"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
            "answer": "C"
        }
    ]

    total_questions = len(questions)
    current_question = 0
    money = 0

    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win big!")

    while current_question < total_questions:
        question = questions[current_question]
        print("\nQuestion", current_question + 1, ":")
        print(question["question"])
        for option in question["options"]:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ")

        if user_answer.upper() == question["answer"]:
            print("Correct answer!")
            money += 10000
            current_question += 1
        else:
            print("Oops, wrong answer!")
            break

    print("\nCongratulations! You answered all the questions correctly!")

    print("You are taking home a whopping", money, "rupees!")

play_kbc()