def giaithua(n):
    if (n == 1 or n == 0):
        return 1
    return n * giaithua(n-1)


def bieuthucdacbiet(n):
    return giaithua(n)/n


n = int(input("Input number: "))

s = 0
for i in range(1, n+1):
    s += bieuthucdacbiet(i)

print(f"Result: {s}")
