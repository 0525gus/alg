#https://www.acmicpc.net/problem/18110
#절사평균 -> N% 기준 위아래 30% -> 15% 15% 표본 제거
#round (2.5)-> 2 오류 --> 부동소수점 표기문제 
import math
import sys
input = sys.stdin.readline

def round(n):
    if n - math.floor(n)< 0.5:
        return math.floor(n)
    else:
        return math.ceil(n)
    
a = int(input())

li = []
for i in range(a):
    li.append(int(input()))
li.sort()
try:print(round(sum(li[round(0.15*a):a-round(0.15*a)]) / (a - 2*round(0.15*a))))
except:print(0)

