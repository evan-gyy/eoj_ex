#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import re
s = input().split('\"')[1:-1]
r = re.sub('\.|,|!|\?', '', ''.join(s).lower()).split()
while '' in r:
    r.remove('')
dic = {}
for i in r:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
res = []
temp = 0
for k, v in dic.items():
    if not res:
        res.append(k)
        temp = v
    else:
        if v < temp:
            break
        else:
            res.append(k)
res.sort()
print(res[0], temp)