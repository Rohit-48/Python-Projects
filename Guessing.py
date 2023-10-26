import random
import math

#lower Bound Input
lower = int(input("Enter Lower Bound Range: "))

#Upper Bound Input 
upper= int(input("Enter Upper Bound Range: "))


#generates a random integer between 
# The Lower & Upper 
x = random.randint(lower, upper)
print("\n\tYou've only ",  
      round(math.log(upper - lower + 1, 2)),
      " chance to guess the Integers!\n")

# Initializing the number of guesses.
count = 0   


# for calculation of minimum number of
# guesses depends upon range

while count < math.log(upper - lower + 1, 2):
    count+= 1

    # for calculation of minimum number of
    # guesses depends upon range
    
    guess = int(input("Guess The Number: "))

    #Condition Testing
    if x == guess:
        print("Congralutions You Did It in ", count, " Try ")
        #Once The Guess Is Right Then Loop Will Break
        break
    elif x > guess:
        print("Try Again!, You Guess Too Small")
    elif x < guess:
        print("Try Again!, You Guees Too High")

    # If Guessing is more than required guesses,
    # shows this output.
if count > math.log(upper - lower +1, 2):
    print("\n The Number Is %d" % x)
    print("\t Better Luck Next Time!")

