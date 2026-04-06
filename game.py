import random
import time

random_value = random.randint(1, 48)
guesses = 9

while True:
    guess = int(input("The guess:"))
    if (guess < random_value):
        print("Information questioned")
        time.sleep(1)

        print("Enter a bigger value")
        guesses -= 1

    elif (guess > random_value):
        print("Information questioned")
        time.sleep(1)

        print("Enter a smaller value")
        guesses -= 1

    else:
        print("Information questioned")
        time.sleep(1)

        print("Congratulations, The value", random_value)
        break
    if (guesses == 0):
        print("The guesses finished")
        print("The value", random_value)
        break





    

    

