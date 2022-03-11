#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
dic = {}
for i in range(int(input())):
    k = input()
    v = float(input())
    dic[k] = v
res = sorted(dic.items(), key=lambda x: x[1], reverse=True)
res = dict(res)
if 'magnus' in res:
    del res['magnus']
rl = list(res.keys())[:3]
rl.sort()
for j in rl:
    print(j)