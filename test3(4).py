a, b, c = int(input()), int(input()), int(input())
if a >= b >= c or a >= c >= b:
    print(a)
elif b >= a >= c or b >= c >= a:
    print(b)
else:
    print(c)
