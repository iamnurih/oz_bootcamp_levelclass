def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])

### reverse 하지 않고 .pop()을 활용해서 해도 됨 

N=int(input())
cases = []
for i in range(N):
    cases.append(reverse_words(input()))

for idx, result in enumerate(cases):
    print(f"Case #{idx +1}: {result}")