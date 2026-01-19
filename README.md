# 🎮 Guess the Number Game (Python)

## 📖 Description
This is a simple **Guess the Number** game written in Python.  
The computer randomly selects a number, and the player tries to guess it.  
Hints are given if the guess is too high or too low, and the game continues until the player guesses correctly or runs out of attempts.

## ✨ Features
- Difficulty levels:
  - **Easy** → Range 1–20, unlimited attempts
  - **Medium** → Range 1–50, 10 attempts
  - **Hard** → Range 1–100, 7 attempts
- Scoring system:
  - Base score depends on difficulty
  - Points decrease with each wrong attempt
  - Minimum score is 0
- High score tracking across multiple rounds
- Error handling for invalid input (e.g., typing letters instead of numbers)
- Option to play again without restarting the program

## 🚀 How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Save the game code in a file, e.g., `guess_number.py`.
3. Run the program in your terminal or IDE:
   ```bash
   python guess_number.py
   
## 🎯Example Gameplay
   Choose difficulty: easy, medium, hard
Enter difficulty: hard
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 63
🎉 Correct! You guessed it in 3 tries.
Your score: 185 points
🏆 New High Score!
Do you want to play again? (yes/no): no
Thanks for playing! Your final high score was 185 points 👋

