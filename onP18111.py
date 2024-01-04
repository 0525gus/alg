import sys
import math
input = sys.stdin.readline

N,M,B = map(int,input().split())
NMLi = []

def round(n):
    if n - math.floor(n)< 0.5:
        return math.floor(n)
    else:
        return math.ceil(n)
    


#NMSUM -> 모든 블럭의 합
NMSUM = 0
for i in range(N):
    temp_a = [j for j in map(int,input().split())]
    #temp_a = > 모두의 어레이
    NMSUM += sum(temp_a)
    NMLi.append(temp_a)

#평탄화 기준점 계산 위해 모든 블럭을 합한뒤 영역 갯수로 나눔-> 정수로 표현위해 반올림
fastBlock = round(NMSUM / (N*M))

#평탄화 기준점에 따른 필요한 블럭수 계산
needBlockNum = 0
for i in NMLi:
    for j in i:
        needBlockNum += abs(j-fastBlock)

for i in NMLi:
    for j in i:
        while needBlockNum < j:
            