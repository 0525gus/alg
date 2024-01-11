import sys
input = sys.stdin.readline

a= input().rstrip()
li = set()
cnt = 1;
while cnt < len(a)+1:
    for j in range(len(a)):
        if (j+cnt) == len(a)+1:  # j는 0부터시작하니깐 len(a)+1임.. (0+cnt) 
            ##ㅅㅂ len(a)+1 정신차려
            break 
        li.add(a[j:j+cnt])
    cnt+=1
print(li);
print(len(li));



# s=input().rstrip()
# total=set()
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         total.add(s[i:j+1])#i번째 문자부터 부분문자열 구하기
# print(total);
# print(len(total))