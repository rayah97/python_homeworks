import random

questions = [
    'What is the capital of France?', 
    'What is the largest planet in our solar system?', 
    'What is the currency of Japan?', 
    'Who painted the Mona Lisa?', 
    'What is the highest mountain in the world?', 
    'Which river flows through London?',
    'What is the largest mammal in the world?',
    'Who wrote the novel "Pride and Prejudice"?',
    'Which country is the Great Wall of China located in?',
    'What is the capital of Australia?',
    'Who won the first FIFA World Cup?',
    'Which US president was in office during World War II?',
    'What is the capital of Egypt?',
    'What is the smallest country in the world?',
    'What is the name of the famous clock tower in London?',
    'Which planet is known as the "Red Planet"?',
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

answers = {
    'What is the capital of France?': ['A) London', 'B) Paris', 'C) Berlin', 'D) Rome'],
    'What is the largest planet in our solar system?': ['A) Jupiter', 'B) Earth', 'C) Mars', 'D) Saturn'],
    'What is the currency of Japan?': ['A) Yen', 'B) Dollar', 'C) Euro', 'D) Peso'],
    'Who painted the Mona Lisa?': ['A) Raphael', 'B) Michelangelo', 'C) Leonardo da Vinci', 'D) Frida Kahlo'],
    'What is the highest mountain in the world?': ['A) K2', 'B) Mount Everest', 'C) Kangchenjunga', 'D) Lhotse'],
    'Which river flows through London?': ['A) Thames', 'B) Seine', 'C) Rhine', 'D) Danube'],
    'What is the largest mammal in the world?': ['A) Blue Whale', 'B) Elephant', 'C) Giraffe', 'D) Hippopotamus'],
    'Who wrote the novel "Pride and Prejudice"?': ['A) George Orwell', 'B) Charles Dickens', 'C) Jane Austen', 'D) F. Scott Fitzgerald'],
    'Which country is the Great Wall of China located in?' : ['A) China', 'B) Japan', 'C) India', 'D) Korea'],
    'What is the capital of Australia?' : ['A) Melbourne', 'B) Sydney', 'C) Canberra', 'D) Perth'],
    'Who won the first FIFA World Cup?' : ['A) Uruguay', 'B) Brazil', 'C) Argentina', 'D) Germany'],
    'Which US president was in office during World War II?' : ['A) Franklin D. Roosevelt', 'B) Harry S. Truman', 'C) Dwight D. Eisenhower', 'D) John F. Kennedy'],
    'What is the capital of Egypt?': ['A) Luxor ', 'B) Alexandria', 'C) Giza', 'D) Cairo'],
    'What is the smallest country in the world?' : ['A) Vatican City', 'B) Monaco', 'C) San Marino', 'D) Liechtenstein'],
    'What is the name of the famous clock tower in London?': ['A) Tower Bridge', 'B) Time Square', 'C) London Eye', 'D) Big Ben'],
    'Which planet is known as the "Red Planet"?' : ['A) Venus', 'B) Mars', 'C) Saturn', 'D) Jupiter']

}

asked_questions = []
correct_count = 0

while questions and len(asked_questions) < 10:
    question = random.choice(questions)
    if question in asked_questions:
        continue
    asked_questions.append(question)
    print(question)
    for answer in answers[question]:
        print("   ",answer)
    user_answer = input("Enter the letter of your answer: ")

    if user_answer.capitalize() == correct_answers[question]:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect.")
    questions.remove(question)

print(f"You got {correct_count} out of {len(correct_answers)} questions correct.")
