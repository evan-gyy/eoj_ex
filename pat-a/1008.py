#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
t = 0
tmp = 0
sl = list(map(int, input().split()))[1:]
for i in sl:
    if i > tmp:
        t += (i - tmp) * 6 + 5
    else:
        t += (tmp - i) * 4 + 5
    tmp = i
print(t)