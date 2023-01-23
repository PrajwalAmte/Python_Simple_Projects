# Dice roll simulator
import random
while True:
    print("1.Roll the dice \n2.Exit")
    user = int(input("What You want to do: "))
    if user == 1:
        number = random.randint(0, 6)
        print("Number = "+str(number)+"\n")
    else:
        break