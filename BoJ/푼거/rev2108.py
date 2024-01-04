#https://www.acmicpc.net/problem/2108
import sys
import math
input = sys.stdin.readline

def round(n):
    if n -math.floor(n)<0.5:
        return math.floor(n)
    else:
        return math.ceil(n)

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li.sort()

san = round(sum(li)/len(li))

mid = list(set(li))[len(li)//2-1]



dic = {}
for i in li:
    if i not in dic:
        dic.setdefault(i,1)
    else:
        dic[i] += 1


mod = max(dic, key =dic.get)
        
bum = max(li)-min(li)

print(san,mid,mod,bum)