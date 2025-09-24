n = int(input())

names = []


for i in range(n):
    names.append(input())

for name in names:
    count_b = name.lower().count("b")
    count_g = name.lower().count("g")
    if count_b > count_g:
        print(f"{name} is A BADDY")
    elif count_g > count_b:
        print(f"{name} is GOOD")
    else:
        print(f"{name} is NEUTRAL")
