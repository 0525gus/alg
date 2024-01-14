import sys
input = sys.stdin.readline

N,M = map(int,input().split())
N_d = {}
a = []
for _ in range(N):
    N_d[input().rstrip()] = 1;

for _ in range(M):
    tmp = input().rstrip()
    if tmp in N_d:
        a.append(tmp)

a.sort() #sort  -> 문자열 사전순 정렬  
print(len(a))
for i in a:
    print(i)