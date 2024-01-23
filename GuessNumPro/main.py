'''
2. Guess the number 
'''
import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number from 1 to {x}: "))
        if guess > random_number:
            print(f"Hint: Lower than {guess}")
        elif guess < random_number:
            print(f"Hint: Higher than {guess}")

    print(f"Yay, congrats. You have guessed the correct number {guess}!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess} correctly!")

computer_guess(10)

