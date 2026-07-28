def player_choose_number():
    while True:
        try:
            number = int(input("Choose your secret number (1-100): "))
            if 1 <= number <= 100:
                return number
        except:
            pass

        print("Invalid input.")


def player_turn(ai_secret_number):

    while True:
        try:
            guess = int(input("Your guess: "))
            break
        except:
            print("Enter a valid number.")

    if guess < ai_secret_number:
        print("⬆️ Higher")
        return False

    elif guess > ai_secret_number:
        print("⬇️ Lower")
        return False

    else:
        print("🎉 Correct!")
        return True