import random
def guess_the_number():
    secret_number = random.randint(1, 20)
    
    print("Hello! What is your name?")
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    
    attempts = 0
    while True:
        guess = int(input("Take a guess."))
        attempts += 1
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too low")
        else:
            print(f"Good job, KBTU! You guessed my number in  {attempts} guesses!")
            break
guess_the_number()