# 문제 제목: 오타맨 고창영

## 문제 정보
- **출처:** https://www.acmicpc.net/problem/2711
- **난이도:** Easy, Medium, Hard 중 하나.

## 문제 설명
시도 수를 입력받고 
고창영의 오타가 난 단어와 오타 위치를 숫자로 입력 받아서(숫자, 단어)
단어에서 그 오타를 삭제하는 문제

## 해결 과정

1. 먼저 시도 수를 입력받는다 T = int(input())
2. 그리고 빈 리스트를 만들어서, 고창영의 오타리스트를 받을 준비 typos_list = []
3. T 갯수 만큼의 오타리스트와 오타 위치 번호를 입력받는다 
for _ in range(T):
    idx, s = input().split() #숫자와 단어를 공백값을 사이에 두고 입력받음 
    typos_list.append((int(idx), s))
4. 이렇게 받고나면 리스트 typos_list에 숫자 idx와, 오타 단어가 입력됨 (T개 만큼)
5. 그러면 그 idx와, s가 delete_typo라는 함수에 쏙 들어가서 T 숫자만큼 돌다가
6. delete_typo 함수의 결과로 리턴된 idx, s 값을 반환함 
for idx, s in typos_list:
    print(delete_typo(idx, s))
7. 자, 그럼 함수 delete_typo는 어떻게 구성되어 있냐면 
8. 숫자(index)와 단어(word)를 입력받아서 
9. word에서 숫자(index)에서 -1 하는 인덱스 값을 찾아서 거기까지 return을 하고 
10. 그 다음에 index에서 그 이후 끝까지 또 return을 한다...


### 접근 방법
위에 다 설명함 


## 코드
```python
def delete_typo(index, word:str) -> str:
    return word[:index -1] + word[index:]

T = int(input())

typos_list = []

for _ in range(T):
    idx, s = input().split()
    typos_list.append((int(idx), s))

for idx, s in typos_list:
    print(delete_typo(idx, s))
