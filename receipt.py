X = int(input())
N = int(input())

a_list = []
b_list = []
for i in range(N):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)


item = sum([x * y for x, y in zip(a_list, b_list)])
if item == X:
    print("Yes")
else:
    print("No")
