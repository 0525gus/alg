import sys
input = sys.stdin.readline

se = {}
for i in range(int(input())):
    n,s = map(str,input().rstrip().split())
    if ( s == "enter"):
        se[n] = 1
    elif( s == "leave"):
        se[n] = 0;

li = [] 
for k, v in se.items(): #this part
    if v == 1:
        li.append(k)
li.sort(reverse=True)

for i in li:
    print(i)
 