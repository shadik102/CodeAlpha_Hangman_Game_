import random

# List of words
words = ["python", "apple", "orange", "laptop", "camera"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_wrong:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")
        print("Remaining chances:", max_wrong - wrong_guesses)

else:
    print("\nGame Over!")
    print("The correct word was:", word)