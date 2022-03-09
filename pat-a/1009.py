#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from decimal import Decimal, ROUND_HALF_UP

class pol:
    def __init__(self, exp, cof):
        self.exp = exp
        self.cof = cof

    def __mul__(self, other):
        new_exp = self.exp + other.exp
        new_cof = self.cof * other.cof
        return pol(new_exp, new_cof)

    def __str__(self):
        return f"{self.exp} {self.cof}"

a = input().split()[1:]
b = input().split()[1:]
pa = []
pb = []
for i in range(0, len(a), 2):
    e = int(a[i])
    c = float(a[i+1])
    pa.append(pol(e, c))
for i in range(0, len(b), 2):
    e = int(b[i])
    c = float(b[i+1])
    pb.append(pol(e, c))

pnew = []
for i in pa:
    for j in pb:
        pnew.append(i * j)

pnew.sort(key=lambda x: x.exp, reverse=True)
res = {}
for i in pnew:
    if i.cof == 0.0:
        continue
    if i.exp not in res:
        res[i.exp] = i.cof
    else:
        res[i.exp] += i.cof
if len(res) == 0:
    # print('0 0 0')
    exit(0)
r = [len(res)]
for k, v in res.items():
    r.append(k)
    r.append(str(Decimal(v).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)))
print(' '.join([str(i) for i in r]))