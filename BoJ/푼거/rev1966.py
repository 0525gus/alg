#https://www.acmicpc.net/problem/1966
import sys
input = sys.stdin.readline

T= int(input())

for _ in range(T):
    N,M = map(int,input().split())
    N_li = list(map(int,input().split())) 
    
    a = list(set(N_li)) 
    a.sort(reverse=True) 
    a_li = {}
    
    for i in a:
        a_li[i] = N_li.count(i)
        
    M_idx = M 
    checkNum = N_li[M]
    b = False
    ans = 0
    
    for j in a:
        if b:
            break
        cur_cnt = a_li[j]
        while cur_cnt:
    
            if N_li[0] == j: 
                N_li.pop(0)
                cur_cnt -=1
                ans +=1
                if M_idx == 0:
                    b =True
                    break
                elif M_idx > 0:
                    M_idx -=1
                    
            else:
                N_li.append(N_li.pop(0)) 
                if M_idx == 0:
                    M_idx = len(N_li)-1
                elif M_idx > 0:
                    M_idx -=1
    print(ans)

            