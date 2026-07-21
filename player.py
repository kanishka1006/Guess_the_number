def player_choose_number():
    while True:
        player_number = int(input("Enter your secret number (1-100): "))

        if 1 <= player_number <= 100:
            return player_number
        else:
            print("Invalid input! Please enter a number between 1 and 100.")


def player_turn(ai_secret_number):
    while True:
        try:
            guess = int(input("\nGuess the AI's number (1-100): "))
            if 1 <= guess <= 100:
                break

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")
    
    
    if guess < ai_secret_number:
        print("🤖 AI says: Higher")
        return False
    elif guess > ai_secret_number:
        print("🤖 AI says: Lower")
        return False
    else:
        print("\n🎉 You guessed the AI's number!")
        return True