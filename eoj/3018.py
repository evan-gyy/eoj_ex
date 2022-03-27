#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import re
for i in range(int(input())):
    ptr = input().lower()
    s = input().lower().replace('.', '')
    loc = -1
    res = re.search('\s'+ptr+'\s', s)
    if res:
        loc = res.span()[0] + 2
    print(f"case #{i}:")
    if loc == -1:
        print('None')
    else:
        print(loc)
