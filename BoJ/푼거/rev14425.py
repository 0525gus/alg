import sys
input = sys.stdin.readline
a,b = map(int,input().split())
s = set()
c = 0 
for i in range(a):
    d = input().rstrip()
    s.add(d)

for _ in range(b):
    d = input().rstrip()
    if d in s:
        c+=1
print(c)