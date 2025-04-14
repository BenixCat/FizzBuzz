# FizzBuzz
for fzbz in range(1, 101,1):
# If the number is divisible by 3 and 5, print FizzBuzz
    if fzbz % 3 == 0 and fzbz % 5 == 0:
        print("FizzBuzz")
    # If the number is divisible by 5, print Fizz
    elif fzbz % 5 == 0:
        print("Buzz")
    # If the number is divisible by 3, print Buzz
    elif fzbz % 3 == 0:
        print("Fizz")
    # If the number is not divisible by 3 or 5, print the number
    else:
        print(fzbz)