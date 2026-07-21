from player import player_choose_number, player_turn
from ai import ai_choose_number, ai_turn


def start_game():
    player_secret_number = player_choose_number()
    ai_secret_number = ai_choose_number()

    low = 1
    high = 100
    used_guesses = set()

    round_number = 1

    while True:

        print("\n" + "=" * 40)
        print(f"ROUND {round_number}")
        print("=" * 40)

        # Player's Turn
        player_won = player_turn(ai_secret_number)

        if player_won:
            print("\n🏆 PLAYER WINS!")
            break

        # AI's Turn
        ai_won, low, high = ai_turn(low, high, used_guesses)

        if ai_won:
            print("\n🤖 AI WINS!")
            break

        round_number += 1