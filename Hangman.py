import random

def choose_word():
    words = ["python", "apple", "banana", "grapes", "orange"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman Game!")
    print("You have 6 incorrect guesses.\n")

    while wrong_guesses < max_wrong:
        print("Word:", display_word(word, guessed_letters))
        print("Wrong guesses left:", max_wrong - wrong_guesses)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess!\n")
        else:
            print("Correct guess!\n")

        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            return

    print("Game Over! The word was:", word)

# Run the game
hangman_game()
