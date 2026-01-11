import random
word__bank = ("apple", "banana", "cherry", "date", "elderberry")
word = random.choice(word__bank)

guessedword =["_"] * len(word)
attempts = 10
while attempts > 0 and "_" in guessedword:
    print("Current word: " + " ".join(guessedword))
    print(f"Attempts remaining: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                guessedword[index] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        attempts -= 1
        print(f"Sorry, '{guess}' is not in the word.")
