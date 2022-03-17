#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
m, n, k = map(int, input().split())
for _ in range(k):
    order = [i for i in range(1, n + 1)]
    check = list(map(int, input().split()))
    if len(check) == 0:
        print('NO')
        continue
    stack = []
    flag = 0
    while len(stack) <= m and check:
        if not stack:
            stack.append(order.pop(0))
        if stack[-1] == check[0]:
            stack.pop()
            check.pop(0)
            if not check:
                flag = 1
        else:
            if order:
                stack.append(order.pop(0))
            else:
                break
    if flag:
        print('YES')
    else:
        print('NO')