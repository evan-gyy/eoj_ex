# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
n = int(input())
ai = input().split()
ai = [int(i) for i in ai]
bi = input().split()
bi = [int(i) for i in bi]
ai.sort(reverse=True)
bi_sum = sum(bi)
income = 0
for i in range(n):
    income += ai[i]
    if income >= bi_sum:
        print(i + 1)
        break
    if i == n - 1:
        print('Game Over!')
