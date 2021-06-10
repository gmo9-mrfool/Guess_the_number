import random
import logo
print(logo.logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100 ')
number= random.randint(0,100)
def play():
    difficulty=input("Choose a difficulty. Type'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        num_of_attempts =10
    elif difficulty=='hard':
        num_of_attempts=5
    while num_of_attempts!=0:
        print(f'You have {num_of_attempts} remaining to guess the number.')
        guess=int(input('Make a guess: '))
        if guess>number:
            print('Too high\nGuess again.')
            num_of_attempts-=1
        elif guess<number:
            print('Too low\nGuess again.')
            num_of_attempts-=1
        elif guess == number:
            print(f'You got it! The answer was {guess}.')
            quit()
        # elif guess==0:
    print("You've run out of guesses,you lose.")   
    quit() 
play()        
        

                    








