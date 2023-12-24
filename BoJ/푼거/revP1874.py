#https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
stack= []
a =[]
cnt = 1  

while len(li):  
    while cnt<=li[0]:
        stack.append(cnt)
        a.append("+")
        cnt+=1
    
    if stack[-1] == li[0]:  
        stack.pop()
        li.pop(0)
        a.append("-")
    else:       #스택 Last와 검사할 숫자가 같지않으면 break
        break

if len(li): 
    print("NO")
else:    
    print(*a,sep="\n")
    