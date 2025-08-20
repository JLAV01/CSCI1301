import random

print("welcome to yatzee")

#First Roll
input("Press enter to roll 5 dice")
die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
die4 = random.randint(1,6)
die5 = random.randint(1,6)
print("first roll", die1, die2, die3, die4, die5)

#First Reroll
reroll = input("Enter dice numbers to reroll or hit enter to accept results")

die1 = ("1" in reroll) * random.randint(1,6) + ("1" not in reroll) * die1
die2 = ("2" in reroll) * random.randint(1,6) + ("1" not in reroll) * die2
die3 = ("3" in reroll) * random.randint(1,6) + ("1" not in reroll) * die3
die4 = ("4" in reroll) * random.randint(1,6) + ("1" not in reroll) * die4
die5 = ("5" in reroll) * random.randint(1,6) + ("1" not in reroll) * die5

print("second roll:", die1, die2, die3, die4, die5)

reroll = input("Enter dice numbers to reroll or hit enter to accept results")

die1 = ("1" in reroll) * random.randint(1,6) + ("1" not in reroll) * die1
die2 = ("2" in reroll) * random.randint(1,6) + ("1" not in reroll) * die2
die3 = ("3" in reroll) * random.randint(1,6) + ("1" not in reroll) * die3
die4 = ("4" in reroll) * random.randint(1,6) + ("1" not in reroll) * die4
die5 = ("5" in reroll) * random.randint(1,6) + ("1" not in reroll) * die5

print("third roll:", die1, die2, die3, die4, die5)

print("dice total:", die1 + die2 + die3 + die4 + die5)
