#https://www.acmicpc.net/problem/18110
#절사평균 -> N% 기준 위아래 30% -> 15% 15% 표본 제거
#round (2.5)-> 2 오류 --> 부동소수점 표기문제 
import decimal
import sys
decimal.getcontext().rounding = decimal.ROUND_HALF_UP



a = int(sys.stdin.readline())
if a == 0:print(0)

else:
    li = []
    for i in range(a):
        li.append(int(sys.stdin.readline()))
    li.sort()
    
    #num = round(len(li)*(30/100))
    num = str(len(li)*(30/100)/2)
    num = decimal.Decimal(num).quantize(decimal.Decimal("1"))
    num =int(num)
    
    if(num == 0):
        end = None 
    else:
        end = -num
        

    ans = str(sum(li[num:end])/(len(li)-(num*2)))
    ans = decimal.Decimal(ans).quantize(decimal.Decimal("1"))
    print(int(ans))
