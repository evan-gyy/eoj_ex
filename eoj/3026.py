#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def cal(s, size, remain):
    x = remain // size
    y = remain % size
    r = [x] * size
    for i in range(size-1, -1, -1):
        if y == 0:
            break
        r[i] += 1
        y -= 1
    res = ''
    for i in range(size):
        res += s[i] + ' '*r[i]
    res += s[-1]
    return ''.join(res)

for i in range(int(input())):
    m = int(input())
    s = input().split()
    print(f'case #{i}:')
    temp = []
    count = 0
    for j in range(len(s)):
        curr = s[j]
        if count + len(curr) >= m - (len(temp) - 1):
            if len(temp) == 1:
                print(temp[0])
            else:
                r = cal(temp, len(temp) - 1, m - count)
                print(r)
            temp = [curr]
            count = len(curr)
        else:
            count += len(curr)
            temp.append(curr)
    if len(temp) == 1:
        print(temp[0])
    else:
        print(' '.join(temp))