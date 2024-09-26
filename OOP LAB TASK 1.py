import math
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def check_prime_numbers(numbers):
    for num in numbers:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
numbers_to_check = [12, 13, 33, 44, 97, 100]
check_prime_numbers(numbers_to_check)
