import random

secret_number = random.randint(1, 100)

#choosing difficulty level
difficulty = input("Choose difficulty level (easy, medium, hard): ")

if difficulty == "easy":
    maximum_guesses = 10
elif difficulty == "medium":
    maximum_guesses = 7
else:
    maximum_guesses = 5

attempts = 0
correct_guess = False

while not correct_guess and attempts < maximum_guesses:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < secret_number:
       print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"You guessed it right! It took you {attempts} attempts.")
        correct_guess = True

    if not correct_guess:
        remaining_attempts = maximum_guesses - attempts
        print(f"You have {remaining_attempts} attempts left.")
    
if not correct_guess:
    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")



