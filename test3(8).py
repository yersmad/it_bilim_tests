n = int(input())
a1 = (n // 10) % 10
a2 = (n // 100) % 10
a3 = (n // 1000) % 10
b1 = (n // 10000) % 10
b2 = (n // 100000) % 10
b3 = n % 10
if a1 + a2 + a3 == b1 + b2 + b3:
    print("True")
else:
    print("False")
