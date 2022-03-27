#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    a, b, n = map(int, input().split())
    print(f'case #{i}:')
    s = str(pow(a, b))
    r = s[-n:] if len(s) >= n else s.zfill(n)
    print(r)