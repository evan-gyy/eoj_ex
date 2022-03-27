#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
left = []
right = []
for i in range(n):
    a, b = map(int, input().split())
    if b:
        right.append(a)
    else:
        left.append(a)
left.sort()
right.sort()
if not left:
    print(len(right))
    exit(0)
if not right:
    print(len(left))
    exit(0)
if left[-1] == right[-1]:
    print(left.count(left[-1]) + right.count(right[-1]))
    exit(0)
elif left[-1] > right[-1]:
    left, right = right, left
m = max(left)
count = 0
for i in range(len(right)):
    if right[i] > m:
        count += 1
    elif right[i] == m:
        count += 2
print(count)