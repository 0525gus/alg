#https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline


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
