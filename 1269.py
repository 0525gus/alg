import sys
input = sys.stdin.readline

a,b = map(int,input().split())

a_li = set(list(map(int,input().split())))
b_li = set(list(map(int,input().split())))

print(len(a_li^b_li))