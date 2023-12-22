import sys
input = sys.std.readline
alp_li = "abcdefghijklmnopqrstuvwxyz"
a = int(input())
b = input()
ans =0;
 
for i in range(0,len(b)):
    ans += (alp_li.index(b[i])+1)*(31**(i))
print(ans)







#해쉬 모듈 연산추가 
# alp_li = "abcdefghijklmnopqrstuvwxyz"
# a = int(input())
# b = input()
# ans = 0
# r = 31
# M = 1234567891

# for i in range(0, len(b)):
#     ans += (alp_li.index(b[i]) + 1) * (r ** i)

# ans %= M  # 모듈로 연산 추가
# print(ans)
