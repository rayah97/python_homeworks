import random

questions = [
    {'question': 'What is the capital of France?', 'answers': ['A) London', 'B) Paris', 'C) Berlin', 'D) Rome']},
    {'question': 'What is the largest planet in our solar system?', 'answers': ['A) Jupiter', 'B) Earth', 'C) Mars', 'D) Saturn']},
    {'question': 'What is the currency of Japan?', 'answers': ['A) Yen', 'B) Dollar', 'C) Euro', 'D) Peso']},
    {'question': 'Who painted the Mona Lisa?', 'answers': ['A) Raphael', 'B) Michelangelo', 'C) Leonardo da Vinci', 'D) Frida Kahlo']},
    {'question': 'What is the highest mountain in the world?', 'answers': ['A) K2', 'B) Mount Everest', 'C) Kangchenjunga', 'D) Lhotse']},
    {'question': 'Which river flows through London?', 'answers': ['A) Thames', 'B) Seine', 'C) Rhine', 'D) Danube']},
    {'question': 'What is the largest mammal in the world?', 'answers': ['A) Blue Whale', 'B) Elephant', 'C) Giraffe', 'D) Hippopotamus']},
    {'question': 'Who wrote the novel "Pride and Prejudice"?', 'answers': ['A) George Orwell', 'B) Charles Dickens', 'C) Jane Austen', 'D) F. Scott Fitzgerald']},
    {'question': 'Which country is the Great Wall of China located in?', 'answers': ['A) China', 'B) Japan', 'C) India', 'D) Korea']},
    {'question': 'What is the capital of Australia?', 'answers': ['A) Melbourne', 'B) Sydney', 'C) Canberra', 'D) Perth']},
    {'question': 'Who won the first FIFA World Cup?', 'answers': ['A) Uruguay', 'B) Brazil', 'C) Argentina', 'D) Germany']},
    {'question': 'Which US president was in office during World War II?', 'answers': ['A) Franklin D. Roosevelt', 'B) Harry S. Truman', 'C) Dwight D. Eisenhower', 'D) John F. Kennedy']},
    {'question': 'What is the capital of Egypt?', 'answers': ['A) Luxor ', 'B) Alexandria', 'C) Giza', 'D) Cairo']},
    {'question': 'What is the smallest country in the world?', 'answers': ['A) Vatican City', 'B) Monaco', 'C) San Marino', 'D) Liechtenstein']},
    {'question': 'What is the name of the famous clock tower in London?', 'answers': ['A) Tower Bridge', 'B) Time Square', 'C) London Eye', 'D) Big Ben']},
    {'question': 'Which planet is known as the "Red Planet"?', 'answers': ['A) Venus', 'B) Mars', 'C) Saturn', 'D) Jupiter']},
]


correct_answers = {
    'What is the capital of France?': 'B',
    'What is the largest planet in our solar system?': 'A',
    'What is the currency of Japan?': 'A',
    'Who painted the Mona Lisa?': 'C',
    'What is the highest mountain in the world?': 'B',
    'Which river flows through London?': 'A',
    'What is the largest mammal in the world?': 'A',
    'Who wrote the novel "Pride and Prejudice"?': 'C',
    'Which country is the Great Wall of China located in?': 'A',
    'What is the capital of Australia?': 'C',
    'Who won the first FIFA World Cup?': 'A',
    'Which US president was in office during World War II?': 'A',
    'What is the capital of Egypt?': 'D',
    'What is the smallest country in the world?': 'A',
    'What is the name of the famous clock tower in London?': 'D',
    'Which planet is known as the "Red Planet"?': 'B',
}


asked_questions = []
correct_count = 0

while questions:
    question = random.choice(questions)
    if question['question'] in asked_questions:
        continue
    asked_questions.append(question['question'])
    print(question['question'])
    for answer in question['answers']:
        print(answer)
    user_answer = input("Enter the letter of your answer: ")

    if user_answer.upper() == correct_answers[question['question']]:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect.")
    questions.remove(question)

print(f"You got {correct_count} out of {len(correct_answers)} questions correct.")




