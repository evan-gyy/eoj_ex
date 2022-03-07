#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
arr = list(map(int, input().split()))
count = 0
start = 0
end = 0
temp = 0
p = 0
maxn = arr[0]
for i in range(n):
    temp += arr[i]
    # 如果加到这里变负了，直接调到下一个位置，重置temp为0，变负相对于加了等于白加
    if temp < 0:
        temp = 0
        p = i + 1
    # 如果加到这比之前大，则记录
    elif temp > maxn:
        maxn = temp
        start = p
        end = i

if max(arr) < 0:
    print(0, arr[0], arr[-1])
else:
    print(maxn, arr[start], arr[end])