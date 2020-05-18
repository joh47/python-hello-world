from random import randrange

text = input("Guess a number from 1 to 10. \n")

if(not text.isdigit()):
    print("You did not enter a digit.")
    exit()
elif(not int(text) >= 1):
    print ("Your digit was not at least 1.")
    exit()
elif(not (int(text) <= 10)):
    print ("Your digit was not smaller than 10.")
    exit()
else:
    print("That was a digit between 1 and 10")

print("Your guess is " + text)

random_number = randrange(10) + 1

print("My guess was " + str(random_number))

if(random_number == int(text)):
    print("Hey rockstar! You got it!")
else:
    print("Oops - better luck next time!")
