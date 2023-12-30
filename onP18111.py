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
NMSUM = 0;
for i in range(N):
    temp_a = [j for j in map(int,input().split())]
    #temp_a = > 모두의 어레이
    NMSUM += sum(temp_a)
    NMLi.append(temp_a)

#평탄화 기준점 계산 (어느 평탄화 지점이 가장 높은가 ?(답이 많다면) )
fastBlock = round(NMSUM / (N*M))

#필요한 블럭수 계산
needBlockNum = 0;

for i in NMLi:
    for j in i:
        needBlockNum += abs(j-fastBlock)


if(needBlockNum>B):
    #
else:
