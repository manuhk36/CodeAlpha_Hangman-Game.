import random

# List of possible words
word_list = ["python", "hangman", "challenge", "programming", "developer"]
word = random.choice(word_list).lower()

# Create display word with underscores matching the word length
display_word = ["_"] * len(word)

# Variables to track guesses
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# DEBUG: print the chosen word (remove/comment in production)
print(f"(Debug) The word to guess is: {word}")

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(display_word))

while wrong_guesses < max_wrong_guesses and "_" in display_word:
    guess = input("\nEnter a letter: ").strip().lower()

    # Input validation: single alphabetic character only
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter (a-z).")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong! You have {max_wrong_guesses - wrong_guesses} tries left.")

    print("\nWord: " + " ".join(display_word))
    print("Guessed letters: " + ", ".join(guessed_letters))

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
