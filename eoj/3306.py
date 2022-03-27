#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
p = int(input())
n1, n2, n3, n4 = map(int, input().split())
l = [25] * n4 + [10] * n3 + [5] * n2 + [1] * n1
sum = 0
count = 0
while l:
    if sum < p:
        sum += l.pop()
        count += 1
    else:
        break
if sum != p:
    print('Impossible')
else:
    print(count)