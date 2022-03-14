#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
dic = {
    '1': '@',
    '0': '%',
    'l': 'L',
    'O': 'o'
}
n = int(input())
rl = []
for i in range(n):
    id, pwd = input().split()
    flag = 0
    for s in pwd:
        if s in dic:
            pwd = pwd.replace(s, dic[s])
            flag = 1
    if flag:
        rl.append(id + ' ' + pwd)
if rl:
    print(len(rl))
    for i in rl:
        print(i)
elif n == 1:
    print('There is 1 account and no account is modified')
else:
    print(f'There are {n} accounts and no account is modified')
