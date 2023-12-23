import sys
input = sys.stdin.readline

N= int(input())
li = []

for _ in range(N):
    a,b = map(int,input().split())
    li.append([a,b,0])
    

for i in range(len(li)):
    tempcnt = 0
    for j in li:
        if li[i][0]<j[0] and li[i][1]<j[1]:
            tempcnt +=1
    li[i][2] = tempcnt
    
print(*(li[i][2]+1 for i in range(N)))
        
    
    