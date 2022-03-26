#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
a, b = map(int, input().split())
enc = {
    '2': -1,
    '1': 1,
    '0': 0
}
dec = {
    1: '1',
    0: '0',
    -1: '2'
}
sig = 1
if a < 0:
    sig = -1
    a = abs(a)
t = a % b
a //= b
ip, dp = '', ''
while a:
    ip = str(a % 3) + ip
    a //= 3
while t:
    t *= 3
    dp += str(t // b)
    t -= t // b * b
flag = 0
r1 = ''
ip = ip + dp
for i in range(len(ip)-1, -1, -1):
    n = sig * int(ip[i]) + 1 + flag
    flag = 0
    if n > 2:
        flag = 1
        n -= 3
    r1 = str(n) + r1
print(r1)
r2 = []
for i in range(len(r1)-1, -1, -1):
    n = int(r1[i]) - 1
    r2.insert(0, dec[n])
print(''.join(r2[:len(ip)-len(dp)]) + '.' + ''.join(r2[len(ip)-len(dp):]))