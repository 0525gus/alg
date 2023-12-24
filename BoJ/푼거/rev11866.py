#https://www.acmicpc.net/problem/11866
N,K = map(int,input().split())
li = [i for i in range(1,N+1)]
t = K-1
ansli = []
for _ in range(1,N+1):
    if t+K-1> len(li):
        t = t%len(li)
    ansli.append(li.pop(t))
    t+=K-1;
    
    
print(f"<{', '.join(map(str, ansli))}>")
