#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
alpha = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
def judge(s, a):
    for i in set(a):
        if s.count(i) < a.count(i):
            return False
    return True
for n in range(int(input())):
    s = list(input())
    curr = 0
    while True:
        res = ''
        temp = s[:]
        for i in range(curr, len(alpha)):
            if not temp:
                break
            while judge(temp, alpha[i]):
                for j in list(alpha[i]):
                    temp.remove(j)
                res += str(i)
        if not temp:
            break
        curr += 1

    print(f'case #{n}:\n{res}')
