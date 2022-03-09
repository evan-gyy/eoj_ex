#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from decimal import Decimal, ROUND_HALF_UP
res = 1
win = []
while True:
    try:
        inp = list(map(float, input().split()))
        res *= max(inp)
        win.append(['W', 'T', 'L'][inp.index(max(inp))])
    except:
        break
res = (res * 0.65 - 1) * 2
res = Decimal(res).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
print(' '.join(win), res)
