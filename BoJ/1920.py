import sys
def bi(list,low,high,target):
    mid = low + (high - low)/2
    mid = int(mid)
    if low > high:
        return 0
    if list[mid] == target:
        return 1
    elif list[mid]<target:
        return bi(list,mid+1,high,target)
    elif list[mid]>target:
        return bi(list,low,mid-1,target)
        
N = int(sys.stdin.readline())
li_N = list(map(int,sys.stdin.readline().split()))
li_N.sort()

M = int(sys.stdin.readline())
li_M = list(map(int,sys.stdin.readline().split()))

for i in li_M:
    print(bi(li_N,0,N-1,i)) 


# 마지막에서 에러 + 다른거 검색못함 // sol) mid에 +1// -1..