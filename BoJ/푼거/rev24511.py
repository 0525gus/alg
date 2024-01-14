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
#         if (li_c[k] == 0):
#                 j,li_d[k] = li_d[k],j
#     print(j,end=" ") # ㅇㅈ 

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
