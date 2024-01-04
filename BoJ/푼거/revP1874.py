#https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

<<<<<<< HEAD
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
    
=======

n = int(input())
li = [int(input()) for _ in range(n)]
stack= []
cnt = 1;
c = True
ans = []

while len(li):
    
    
    if cnt ==li[0]:
        li.pop(0)
        ans.append("+")
        ans.append("-")      
        cnt +=1
        continue
    if cnt ==1:
        stack.append(cnt)
        cnt +=1
        ans.append("+")
            
    temp = li[0]
    
    try:
        if(stack[-1]<temp):
            stack.append(cnt)
            ans.append("+")
            cnt+=1
            
        elif (stack[-1] == temp):
            li.pop(0)
            stack.pop(-1)
            ans.append("-")
        else:
            print("NO")
            c = False
            break
    except:
            print("NO")
            c = False
            break
        
if c ==True:
    print(*ans,sep="\n")
>>>>>>> ca23624c659542144cad5f1a3dc7768fc6edd7e0
