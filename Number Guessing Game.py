import random
print("Welcome to number guessing game.\n")
print("Press Enter to Continue... ")
start = input()
first_number = int(input("Choose First Number: "))
second_number = int(input("Choose Second Number: "))
right_number = random.randint(first_number, second_number)

print("I've picked a number for you to guess.")
print(f"The number is between {first_number} and {second_number}.\n")
count = 0
while True:
    count += 1
    guessed_number = int(input("Guess a number: "))
    if guessed_number == right_number:
        print("\nCorrect guess.")
        print("You won. Thank you for playing.")

        break

    if guessed_number < first_number or guessed_number > second_number:
        print(
            f"Invalid guess. Please enter a number between {first_number} and {second_number}.")

    elif guessed_number > right_number:
        print("\nYour guess is not correct.")
        print("Give it another shot.")
        print("Choose a lower number\n.")
    elif guessed_number < right_number:
        print("\nYour guess is not correct.")
        print("Give it another shot.")
        print("Choose a higher number\n.")
print(f"Number of Guesses: {count}")
