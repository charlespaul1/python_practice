import random
numbers = [1,2,3,4,5,6,7,8,9,10]
number_of_guess  = 0
name = input("what is your name: ")
while number_of_guess < 3:
    
    guess = input(f"ok {name}, im guessing a number between 1 and 10, take a guess which number it is:  ")
    # changing input to int
    guess = int(guess)
    #  selecting a random number
    the_number  = random.choice(numbers)
    number_of_guess += 1

    if (guess > the_number):
        print(f"Guess is too high, try again, the number is {the_number}")
    elif (guess < the_number):
        print(f"Guess is too low , try again, the number is  {the_number}")
    else:
        print(f"You got it, your guess was {guess} and my number is {the_number} ")
        break
