def delete_typo(index, word:str) -> str:
    return word[:index -1] + word[index:]

T = int(input())

typos_list = []

for _ in range(T):
    idx, s = input().split()
    typos_list.append((int(idx), s))

for idx, s in typos_list:
    print(delete_typo(idx, s))
