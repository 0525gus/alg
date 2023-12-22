import sys
N = int(sys.stdin.readline())
N_li = list(map(int,sys.stdin.readline().split()))
M = int(input())
M_li = list(map(int,sys.stdin.readline().split()))

dic={}
ansli=[]
for i in N_li:
    dic.setdefault(i,1)


for j in M_li:
    if j in dic.keys():
        ansli.append(1)
    else:
        ansli.append(0)
        
print(*ansli)