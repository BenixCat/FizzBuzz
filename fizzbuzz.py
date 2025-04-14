for fzbz in range(1, 101,1):
    if fzbz % 3 == 0 and fzbz % 5 == 0:
        print("FizzBuzz")
    elif fzbz % 5 == 0:
        print("Buzz")
    elif fzbz % 3 == 0:
        print("Fizz")
    else:
        print(fzbz)