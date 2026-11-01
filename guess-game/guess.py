# A number guessing game.
# The computer picks a secret number, and the player keeps guessing
# until they find it, with "too high" / "too low" hints along the way.

# "import" loads extra tools that come with Python.
# The random module lets us pick random numbers.
import random

# Store the range in variables so it's easy to change later in one place.
LOWEST = 1
HIGHEST = 100

# randint picks a random whole number between LOWEST and HIGHEST (both included).
secret_number = random.randint(LOWEST, HIGHEST)

# Count how many guesses the player makes.
attempts = 0

print("Welcome to the Guessing Game!")
print(f"I'm thinking of a number between {LOWEST} and {HIGHEST}.")

# "while True" repeats the indented code forever,
# until we stop it with "break" (when the player guesses correctly).
while True:
    # input() waits for the player to type something and press Enter.
    # Whatever they type comes back as text (a "string"), not a number.
    guess_text = input("Your guess: ")

    # int() turns text like "42" into the number 42.
    # If the player types something that isn't a number (like "abc"),
    # int() raises an error. "try/except" catches that error so the game
    # doesn't crash, and we ask again instead.
    try:
        guess = int(guess_text)
    except ValueError:
        print("That's not a number. Please type a whole number.")
        continue  # skip the rest of the loop and go back to the top

    # Reject numbers outside the range, but don't count them as attempts.
    if guess < LOWEST or guess > HIGHEST:
        print(f"Please pick a number between {LOWEST} and {HIGHEST}.")
        continue

    attempts = attempts + 1

    # Compare the guess to the secret number and give a hint.
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You got it in {attempts} attempts.")
        break  # exit the while loop, which ends the game
