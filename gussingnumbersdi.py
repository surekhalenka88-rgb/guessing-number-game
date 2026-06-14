import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Enter Your Guess: "))

    if secret_number == guess:
        print("Hey! Congrats, you guessed the number 🎉")
        break
    elif guess < secret_number:
        print("Too Low ")
    else:
        print("Too High ")