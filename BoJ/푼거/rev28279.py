import sys
input = sys.stdin.readline
MAX = 2000001
h,t = MAX//2,MAX//2
li = [0 for _ in range(MAX)]
for _ in range(int(input())):
    com = input().rstrip()
    if com[0] == "1":
        a,b = com.split()
        li[h-1] = b
        h -= 1
    if com[0] == "2":
        a,b = com.split()
        li[t] = b
        t += 1
        
    if com[0] == "3":
        if h != t:
            print(li[h]);
            li[h] = 0; #이파트.. 조심할것 (삭제가 아니다 그공간을 그대로 냅두는것임) .pop (x)
            h += 1
        else:
            print(-1)
            
    if com[0] == "4":
        if h != t:
            print(li[t-1]);
            li[t-1] = 0; #이파트.. 조심할것 (삭제가 아니다 그공간을 그대로 냅두는것임)
            t-=1
        else:
            print(-1)
            
    if com[0] == "5":
        print((t-h))
    if com[0] == "6":
        if(t==h):
            print(1)
        else:
            print(0)
    if com[0] == "7":
        if(t==h):
            print(-1)
        else:
            print(li[h])
    if com[0] == "8":
        if(t==h):
            print(-1)
        else:
            print(li[t-1])       
    
    




#더 깔끔한 풀이 표준 라이브러리 불러와서 해결
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# d = deque()

# for _ in range(N) :
#   order = list(map(int, input().split()))
#   l = len(d)

#   if order[0] == 1 :
#     d.appendleft(order[1])
#   elif order[0] == 2 :
#     d.append(order[1])
#   elif order[0] == 3:
#     print(d.popleft() if l else -1)
#   elif order[0] == 4 :
#     print(d.pop() if l else -1)
#   elif order[0] == 5 :
#     print(len(d))
#   elif order[0] == 6 :
#     print(0 if l else 1)
#   elif order[0] == 7 :
#     print(d[0] if l else -1)
#   elif order[0] == 8 :
#     print(d[-1] if l else -1)