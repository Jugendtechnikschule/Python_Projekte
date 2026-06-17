zäler = 0


while True:
    zäler = zäler + 1
    if zäler % 2 == 0 and zäler % 3 == 0:
        print("FizzBuzz")
    elif zäler % 2 == 0:
        print("Fizz")
    elif zäler % 3 == 0:
        print("Buzz")
    else:
        print(zäler)