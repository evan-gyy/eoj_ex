#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
stack = []
for _ in range(int(input())):
    op = input().split()
    if len(op) > 1:
        stack.append(int(op[1]))
    else:
        if not stack:
            print('Invalid')
        elif op[0] == 'Pop':
            print(stack.pop())
        elif op[0] == 'PeekMedian':
            s = sorted(stack)
            l = len(stack)
            print(s[l//2-1 if l % 2 == 0 else (l+1)//2-1])
