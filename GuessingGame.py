import random

def validNumber(guess):
    if(not guess.isnumeric()):
        return -1
    num = int(guess)
    if(num > 100 or num < 1):
        return -1
    return num
def getInput(target, guesses):
    guess = validNumber(input("Guess a number: "))
    if(guess == -1):
        print("Error: input is not valid, please enter a number between 1-100 (inclusive):")
        return getInput(target, guesses)
    guesses += 1
    if(guess < target):
        print("Higher")
        return getInput(target, guesses)
    if(guess > target):
        print("Lower")
        return getInput(target, guesses)
    if(guess == target):
        print("Congratulations, you got it in " + str(guesses) + " tries!")

def main():
    rand = random.randint(1,100)
    getInput(rand, 0)
    
if __name__ == "__main__":
    main()
