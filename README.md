# Hangman Game Project

## Project Title
Hangman Game

## Description
The Hangman Game is a simple command-line Python project based on the classic word guessing game. In this game, the computer randomly selects a word from a predefined list, and the player has to guess the word one letter at a time within a limited number of attempts. The game provides hints by displaying correctly guessed letters in their correct positions while hiding the remaining letters with underscores.

This project is beginner-friendly and helps in understanding important Python concepts such as loops, conditional statements, lists, strings, and user input handling.

## Features
- Interactive command-line gameplay
- Random word selection from predefined words
- Maximum of 6 incorrect attempts allowed
- Tracks guessed letters
- Displays current progress after every guess
- Input validation for better user experience
- Winning and losing messages
- Beginner-friendly Python project

## Technologies Used
- Python 3.x

## Predefined Words
The game uses the following predefined words:
- python
- coding
- laptop
- gaming
- project

## How to Run

1. Install Python from the official website: https://www.python.org/

2. Create a file named `hangman.py`

3. Copy and paste the Python code into the file.

4. Open terminal or command prompt in the project folder.

5. Run the program using:
```bash
python hangman.py
```

## Python Code

```python
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

    # Validation
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
```

## Sample Output

```text
🎮 Welcome to Hangman Game
Guess the word one letter at a time.
You have 6 attempts.

Word: _ _ _ _ _ _
Guessed Letters:
Attempts Left: 6

Enter a letter: p
✅ Correct Guess!

Word: p _ _ _ _ _
Guessed Letters: p
Attempts Left: 6
```

## Learning Outcomes
By building this project, you can learn:
- Python basics
- Loops and conditions
- Lists and strings
- Random module usage
- Input validation
- Problem-solving skills

## Author
Sunny Kumari
