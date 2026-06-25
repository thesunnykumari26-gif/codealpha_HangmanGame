import random

# Predefined words
words = ["python", "coding", "laptop", "gaming", "project"]

# Select random word
word = random.choice(words)

# Create hidden word
guessed_word = ["_"] * len(word)

# Game settings
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game")
print("Guess the word one letter at a time.")
print(f"You have {attempts} attempts.\n")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validationc
    c
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in word:
        print("✅ Correct Guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong Guess!\n")

# Result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)