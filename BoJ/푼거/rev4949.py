#https://www.acmicpc.net/problem/4949
import sys
input = sys.stdin.readline

start_b ="[{("
end_b ="]})"
while(1):
    s_stack = []
    a = input().rstrip()
    if a ==".":
        break
    
    for i in a:
        if i in start_b:
            s_stack.append(i)
        elif(i in end_b):
            if len(s_stack) ==0:
                s_stack.append("NO")
                break
            fore = s_stack[-1]
            fore_num = start_b.index(fore)
            if i == end_b[fore_num]:
                s_stack.pop()
            else:
                break
    
    
    if s_stack:
        print("no")
    else:
        print("yes")
