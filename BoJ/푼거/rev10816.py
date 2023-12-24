#https://www.acmicpc.net/problem/10816
import sys

N = int(sys.stdin.readline())
N_li = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_li = list(map(int, sys.stdin.readline().split()))

mydict = {}

for i in M_li:
    mydict.setdefault(i, 0)

for j in N_li:
    if j in mydict:
        mydict[j] += 1




#print
# print(*mydict.values())

# for i in M_li:
#     print(mydict[i],end=" ")

print(*[mydict[i] for i in M_li])