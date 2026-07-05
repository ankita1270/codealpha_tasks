import random

words = ["python", "computer", "coding", "program", "internship"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)