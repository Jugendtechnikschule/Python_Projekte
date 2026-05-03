import random

while True:
    x = random.randint(1, 10)
    print(x)

    user_input = input("Was ist die Random Zahl: ")
    print(user_input)

    y += 2

    if int(user_input) == x:
        print("Richtig!")
    else:
        print("Falsch!")