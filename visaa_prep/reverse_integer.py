def reverse_integer(n):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    reversed_n = int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
    return reversed_n if INT_MIN <= reversed_n <= INT_MAX else 0
n=int(input())
print(reverse_integer(n))
