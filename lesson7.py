# def leap_year(year):
#     if (year % 4 == 0):
#         return True
#     elif (year % 100 == 0 and year % 400 == 0):
#         return True
#     return False


# if leap_year(int(input("Nhap vo nam di😍😍: "))):
#     print("Day la nam nhuan nha mn 😘😘")
# else:
#     print("Day khong phai nam nhuan dau 🤧🤧")

# def sinh(a, n):
#     a[n-1] += 1
#     i = n-1
#     while i >= 0:
#         if (a[i] > 1):
#             a[i - 1] += 1
#             a[i] -= 2
#         i -= 1


# n = int(input())
# a = [0] * n
# for i in range(2**n):
#     print(a)
#     sinh(a, n)

# def oddeven(n):
#     if (n == 0):
#         return 0
#     elif (n % 2 == 0):
#         return 1
#     elif (n % 2 != 0):
#         return 2


# n = int(input())
# if oddeven(n) == 1:
#     print("La so chan")
# elif oddeven(n) == 2:
#     print("La so le")
# else:
#     print("La so 0")

# def tong(a, n):
#     s = 0
#     for i in range(n):
#         try:
#             tmp = int(a[i])
#             s += tmp
#         except:
#             try:
#                 tmp = float(a[i])
#                 s += tmp
#             except:
#                 continue
#     return s


# a = [1, 2, 3, 4, 'a', '5', '3.14']
# n = len(a)

# print(tong(a, n))

# def sort(n):
#     lst = list(n)
#     for i in range(len(lst)-1):
#         for j in range(i+1, len(lst)):
#             if (ord(lst[i]) > ord(lst[j])):
#                 lst[i], lst[j] = lst[j], lst[i]
#     return ",".join(lst)


# n = input()
# print(sort(n))

# def is_int(n):
#     tmp = int(n)
#     return n == tmp


# n = float(input("Input number: "))
# if (is_int(n)):
#     print(f"{n} is an integer")
# else:
#     print(f"{n} is not an integer")

# import math

# def is_prime(n):
#     if (n < 2):
#         return False
#     if (n % 2 == 0 and n != 2):
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if (n % i == 0):
#             return False
#     return True


# n = int(input("Input number: "))
# if (is_prime(n)):
#     print(f"{n} is a prime")
# else:
#     print(f"{n} is not a prime")


# import math

# def is_prime(n):
#     if (n < 2):
#         return False
#     if (n % 2 == 0 and n != 2):
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if (n % i == 0):
#             return False
#     return True


# i = 2
# d = 0
# n = int(input("Input number: "))
# print(f"First {n} prime(s):", end=" ")
# while d < n:
#     if (is_prime(i)):
#         print(i, end=" ")
#         d += 1
#     i += 1

# def giaithua(n):
#     if (n == 1 or n == 0):
#         return 1
#     return n * giaithua(n-1)


# def bieuthucdacbiet(n):
#     return giaithua(n)/n


# n = int(input("Input number: "))

# s = 0
# for i in range(1, n+1):
#     s += bieuthucdacbiet(i)

# print(f"Result: {s}")


# from datetime import datetime
# now = datetime.now()
# print(f"Today is {now.strftime('%d/%m/%Y')}")
# print(f"Time right now {now.strftime('%H:%M:%S')}")
