def is_int(n):
    tmp = int(n)
    return n == tmp


n = float(input("Input number: "))
if (is_int(n)):
    print(f"{n} is an integer")
else:
    print(f"{n} is not an integer")
