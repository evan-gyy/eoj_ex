#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
cards = []
for i in ['S', 'H', 'C', 'D']:
    for j in range(1, 14):
        cards.append(i+str(j))
cards.extend(['J1', 'J2'])
def shuffle(ord, card):
    rl = [0 for _ in range(len(card))]
    for i in range(len(card)):
        rl[ord[i] - 1] = card[i]
    return rl
n = int(input())
ord = list(map(int, input().split()))
for i in range(n):
    cards = shuffle(ord, cards)
print(' '.join(cards))