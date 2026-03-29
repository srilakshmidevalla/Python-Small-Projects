# project_01_number_guessing.py
# Mini Project 1: Number Guessing Game
# Run: python 06_mini_projects/project_01_number_guessing.py

import random

def play_game():
    print("=" * 40)
    print("   🎮 NUMBER GUESSING GAME")
    print("=" * 40)

    # Choose difficulty
    print("\nDifficulty:")
    print("  1 → Easy   (1-50,  10 guesses)")
    print("  2 → Medium (1-100,  7 guesses)")
    print("  3 → Hard   (1-500,  5 guesses)")

    choice = input("\nChoose difficulty (1/2/3): ")

    if choice == "1":
        max_num, max_guesses = 50, 10
    elif choice == "3":
        max_num, max_guesses = 500, 5
    else:
        max_num, max_guesses = 100, 7

    secret = random.randint(1, max_num)
    attempts = 0
    won = False

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_guesses} guesses. Good luck!\n")

    while attempts < max_guesses:
        remaining = max_guesses - attempts
        try:
            guess = int(input(f"Guess #{attempts + 1} ({remaining} left): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret:
            won = True
            break
        elif guess < secret:
            gap = secret - guess
            if gap > 20:
                print("📉 Way too low!")
            else:
                print("⬆️  A bit low...")
        else:
            gap = guess - secret
            if gap > 20:
                print("📈 Way too high!")
            else:
                print("⬇️  A bit high...")

    print()
    if won:
        print(f"🎉 Correct! The number was {secret}.")
        print(f"You got it in {attempts} guess{'es' if attempts > 1 else ''}!")
        if attempts <= max_guesses // 2:
            print("⭐ Amazing performance!")
    else:
        print(f"😢 Game over! The number was {secret}.")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing! 🐍")

# Entry point
if __name__ == "__main__":
    play_game()
