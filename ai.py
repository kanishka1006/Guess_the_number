import random
def ai_choose_number():
    ai_number = random.randint(1,100)
    return ai_number



def ai_turn(low, high, used_guesses):
    if low > high:
        print("Something went wrong! Please check your responses.")
        return False, low, high
    
    ai_guess = (low + high) // 2


    used_guesses.add(ai_guess)

    print(f"\n🤖 AI guesses: {ai_guess}")

    
    while True:
        response = input("Player (higher/lower/correct): ").lower()
        
        if response in ["higher", "lower", "correct"]:
            break

        print("Invalid response! Please enter higher, lower, or correct.")
    if response == "higher":
        low = ai_guess + 1
        return False, low, high

    elif response == "lower":
        high = ai_guess - 1
        return False, low, high
    elif response == "correct":
        print("\n🤖 AI guessed your number!")
        return True, low, high
    return False,low, high