selected_country = "France"
selected_capital = "Paris"
hidden_capital = "*" * len(selected_capital)
guessed_letters = []

while "*" in hidden_capital:
    letter = input("Guess a letter in the capital of " + selected_country + ": ").lower()
    if letter in guessed_letters:
        print("You already guessed that letter.")
    elif letter in selected_capital.lower():
        hidden_capital = "".join([selected_capital[i] if selected_capital[i].lower() == letter else hidden_capital[i] for i in range(len(selected_capital))])
        print("Correct! The word is now: " + hidden_capital)
    else:
        print("Incorrect.")
    guessed_letters.append(letter)

print("Congratulations! The capital of " + selected_country + " is " + selected_capital + ".")
