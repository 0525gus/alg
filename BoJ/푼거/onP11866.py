#https://www.acmicpc.net/problem/11866
N,K = map(int,input().split())
ansli = []
li = [i for i in range(1,N+1)]
print(li)
while(1):
    if(len(li)==0):
        break
    if K<len(li):
        print(len(li))
        
        ansli.append(li.pop(K))
    elif K>=len(li):
        print(len(li))
        ansli.append(li.pop(K%len(li)))
    
print(ansli)