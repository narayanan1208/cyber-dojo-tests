def print_multiples_of_number_in_string():
    first_digit, last_digit = 1, 100
    for i in range(first_digit, last_digit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":  # pragma: no cover
    print_multiples_of_number_in_string()
