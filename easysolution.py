A, B = map(int, input().split())
number_list = []

i = 1
while len(number_list) < B:
    for _ in range(i):
        number_list.append(i)
        if len(number_list) >= B:
            break
    i +=1

start_index = A - 1
end_index = B
selected_numbers = number_list[start_index:end_index]
total = sum(selected_numbers)

print(total)



