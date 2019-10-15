import random
min = 1
max = 6

# roll_dice_permission =
roll_again = input("Do you want to roll the dice?")

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = input("Roll the dices again?")
