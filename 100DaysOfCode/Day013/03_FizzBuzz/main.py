# 3. debugging exercise

if __name__ == "__main__":
    for number in range(1, 101):
        # if number % 3 == 0 or number % 5 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            # print([number])
            print(number)
