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
li = [int(input()) for _ in range(N)]
li.sort()
ari = round(sum(li)/len(li))
mid = li[round(len(li)/2)-1]
ran = max(li)-min(li)

dic = {}
for i in li:
    if i not in dic:
        dic.setdefault(i,1)
    else:
        dic[i] += 1 
max_num = max(dic, key=dic.get)  #키의 값들 중에서 가장 큰 밸류를 가진 해당 키값을 반환
max_num_value = dic[max_num] #해당 밸류

a = list(dic.values()).count(max_num_value)

if a==1:
    mod = max_num
else:
    ansli = [key for key,value in dic.items() if value == max_num_value]
    ansli.sort()
    mod = ansli[1]
    
    
    
    
print(ari,mid,mod,ran)