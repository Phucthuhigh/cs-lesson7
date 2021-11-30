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


i = 2
d = 0
n = int(input("Input number: "))
print(f"First {n} prime(s):", end=" ")
while d < n:
    if (is_prime(i)):
        print(i, end=" ")
        d += 1
    i += 1
