#https://www.acmicpc.net/problem/1654
# 매개변수탐색(이진탐색)

import sys
input = sys.stdin.readline

def binary_search_lan(target, arr):
    low, high = 1, max(lan)
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        comp = sum(i // mid for i in arr)
        if comp >= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

answer = binary_search_lan(N, lan)
print(answer)
