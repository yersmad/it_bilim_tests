name1 = input()
name2 = input()
a = 0
b = 0
vowels = ["a", "e", "i", "o", "u"]
for c in name1:
    # if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
    if c in vowels:
        a += 1
for d in name2:
    # if d == "a" or d == "e" or d == "i" or d == "o" or d == "u":
    if d in vowels:
        b += 1
if a > b:
    print(name1)
else:
    print(name2)
