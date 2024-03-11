# simple quiz game

questions = [
    {
        "question": "What is the capital of France?",
        "answers": ['A) Paris', 'B) London', 'C) Berlin', 'D) Rome'],
        "correct": "A"
    },
    {
        "question": "What is the capital of Germany?",
        "answers": ['A) Paris', 'B) London', 'C) Berlin', 'D) Rome'],
        "correct": "C"
    },
    {
        "question": "What is the capital of Italy?",
        "answers": ['A) Paris', 'B) London', 'C) Berlin', 'D) Rome'],
        "correct": "D"
    },
    {
        "question": "What is the capital of England?",
        "answers": ['A) Paris', 'B) London', 'C) Berlin', 'D) Rome'],
        "correct": "B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for answer in question["answers"]:
            print(answer)
        user_answer = input("Enter A, B, C or D: ")
        if user_answer == question["correct"]:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
    
    
if __name__ == "__main__":
    run_quiz(questions)