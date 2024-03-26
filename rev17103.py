#골드바흐 
#에라토스테네스 다시생각
import sys;
input = sys.stdin.readline


prime = []
check = [True] * 1000001
check[0] = False
check[1] = False

for i in range(2,1000001):
    if check[i] == 1:
        prime.append(i)
        for j in range(2*i , 1000001, i ):
            check[j] = 0



T = int(input())
for _ in range(T):
    cnt = 0
    N = int(input())
    for i in prime:
        if i>=N:
            break
        if check[N-i] and i <=N-i:
            cnt +=1
    print(cnt)