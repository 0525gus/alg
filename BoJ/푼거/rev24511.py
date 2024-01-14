import sys
input = sys.stdin.readline
N = int(input().rstrip())
li_c = list(map(int,input().split()))
li_d = list(map(int,input().split()))
M = input()
M_li = list(map(int,input().split()))


# for j in M_li:
#     for k in range(N):
#         if (li_c[k] == 1):
#             continue
#         if (li_c[k] == 0): #굳이 0이 아닌부분도 싹다 한번씩 다 검사해서 누적하기 때문에 느리다
#                 j,li_d[k] = li_d[k],j
#     print(j,end=" ") # ㅇㅈ  -> 느리네  

#직접 쓰는 deq
MAX = 200001
li_deq =[0 for _ in range(MAX)]
h = t = MAX//2
for i in range(N):
    if li_c[i] ==0:
        li_deq[t] = (li_d[i])
        t +=1
for j in M_li:
    h-=1
    li_deq[h] = j
    print(li_deq[t-1],end=" ")
    t-=1

print()
# 표준라이브러리 덱을 사용하자
from collections import deque
res = deque()
for qs in range(N):
    if li_c[qs] == 0:
        res.appendleft(li_d[qs])
for i in range(int(M)):
    res.append(M_li[i])
    print(res.popleft(), end=" ");