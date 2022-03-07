#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
from datetime import datetime
sl = []
for i in range(int(input())):
    h = input().split()
    name = h[0]
    start = datetime.strptime(h[1], '%H:%M:%S').time()
    end = datetime.strptime(h[2], '%H:%M:%S').time()
    sl.append([name, start, end])
print(min(sl, key=lambda x: x[1])[0], max(sl, key=lambda x: x[2])[0])