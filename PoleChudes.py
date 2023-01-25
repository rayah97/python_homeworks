selected_country = "France"
selected_capital = "Paris"
hidden_capital = "*" * len(selected_capital)

while "*" in hidden_capital:
    letter = input("Guess a letter in the capital of " + selected_country + ": ").lower()

    if letter in selected_capital.lower():
        for i in range(len(selected_capital)):
            if selected_capital[i].lower() == letter and hidden_capital[i] == "*":
                hidden_capital = hidden_capital[:i] + selected_capital[i] + hidden_capital[i+1:]
        print("Correct! The word is now: " + hidden_capital)
    else:
        print("Incorrect.")

print("Congratulations! The capital of " + selected_country + " is " + selected_capital + ".")
