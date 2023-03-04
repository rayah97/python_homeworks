def get_guess(selected_country, selected_capital, hidden_capital):
    try:
        letter = input("Guess a letter in the capital of " + selected_country + ": ").lower()
        if not letter.isalpha() or len(letter) != 1:
            raise ValueError("Input must be a single letter.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return hidden_capital

    if letter in selected_capital.lower():
        for i in range(len(selected_capital)):
            if selected_capital[i].lower() == letter and hidden_capital[i] == "*":
                hidden_capital = hidden_capital[:i] + selected_capital[i] + hidden_capital[i+1:]
        print("Correct! The word is now: " + hidden_capital)
    else:
        print("Incorrect.")
    return hidden_capital

def play_game():
    selected_country = "France"
    selected_capital = "Paris"
    hidden_capital = "*" * len(selected_capital)

    try:
        while "*" in hidden_capital:
            hidden_capital = get_guess(selected_country, selected_capital, hidden_capital)
    except KeyboardInterrupt:
        print("\nGame ended by user.")
        return

    print("Congratulations! The capital of " + selected_country + " is " + selected_capital + ".")

def main():
    try:
        play_game()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
