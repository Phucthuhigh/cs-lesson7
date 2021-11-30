import math


def is_prime(n):
    if (n < 2):
        return False
    if (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if (n % i == 0):
            return False
    return True


n = int(input("Input number: "))
if (is_prime(n)):
    print(f"{n} is a prime")
else:
    print(f"{n} is not a prime")
