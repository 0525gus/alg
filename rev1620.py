import sys
input = sys.stdin.readline

a,b = map(int,input().split())
se = {}

for i in range(1,a+1):
    n= input().rstrip()
    se[n] = i
    se[str(i)] = n #str(i)이부분 -> dict 가져올때 type구분하니깐 조심

for _ in range(b):
    print(se[input().rstrip()])


