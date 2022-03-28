#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from itertools import permutations
for i in range(int(input())):
    n, m = map(int, input().split())
    cards = [int(j) for j in input().split()]
    max_sum = cards[0]
    for j in permutations(cards, 3):
        if sum(j) > m:
            continue
        else:
            max_sum = max(sum(j), max_sum)
    print(f'case #{i}:')
    print(max_sum)