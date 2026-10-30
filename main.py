import random
from collections import Counter
import re


# Number Guessing Game
def guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Guess a number between 1 and 100")
    print("You have 7 attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                score = (max_attempts - attempts + 1) * 10

                print("\nCongratulations! You won!")
                print("Attempts used:", attempts)
                print("Your score:", score)
                return

            elif guess < secret_number:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

            print("Attempts remaining:", max_attempts - attempts)

        except ValueError:
            print("Invalid input! Enter a valid number.")

    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Your score: 0")


# Word Counter
def word_counter():
    print("\n===== WORD COUNTER =====")

    filename = input("Enter text filename (e.g. sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r"\b\w+\b", text.lower())

        total_words = len(words)
        frequency = Counter(words)

        print("\nTotal Words:", total_words)
        print("Unique Words:", len(frequency))

        print("\nTop 10 Most Common Words:")

        for word, count in frequency.most_common(10):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found!")

    except OSError as error:
        print("File error:", error)


# Main Menu
def main():
    while True:
        print("\n================================")
        print(" NUMBER GUESSING & WORD COUNTER")
        print("================================")

        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()