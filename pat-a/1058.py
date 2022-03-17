#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
a, b = map(lambda x: x.split('.'), input().split())
res = [0 for _ in range(3)]
base = [10 ** 8 + 1, 17, 29]
flag = 0
for i in range(2, -1, -1):
    add = int(a[i]) + int(b[i]) + flag
    flag = 0
    while add >= base[i]:
        flag += 1
        add -= base[i]
    res[i] = add
print('.'.join(str(i) for i in res))
