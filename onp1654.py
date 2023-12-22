#https://www.acmicpc.net/problem/1654
# 리스트의 최솟값의 값부터 할당해 -1씩 해서  해당인자로부터 모두검색
import sys
a,b = map(int,input().split())
li = []
for _ in range(a):
    li.append(int(sys.stdin.readline()))
    
#출력 ans
ans =0 
minNum = min(li)
#cNum 을 minNum 에 할당 .. check 에도 할당 . 
while(1):
    cNum = minNum
    check = 0;
    for i in li:
        check += i//minNum
        
    if(check >= b):
        ans = check
        break
    else:
        minNum -=1
print(ans)