#https://www.acmicpc.net/problem/1966
import sys
input = sys.stdin.readline

T= input()

for _ in range(T):
    h,t= 0,0
    N,M = map(int,input().split())
    N_li = list(map(int,input().split()))
    
    a = list(set(N_li))
    a.sort()
    
    a_li = {}
    for i in a:
        a_li[i] = a.count(i)
        
    M_check = M
    for i in a:
        current_impNum = a[-1]
        current_impNum_cnt = a_li[current_impNum]
        while(current_impNum_cnt):
            if current_impNum == N_li[0]:
                if M_check == M:     
                    N_li.pop(0)
        
        
    