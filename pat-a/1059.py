#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def get_prime(n):
    l = []
    for i in range(2, n):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag:
            l.append(i)
    return l
pl = get_prime(2000)
n = int(input())
r = str(n)
if n == 1:
    print('1=1')
    exit()
dic = {}
p = 0
while n != 1:
    d = pl[p]
    if n % d == 0:
        n //= d
        if d in dic:
            dic[d] += 1
        else:
            dic[d] = 1
    else:
        p += 1
rl = []
for k, v in dic.items():
    if v > 1:
        rl.append(f'{k}^{v}')
    else:
        rl.append(str(k))
print(r + '=' + '*'.join(rl))