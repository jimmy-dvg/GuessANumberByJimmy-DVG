import random

high_score = 0

while True:
    print("Choose difficulty: easy, medium, hard")
    difficulty = input("Enter difficulty: ").lower()

    if difficulty == "easy":
        max_number = 20
        max_attempts = None
        base_score = 50
    elif difficulty == "medium":
        max_number = 50
        max_attempts = 10
        base_score = 100
    else:  # hard
        max_number = 100
        max_attempts = 7
        base_score = 200

    secret_number = random.randint(1, max_number)
    attempts = 0
    score = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess < 1 or guess > max_number:
            print(f"Invalid input! Please enter a number between 1 and {max_number}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            score = base_score - (attempts - 1) * 5
            if score < 0:
                score = 0
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            print(f"Your score: {score} points")

            if score > high_score:
                high_score = score
                print("🏆 New High Score!")
            else:
                print(f"High Score remains: {high_score} points")
            break

        if max_attempts and attempts >= max_attempts:
            print(f"Out of attempts! The number was {secret_number}.")
            print("Your score: 0 points")
            print(f"High Score remains: {high_score} points")
            break